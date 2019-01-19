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
operand_upper_bound = 100
seed(a=None, version=2)
formatter = '%.2f'

# --------------------

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon"):
        """ Create a user """
        self.name = name
        self.qs_total = 0
        self.qs_correct = 0

def getPercentageCorrect(user):
    return 100 if user.qs_total == 0 else user.qs_correct / user.qs_total * 100

app.jinja_env.globals.update(getPercentageCorrect = getPercentageCorrect, formatter = formatter)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/problems", methods = ["GET", "POST"]) 
def ask_qs():
    if request.method == "GET" and (request.args.get("logout_button")  or session.get("userid", None) is None):
        session["userid"] = -1
        return redirect(url_for("index"))        
        
    if request.method == "POST":
        
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        
        if userid == -1:    # so it's a new user
            userid = len(users)
            user = User(uname)
            users.append(user)
        else:               # so we already know this user
            user = users[userid]

        session["userid"] = userid # save userid on client
    
    # if coming from "Next problem" button in mark.html:
    userid = session.get("userid", None)
    user = users[userid]
                
    # Handle GET method, when coming from mark.html > Next Problem button
    # Here calculate values and operation;
    term1 = randint(2, operand_upper_bound)
    term2 = randint(2, operand_upper_bound)
    opn = randint(0,3)  # Select index for one of +, -, *, /
    op = ops[opn][0] # get chosen function
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
def mark(): # Inform the user whether they're correct and display scores
    
    if request.method == "POST":
        formatter = '%.2f'
        leaders = []
        ua = request.form["user_answer"]
        answer = session.get("answer", None)
        userid = session.get("userid", None)
        if userid is None:
            return redirect(url_for("index"))
        users[userid].qs_total += 1
        correct = False            
        if ua == answer:
            correct = True
            users[userid].qs_correct += 1 
        percentCorrect = formatter % getPercentageCorrect(users[userid])
        users_sorted = sorted(users, key=lambda u: getPercentageCorrect(u), reverse = True)
        leader_percentage = getPercentageCorrect(users_sorted[0])
        # Check for multiple leaders
        for user in users_sorted:
            if getPercentageCorrect(user) == leader_percentage:
                leaders.append(user)        

        text = leaders[0].name
        if len(leaders) > 1:
            for vin in leaders[1:]:
                text += f' and {vin.name} '
            text += "are leading with "
        else:
            text += " is leading with "

        return render_template("mark.html",
            result = f'{ua} is {"" if correct else "in"}correct, {users[userid].name}.',
            feedback = 'Well done!' if correct else f'Sorry. :( The answer is in fact {answer}.',
            score = f'Your score is {users[userid].qs_correct} out of {users[userid].qs_total}.',
            percent = f'Your rating is {percentCorrect}%.',
            leader_text = text + f'{formatter % leader_percentage}%.',
            user_list = users_sorted)

# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
