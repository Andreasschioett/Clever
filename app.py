from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os
import sqlite3


app = Flask(__name__)

dir = os.path.dirname(__file__)
db = os.path.join(dir, 'Clever.db')

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

#function that gets the data from clever.db opklader and sends it to the html file
@app.route("/data")
def data():
    with sqlite3.connect(db) as conn:
        c = conn.cursor()  
        c.execute("SELECT * FROM oplader")
        oplader = c.fetchall()
        print(oplader)
    return render_template("data.html", oplader=oplader)



# DML inset profile data into database in table kunde
@app.route('/create', methods=['POST'])
def create():
    navn = request.form.get('Navn')
    email = request.form.get('email')
    password = request.form.get('password')
    adresse = request.form.get('adresse')
    data = (navn, email, password, adresse)
    
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO kunde (navn, email, password, adresse) VALUES (?, ?, ?, ?)", data)
    return redirect('/')




# DML update oplader udelukende in database in table oplader
@app.route('/update', methods=['POST'])
def update():
    solcelle = request.form.get('solcelle')
    if solcelle == "true":
        new_value = 1
        old_value = 0
    else:
        new_value = 0
        old_value = 1

    print(new_value)
    print(solcelle)
    data = (new_value, old_value)
    print(data)

    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute("UPDATE oplader SET solcelle=? WHERE solcelle=?", data)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)