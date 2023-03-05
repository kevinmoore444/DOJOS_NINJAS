from flask import Flask, render_template, request, redirect
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja
from flask_app import app


@app.route("/")
def index():
    all_dojos = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos=all_dojos)

@app.route("/dojos/create", methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')


@app.route('/dojos/<int:id>/view')
def get_all_dojo_ninjas(id):
    data = {
        'id':id
    }
    dojo_instance = Dojo.get_all_dojo_participants(data)
    return render_template("all_ninjas.html", dojo_instance=dojo_instance)
    