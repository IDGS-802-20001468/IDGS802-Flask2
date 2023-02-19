from flask import Flask, render_template
from flask import request

import forms

app = Flask(__name__)

@app.route("/", methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos", methods=["GET","POST"])
def Alumnos():
    alumn_form = forms.UseForm(request.form)
    mat =''
    nom =''
    if request.method == 'POST':
        mat =alumn_form.matricula.data
        nom = alumn_form.nombre.data
        alumn_form.apaterno.data
        alumn_form.apmaterno.data
        alumn_form.email.data
    return render_template('Alumnos.html', form = alumn_form, mat = mat, nom = nom)


if __name__ =="__main__":
    app.run(debug=True, port=5000)