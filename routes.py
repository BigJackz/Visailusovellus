from app import app
from flask import redirect, render_template, session
from questions import get_all_questions, get_question_and_answers, get_result, send_question, loginn
from os import getenv

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = loginn()
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST", "GET"])
def send():
    answer = send_question()
    if answer == 1:
        return redirect("/success")
    elif answer == 2:
        #quite fat error message maybe make 3 separate errors at some point
        return (render_template("error.html", error = "Question, topic or one of the answers i"
        "s too long or short! Question must be between 1 and 100 characters, topic between 1 and 20 characters"
        " and answers between 1 and 30 characters."))
    elif answer == 3:
        return render_template("error.html", error = "Right answer can't be the same as a wrong answer!")
    elif answer == 4:
        return render_template("error.html", error = "Two or more answers can't be the same!")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/get_question", methods=["GET"])
def get_question():
    random_order, question, final_answers,id = get_question_and_answers(-1)
    return (render_template("answer.html", question=question, answer1=final_answers[random_order[0]],
            answer2=final_answers[random_order[1]], answer3=final_answers[random_order[2]],
            answer4=final_answers[random_order[3]], id = id))

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

@app.route("/questions", methods=["GET"])
def questions():
    questions = get_all_questions()
    return render_template("questions.html", questions=questions)

@app.route("/get_this_question", methods=["GET", "POST"])
def get_this_question():
    #id = int(request.form["id"])
    #print(id)
    random_order, question, final_answers, id = get_question_and_answers(-1)
    return (render_template("answer.html", question=question, answer1=final_answers[random_order[0]],
            answer2=final_answers[random_order[1]], answer3=final_answers[random_order[2]],
            answer4=final_answers[random_order[3]], id = id))