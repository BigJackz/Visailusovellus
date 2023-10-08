from app import app
from db import db
from flask import redirect, render_template, request
from sqlalchemy.sql import text
from tools import make_string
import random


def get_question_and_answers():
    sql = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql))
    id = random.randint(1,int(make_string(str(result.fetchone()))))
    sql = f"SELECT question FROM questions WHERE id = {id}"
    result = db.session.execute(text(sql))
    question = result.fetchone()

    sql = f"SELECT (answer1, answer2, answer3, answer4) FROM answers WHERE question_id = {id}"
    result = db.session.execute(text(sql))
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
    sql = f"SELECT answer FROM correct WHERE question_id = {id}"
    result = db.session.execute(text(sql))
    correct = result.fetchone()
    correct = make_string(correct)
    return correct, answer

def send_question():
    question = request.form["question"]
    answer1 = request.form["answer1"]
    answer2 = request.form["answer2"]
    answer3 = request.form["answer3"]
    right_answer = request.form["right_answer"]
    sql = f"INSERT INTO questions (question) VALUES ('{question}');"

    db.session.execute(text(sql))
    db.session.commit()

    sql4 = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql4))
    count = str(result.fetchone())
    count = make_string(count)
    count = int(count)
    sql2 = f"INSERT INTO answers (question_id, answer1, answer2, answer3, answer4) VALUES ('{count}', '{answer1}','{answer2}','{answer3}','{right_answer}');"

    sql3 = f"INSERT INTO correct (question_id, answer) VALUES ('{count}', '{right_answer}');"

    db.session.execute(text(sql2))

    db.session.execute(text(sql3))
    db.session.commit()