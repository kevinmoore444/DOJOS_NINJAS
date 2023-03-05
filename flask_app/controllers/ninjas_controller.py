from flask import Flask, render_template, request, redirect
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja
from flask_app import app


@app.route("/ninja/new")
def ninja_new():
    all_dojos = Dojo.get_all_dojos()
    return render_template("ninja_new.html", all_dojos=all_dojos) 

@app.route("/ninja/create", methods=['POST'])
def ninja_create():
    Ninja.create(request.form)
    return redirect('/')


