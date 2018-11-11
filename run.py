from flask import Flask, redirect, render_template, request # flash
from operator import add, sub, mul, truediv
import os
# from datetime import datetime
# import json

app = Flask(__name__)

ops = {'+': add, '-': sub, 'x': mul, '/': truediv}
# initial test data...
term1 = 6
term2 = 28
op = '+'
# --------------------

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon"):
        """ Create a user """
        self.name = name
        self.qs_total = 0
        self.qs_correct = 0

class Q:
    """ Q, or Question class represents an arithmetical problem """
    def __init__(self, x = 0, y = 0, op = "+"):
        """ Create a new sum """
        self.x = x
        self.y = y
        self.op = op

@app.route("/", methods = ["GET", "POST"])  
@app.route("/index", methods = ["GET", "POST"]) 
def index():
    if request.method == "POST":
        u = request.form["user_answer"]
        return render_template("mark.html") #, uname = "Anon", user_answer = u)  
    return render_template("index.html", uname = "Anon", x = term1, op = op, y = term2)

@app.route("/mark", methods = ["GET"])
def mark(uname, uanswer):
    return render_template("mark.html", uname = uname, user_answer = uanswer)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
