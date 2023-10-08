from app import app
from db import db
from flask import redirect, render_template, request
from sqlalchemy.sql import text

from tools import make_string
import random
#rng = Random

def get_question_and_answers():
    sql = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql))
    r = random.randint(1,int(make_string(str(result.fetchone()))))
    id = r
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