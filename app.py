from sqlalchemy.sql import text
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from random import Random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
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
    count = count.strip('('+')'+',')
    count = int(count)
    sql2 = f"INSERT INTO answers (question_id, answer1, answer2, answer3, answer4) VALUES ('{count}', '{answer1}','{answer2}','{answer3}','{right_answer}');"

    sql3 = f"INSERT INTO correct (question_id, answer) VALUES ('{count}', '{right_answer}');"
    print(f"{count} this is count")

    db.session.execute(text(sql2))
    #db.session.commit()

    db.session.execute(text(sql3))
    db.session.commit()

    #print(result)
    return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/get_question", methods=["GET"])
def get_question():
    sql = "SELECT COUNT(*) FROM questions;"
    result = db.session.execute(text(sql))
    count = str(result.fetchone())
    count = count.strip('('+')'+',')
    count = int(count)
    r = rng.randint(1,count)
    id = r
    print(f"id ennen kun haetaan kysymys {id}")
    sql = f"SELECT question FROM questions WHERE id = {id}"
    result = db.session.execute(text(sql))
    question = result.fetchone()
    print(f"id ennen kuin haetaan vastaukset {id}")
    sql = f"SELECT (answer1, answer2, answer3, answer4) FROM answers WHERE question_id = {id}"
    result = db.session.execute(text(sql))
    answers = result.fetchall()
    print("here is the result below")
    answer1, answer2, answer3, answer4 = answers[0][0].split(",")
    all = [answer1, answer2, answer3, answer4]

    final_answers = []
    for answer in all:
        #print(answer)
        answer = answer.strip('(' + ')' + '"')
        final_answers.append(answer)

    for a in final_answers:
        print(a)

    question = str(question)
    question = question.strip('(' + ')' + ',' + "'")
    print(question)
    randoms = []
    for i in range(4):
        randoms.append(i)
    rng.shuffle(randoms)
    print(randoms[3])

    return render_template("answer.html", question=question, answer1=final_answers[randoms[0]], answer2=final_answers[randoms[1]], answer3=final_answers[randoms[2]], answer4=final_answers[randoms[3]], id = id)

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
    correct = str(correct).strip('(' + ')' + ',' + "'" + '"')
    print(correct)
    #print(id)
    if correct == answer:
        return render_template("correct.html")
    else:
        return render_template("result.html", chosen=answer, id = id, correct = correct)