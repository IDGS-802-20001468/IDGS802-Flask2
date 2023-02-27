from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms, calculos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave encriptada calculo de resistencias'
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template("Error404.html"),404

@app.before_request
def before_request():
    print('Bienvenido a la aplicacion')

@app.route("/", methods=["GET", "POST"])
def iniciar():
    reg_user = forms.InicioForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        datos =  reg_user.Nombre.data
        motivo = reg_user.motivo.data
        success_message = 'Bienvenido {}'.format(datos)
        flash(success_message)
    response = make_response(render_template("Inicio.html", form = reg_user))
    response.set_cookie('datos', datos)
    return response

@app.route("/Resistencia", methods=["GET", "POST"])
def calcularR():
    print('Calculo de resistencias')
    res = {}
    color ={}
    valor_cookie = request.cookies.get('datos')
    form = forms.ResistenciaForm(request.form)
    if request.method == 'POST' and form.validate():
        banda1 = request.form.get('banda1')
        banda2 = request.form.get('banda2')
        banda3 = request.form.get('banda3')
        rbt =  request.form.get('tolerancia')
        valor = calculos.calcularValor(banda1,banda2,banda3, rbt, 1)
        mini= calculos.calcularValor(banda1,banda2,banda3, rbt, 2)
        maxi= calculos.calcularValor(banda1,banda2,banda3, rbt, 3)
        res = {'b1': banda1,
            'b2': banda2,
            'b3': banda3,
            'b4': rbt,
            'val': valor,
            'mini': mini,
            'maxi': maxi
            }
        color = calculos.mostrarColores(banda1,banda2,banda3,rbt)
    return render_template("Resistencia.html", form = form, res = res, color = color, nombre = valor_cookie)

@app.after_request
def after_request(response):
    print('Estas usando una aplicacion para calcular resistencias')
    return response


if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)