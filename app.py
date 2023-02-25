from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Esta es una clave encriptada'
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template("404.html"),404

@app.before_request
def before_request():
    print('numero1')

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    print('numero2')
    reg_user = forms.LoginForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user =  reg_user.username.data
        passw = reg_user.password.data
        datos = user+'@'+passw
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)
    response = make_response(render_template("cookies.html", form = reg_user))
    response.set_cookie('datos_user', datos)
    return response

@app.after_request
def after_request(response):
    print('numero3')
    return response
    
@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombre = valor_cookie.split('@')[0]
    return render_template("saludo.html", nom = nombre)
    

@app.route("/formulario2", methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos", methods=["GET","POST"])
def Alumnos():
    alumn_form = forms.UseForm(request.form)
    mat =''
    nom =''
    if request.method == 'POST' and alumn_form.validate():
        mat =alumn_form.matricula.data
        nom = alumn_form.nombre.data
        alumn_form.apaterno.data
        alumn_form.apmaterno.data
        alumn_form.email.data
    return render_template('Alumnos.html', form = alumn_form, mat = mat, nom = nom)


if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=5000)
