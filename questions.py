from calendar import TUESDAY
from app import app
from db import db
from flask import request
from sqlalchemy.sql import text
from tools import make_string, check_length
import random

#Checks if a topic already exists in the database returns true if it does otherwise returns false
def topic_exists(x):
    sql = "SELECT topic FROM topics;"
    result = db.session.execute(text(sql))
    topics = result.fetchall()
    for topic in topics:
        if make_string(topic) == x:
            return True
    return False

def get_all_questions():
    sql = "SELECT question FROM questions;"
    result = db.session.execute(text(sql))
    q = result.fetchall()
    db.session.commit()
    questions = []
    i = 1
    for q in q:
        questions.append((make_string(q),i))
        i += 1
    return questions

def get_question_and_answers(id):
    sql = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql))

    #set id to -1 to get a random question
    if id == -1:
        id = random.randint(1,int(make_string(str(result.fetchone()))))
    
    sql = f"SELECT question FROM questions WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    question = result.fetchone()

    sql = f"SELECT (answer1, answer2, answer3, answer4) FROM answers WHERE question_id = :id"
    result = db.session.execute(text(sql), {"id":id})
    answers = result.fetchall()

    answer1, answer2, answer3, answer4 = answers[0][0].split(",")
    all = [answer1, answer2, answer3, answer4]

    final_answers = []
    for answer in all:
        answer = make_string(answer)
        final_answers.append(answer)

    question = make_string(question)

    random_order = []
    for i in range(4):
        random_order.append(i)
    random.shuffle(random_order)

    return random_order, question, final_answers, id

def get_result():
    answer = request.form["answer"]
    id = request.form["id"]
    sql = f"SELECT answer FROM correct WHERE question_id=:id"
    result = db.session.execute(text(sql), {"id":id})
    correct = result.fetchone()
    correct = make_string(correct)
    return correct, answer

def send_question():
    question = request.form["question"]
    answer1 = request.form["answer1"]
    answer2 = request.form["answer2"]
    answer3 = request.form["answer3"]
    right_answer = request.form["right_answer"]
    answers = [answer1,answer2,answer3]
    topic = request.form["topic"].lower()

    #Check if the question and answers are correct length 2
    for answer in answers:
        if check_length(answer, 1, 30) == False:
            return 2
    if check_length(question, 1, 100) == False:
        return 2
    
    #Check if one of the wrong answers is same as right answer 3
    for answer in answers:
        if answer == right_answer:
            return 3

    #Finally check if two of the answers are the same return 4
    amount = 0
    for answer in answers:
        for answer2 in answers:
            if answer == answer2:
                amount += 1
    if amount > 3:
        return 4

    if not topic_exists(topic):
        sql = "INSERT INTO topics (topic) VALUES (:topic)"
        db.session.execute(text(sql), {"topic":topic})
        db.session.commit()

    sql6 = f"SELECT id FROM topics WHERE topic = '{topic}'"
    result = db.session.execute(text(sql6))
    topic_id = int(make_string(str(result.fetchone())))
    db.session.commit()

    sql = "INSERT INTO questions (topic_id, question) VALUES (:topic_id, :question)"
    db.session.execute(text(sql), {"topic_id":topic_id,"question":question})

    db.session.commit()



    sql = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql))
    count = str(result.fetchone())
    count = int(make_string(count))
    sql = f"INSERT INTO answers (question_id, answer1, answer2, answer3, answer4) VALUES (:count, :answer1, :answer2, :answer3, :right_answer);"
    sql1 = f"INSERT INTO correct (question_id, answer) VALUES (:count, :right_answer);"

    db.session.execute(text(sql), {"count":count, "answer1":answer1, "answer2":answer2, "answer3":answer3, "right_answer":right_answer})
    db.session.execute(text(sql1), {"count":count, "right_answer":right_answer})
    db.session.commit()
    return 1

