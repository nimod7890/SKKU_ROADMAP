from flask import Flask, render_template


applicationlication = Flask(__name__)


@applicationlication.route("/")
def hello():
    return render_template("main.html")


@applicationlication.route("/edu")
def edu():
    return render_template("edu.html")


@applicationlication.route("/educch")
def educch():
    return render_template("educch.html")


@applicationlication.route("/comedu")
def comedu():
    return render_template("comedu.html")


@applicationlication.route("/mathedu")
def mathedu():
    return render_template("mathedu.html")


@applicationlication.route("/create")
def create_by():
    return render_template("create_by.html")


@applicationlication.route("/create/bomintro")
def bomintro():
    return render_template("bomintro.html")


@applicationlication.route("/create/seokintro")
def seokintro():
    return render_template("seokintro.html")


@applicationlication.route("/create/sointro")
def sointro():
    return render_template("sointro.html")


if __name__ == "__main__":
    applicationlication.run(host='0.0.0.0')
