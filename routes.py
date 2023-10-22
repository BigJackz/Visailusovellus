from app import app
from flask import redirect, render_template, session, request, abort
from questions import create_new_user, get_all_questions, get_question_and_answers, get_result, send_question, login_to_service
from os import getenv

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = login_to_service()
    if username == False:
        return render_template("error.html", error="There is no user with that username.")
    elif username == True:
        return render_template("error.html", error="Wrong password.")
    else:
        session["username"] = username
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_new_user", methods=["POST"])
def create_user():
    value = create_new_user()
    if value == 3:
        return render_template("account_created.html")
    elif value == 1:
        return render_template("error.html", error="That username is already taken!")
    else:
        return render_template("error.html", error="Username and password have to be atleast 3 characters long.")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST", "GET"])
def send():
    answer = send_question()
    if answer == 1:
        return redirect("/success")
    elif answer == 2:
        #quite big error message maybe make 3 separate errors at some point
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
    if id == False:
        return render_template("error.html", error="There is 0 questions added.")
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
    if questions == False:
        return render_template("error.html", error="There is 0 questions added.")
    return render_template("questions.html", questions=questions)

@app.route("/get_this_question", methods=["GET", "POST"])
def get_this_question():
    #id = int(request.form["id"])
    #print(id)
    random_order, question, final_answers, id = get_question_and_answers(-1)
    return (render_template("answer.html", question=question, answer1=final_answers[random_order[0]],
            answer2=final_answers[random_order[1]], answer3=final_answers[random_order[2]],
            answer4=final_answers[random_order[3]], id = id))