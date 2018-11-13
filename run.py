from flask import Flask, redirect, render_template, request, url_for, flash
from operator import add, sub, mul, truediv
import os
# from datetime import datetime
# import json

app = Flask(__name__)
app.secret_key = '12676506002A2822HOD940149670../"^$CCC320537618446744074370f95g51616'
ops = {'+': add, '-': sub, 'x': mul, '/': truediv}
# initial test data...
term1 = 6
term2 = 28
op = '+'
users = []

# --------------------

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon"):
        """ Create a user """
        self.name = name
        self.qs_total = 0
        self.qs_correct = 0

# keep a list of known users


class Q:
    """ Q, or Question class represents an arithmetical problem """
    def __init__(self, x = 0, y = 0, op = "+"):
        """ Create a new sum """
        self.x = x
        self.y = y
        self.op = op

@app.route("/")
def index():    
    return render_template("index.html")



@app.route("/problems", methods = ["GET", "POST"]) 
def ask_qs():
    if request.method == "POST":
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        if userid == -1:
            userid = len(users)
            user = User(uname)
            users.append(user)
        else:
            user = users[userid]
        # Here calculate values and operation; for now they're fixed;
        return render_template("problems.html", uname = user.name, x = term1, op = op, y = term2)
        

@app.route("/mark", methods = ["GET", "POST"])
def mark():
    if request.method == "POST":
        ua = request.form["user_answer"]
        return f'{ua} is {"" if ua == "34" else "in"}correct'
         




app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
