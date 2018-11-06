from flask import Flask, redirect, render_template, request # flash
import os
# from datetime import datetime
import json

app = Flask(__name__)

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon"):
        """ Create a new point at x, y """
        self.name = name
        self.qs_total = 0
        self.qs_correct = 0



@app.route("/", methods = ["GET", "POST"])	
@app.route("/index", methods = ["GET", "POST"])	
def index():	
	return render_template("index.html")

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT', 5000)), debug=True)
