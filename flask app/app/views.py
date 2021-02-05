# views.py

from flask import render_template
from app import app
#from app.models import *
from app.forms import *

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    fahrenheit_from(7)
    return render_template("about.html")

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)

@app.route("/<string:stringy>")
def test_string(stringy):
    return stringy

@app.route("/egg", methods=['GET','POST'])
def egg_route():
    form = CommandForm()
    egg = "uwu"

    if form.validate_on_submit():
        return render_template('result.html', command=form.command)
    
    return render_template("egg.html", string=egg, form=form)


@app.route("/result")
def result(command):
    return render_template("result.html", command="Hey there's no command here")
