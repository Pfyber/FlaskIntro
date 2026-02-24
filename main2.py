from flask import Flask, render_template, request
import requests
# pip install flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
 
    

@app.route("/temp", methods = ["GET", "POST"])
def data():
    print(request.form)
    if request.method == "POST":
        return {"temp": 20, "hum": 30}
        
    return render_template("index2.html")
    

app.run(debug = True)