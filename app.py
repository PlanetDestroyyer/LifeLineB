from flask import Flask, render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from waitress import serve

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get_involved")
def getinvolved():
    return render_template("get_involved.html")

@app.route("/donors")
def donors():
    return render_template("donors.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')