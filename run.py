from flask import Flask, redirect, render_template, request, url_for, session
from operator import add, sub, mul, truediv
import os
from random import seed, randint
# from datetime import datetime
# import json

app = Flask(__name__)
app.secret_key = '12676506002A2822HOD940149670../"^$CCC320537618446744074370f95g51616'
ops = [('+', add), ('-', sub), ('x', mul), ('/', truediv)]
users = []    # keep a list of known users
user = ''
userid = -1
operand_upper_bound = 16
seed(a=None, version=2)
# --------------------

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon"):
        """ Create a user """
        self.name = name
        self.qs_total = 0
        self.qs_correct = 0

# class Q:
#     """ Q, or Question class represents an arithmetical problem """
#     def __init__(self, x = 0, y = 0, op = "+"):
#         """ Create a new sum """
#         self.x = x
#         self.y = y
#         self.op = op

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/problems", methods = ["GET", "POST"]) 
def ask_qs():
    if request.method == "POST":
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        if userid == -1:    # so it's a new user
            userid = len(users)
            user = User(uname)
            users.append(user)
        else:               # so we already know this user
            user = users[userid]
        # Here calculate values and operation;
        term1 = randint(2, operand_upper_bound)
        term2 = randint(2, operand_upper_bound)
        opn = randint(0,3)  # Select one of +, -, *, /
        op = ops[opn][0]
        # Handle division by doing pre-multiplication, so we get result castable to integer
        if opn == 3:
            term1 *= term2
        opfn = ops[opn][1]
        answer = opfn(term1, term2)
        if opn == 3:
            answer = int(answer)    # For division, cast to int, because truediv returns a float
        session["answer"] = str(answer)
        return render_template("problems.html", uname = user.name, x = term1, op = op, y = term2)        

@app.route("/mark", methods = ["GET", "POST"])
def mark():
    if request.method == "POST":
        ua = request.form["user_answer"]
        answer = session.get("answer", None)
        users[userid].qs_total += 1
        correct = False            
        if ua == answer:
            correct = True
            users[userid].qs_correct += 1 
        return render_template("mark.html",
            result = f'{ua} is {"" if correct else "in"}correct, {users[userid].name}',
            score = f'Your score is {users[userid].qs_correct} out of {users[userid].qs_total}')

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
