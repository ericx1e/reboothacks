from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/challenge")
def newpage():
    return render_template("challenge.html")

@app.route("/easter-egg")
def newpage1():
    return render_template("easter-egg.html")
