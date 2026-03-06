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
    print(requests.args)
    if request.method == "POST":
        return {"temp": 20, "hum": 30}
        
    return render_template("index2.html")

# route to show 100% of all data in request header, body, query string, etc.    
@app.route("/showall", methods = ["GET", "POST"])
def show_all():
    return {
        "headers": dict(request.headers),
        "form": dict(request.form),
        "args": dict(request.args),
        "json": request.get_json() if request.is_json else None
    }

# route to show difference for handling post or get method and show data from jquery ajax data packet from both methods
@app.route("/showmethod", methods = ["GET", "POST"])
def show_method():
    if request.method == "POST":
        return {
            "method": "POST",
            "headers": dict(request.headers),
            "form": dict(request.form),
            "args": dict(request.args)
        }
    else:
        return {
            "method": "GET",
            "headers": dict(request.headers),
            "form": dict(request.form),
            "args": dict(request.args)
        }
app.run(debug = True)