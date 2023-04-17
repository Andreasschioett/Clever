from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


app = Flask(__name__)

dir = os.path.dirname(__file__)
db = os.path.join(dir, 'Clever.db')

@app.route("/")
def srtartside():
    with sqlite3.connect(db) as conn:
        c = conn.cursor()  
        c.execute("SELECT * FROM oplader")
        oplader = c.fetchall()
        print(oplader)
    return render_template("menu.html", oplader=oplader)

@app.route("/menu")
def menu():
    with sqlite3.connect(db) as conn:
        c = conn.cursor()  
        c.execute("SELECT * FROM oplader")
        oplader = c.fetchall()
        print(oplader)
    return render_template("menu.html", oplader=oplader)



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
    with sqlite3.connect(db) as conn:
        c = conn.cursor()  
        c.execute("SELECT * FROM oplader")
        oplader = c.fetchall()
    return render_template("menu.html", oplader=oplader)


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
    data = (new_value, old_value)
   

    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute("UPDATE oplader SET solcelle=? WHERE solcelle=?", data)
    return redirect('/')

query = "https://api.energidataservice.dk/dataset/CO2EmisProg?offset=0&sort=Minutes5UTC%20DESC&timezone=dk"
response = requests.get(query)
if response.status_code == 200:
    tidspunkter = []
    co2= []
    for x in response.json()['records']:
        tidspunkter.append(x['Minutes5DK'])
        co2.append(x["CO2Emission"])
    plt.plot(tidspunkter, co2)
    plt.ylabel('CO udledning')
    plt.xlabel('Tidspunkt')
    plt.xticks(rotation=90)
    plt.ylim(0, max(co2) + 100)
    plt.xticks(tidspunkter[::5])
    plt.subplots_adjust(bottom=0.5)
    plt.savefig('static/Screenshot_2.png')
    plt.clf()
else:
    # Print the error message
    print("Error: " + response.text)

today = datetime.now()
tommorrow = today + timedelta(days=1)
today = today.strftime("%Y-%m-%d")
tommorrow = tommorrow.strftime("%Y-%m-%d")
query2 = "https://api.energidataservice.dk/dataset/Elspotprices?offset=0&start=" + str(today) + "&end=" + str(tommorrow) + "&filter=%7B%22PriceArea%22:[%22DK1%22]%7D&sort=HourUTC%20DESC&timezone=dk"
response2 = requests.get(query2)
if response2.status_code == 200:
    tidspunkter2 = []
    pris = []
    for x in response2.json()['records']:
        tidspunkter2.append(x['HourDK'])
        pris.append(x["SpotPriceDKK"])
        plt.plot(tidspunkter2, pris)
        plt.ylabel('pris')
        plt.xlabel('Tidspunkt')
        plt.xticks(rotation=90)
        plt.ylim(0, max(pris) + 100)
        plt.xticks(tidspunkter2[::2])
        plt.subplots_adjust(bottom=0.5)
        plt.savefig('static/Screenshot_1.png')
        plt.clf()
    else:
        # Print the error message
        print("Error: " + response2.text)






if __name__ == '__main__':
    app.run(debug=True)