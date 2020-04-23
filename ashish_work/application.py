# import datetime
from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
# 	now=datetime.datetime.now()
# 	day= now.month==1 and now.day==1
# 	date = now
# 	return render_template("front.html", day=day,date=date)
@app.route("/")
def index():
	return render_template("index.html")
def more():
	return render_template("more.html")