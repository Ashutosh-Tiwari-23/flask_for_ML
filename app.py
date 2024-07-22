from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h2>This is a Flask application</h2>"


# Variable rule, how a variable is passed to a function in Flask application
@app.route("/success/<int:score>")
def success(score):
    if (score) >= 55:
        return "The person has passed and the score is : " + str(score)
    else:
        return "The person has failed!"


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        english = float(request.form["english"])

        average_marks = (maths + science + english) / 3
        result = ""
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"

        return redirect(url_for(result, score=average_marks))


if __name__ == "__main__":
    app.run(debug=True)
