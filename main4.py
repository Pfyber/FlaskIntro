from flask import Flask, render_template, request
#import requests
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinFlip")
def coinFlip():
    return render_template("coinFlip.html")

@app.route("/coinData")
def coinData():
    #print(request.form) v primeru POST
    print(request.args["vrednost"])
    rnd = random.randint(0,1)
    status =  ["HEADS", "TAILS"][rnd]
    return {"img" : "url", "status" : status}

#https://github.com/Pfyber/FlaskIntro
#templates, main4

app.run(debug = True)