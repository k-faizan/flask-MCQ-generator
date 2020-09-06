from flask import Flask,render_template,url_for,request,redirect


app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")


@app.route('/mechanical')
def mechanical():
    return render_template("mech.html")


@app.route('/dev')
def dev():
    return render_template("dev.html")