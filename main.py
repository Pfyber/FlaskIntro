from flask import Flask, render_template
import requests
# pip install flask
app = Flask(__name__)

chuck_url = "https://api.chucknorris.io/jokes/random"

@app.route("/")
def index():
    call = requests.get(chuck_url).json()
    joke = call["value"]
    name = "Luka Colarič"
    return render_template("index.html", author = joke)

@app.route("/about")
def about():
    return "<h1>Welcome to about page</h1>"

app.run(debug = True)