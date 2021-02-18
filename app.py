from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)