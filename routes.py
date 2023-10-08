from app import app
from flask import redirect, render_template
from questions import get_question_and_answers, get_result, send_question


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST", "GET"])
def send():
    send_question()
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
    correct, answer = get_result()
    if correct == answer:
        return render_template("correct.html")
    else:
        return render_template("result.html", chosen=answer, id = id, correct = correct)