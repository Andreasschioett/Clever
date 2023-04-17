from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os


app = Flask(__name__)

@app.route("/")
def startside():
    return render_template("menu.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/Settings")
def Settings():
    return render_template("Settings.html")

@app.route("/kort")
def kort():
    return render_template("kort.html")

@app.route("/Profile")
def Profile():
    return render_template("Profile.html")

@app.route("/Overblik")
def Overblik():
    return render_template("Overblik.html")

@app.route("/strømpris")
def strømpris():
    return render_template("strømpris.html")

@app.route("/co2udledning")
def co2udledning():
    return render_template("co2udledning.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("menu.html")




if __name__ == '__main__':
    app.run(debug=True)