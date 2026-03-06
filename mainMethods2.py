# POST / GET metode
from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        print(request.form) #request.form["zipcode"]
        return {"num" : random.randint(1,100)}
    return render_template("methods.html")
    # če ajax tipa get... request.args

app.run(debug=True)