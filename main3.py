from flask import Flask, request, render_template
#import requests
import random
# pip install flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinFlip")
def coinFlip():
    return render_template("coin.html")

@app.route("/coinData")
def coinData():
    # POST request.form
    #GET
    print(request.args["vrednost"])
    rnd = random.randint(0,1)
    status =  ["TAILS", "HEADS"][rnd]
    return {"img" : "url", "status" : status}
#ImmutableMultiDict([('zipcode', '97201'), ('vrednost', 'asassa')])
app.run(debug = True)