# views.py

from flask import render_template
from app import app
#import

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/athena')
def athena():
    return render_template("athena.html")


#@app.route("/<int:celsius>")
#def fahrenheit_from(celsius):
#    """Convert Celsius to Fahrenheit degrees.
#    fahrenheit = float(celsius) * 9 / 5 + 32
#    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
#    return str(fahrenheit)"""