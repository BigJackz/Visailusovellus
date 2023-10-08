from app import app
from db import db
from flask import redirect, render_template, request
from sqlalchemy.sql import text
from random import Random
from tools import make_string
from questions import get_question_and_answers

rng = Random()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST", "GET"])
def send():
    question = request.form["question"]
    answer1 = request.form["answer1"]
    answer2 = request.form["answer2"]
    answer3 = request.form["answer3"]
    right_answer = request.form["right_answer"]
    sql = f"INSERT INTO questions (question) VALUES ('{question}');"
    
    print(sql)

    db.session.execute(text(sql))
    db.session.commit()

    sql4 = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql4))
    count = str(result.fetchone())
    count = make_string(count)
    count = int(count)
    sql2 = f"INSERT INTO answers (question_id, answer1, answer2, answer3, answer4) VALUES ('{count}', '{answer1}','{answer2}','{answer3}','{right_answer}');"

    sql3 = f"INSERT INTO correct (question_id, answer) VALUES ('{count}', '{right_answer}');"
    print(f"{count} this is count")

    db.session.execute(text(sql2))

    db.session.execute(text(sql3))
    db.session.commit()

    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/get_question", methods=["GET"])
def get_question():
    random_order, question, final_answers,id = get_question_and_answers()
    return render_template("answer.html", question=question, answer1=final_answers[random_order[0]], answer2=final_answers[random_order[1]], answer3=final_answers[random_order[2]], answer4=final_answers[random_order[3]], id = id)

@app.route("/answer")
def answer():
    return render_template("answer.html")

@app.route("/result", methods=["POST","GET"])
def result():
    answer = request.form["answer"]
    id = request.form["id"]
    sql = f"SELECT answer FROM correct WHERE question_id = {id}"
    result = db.session.execute(text(sql))
    correct = result.fetchone()
    correct = make_string(correct)
    print(correct)
    if correct == answer:
        return render_template("correct.html")
    else:
        return render_template("result.html", chosen=answer, id = id, correct = correct)