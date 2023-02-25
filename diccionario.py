from flask import Flask, render_template
from flask import request

import forms, pruebas

app = Flask(__name__)

@app.route("/", methods=["GET"])
def iniciar():
    diccionario_form = forms.DGuardar(request.form)
    diccionario2_form = forms.DBuscar(request.form)
    return render_template('Diccionario.html', form = diccionario_form, form2 = diccionario2_form)


@app.route("/guardar", methods=["POST"])
def guardar():
    estado = ''
    diccionario_form = forms.DGuardar(request.form)
    diccionario2_form = forms.DBuscar(request.form)
    if request.method == 'POST' and diccionario_form.validate():
        pEsp = request.form.get('palabraEsp')
        pIng = request.form.get('palabraIng')
        estado =  pruebas.escribirPalabra(pEsp, pIng)
            
    return render_template('Diccionario.html', form = diccionario_form, form2 = diccionario2_form, estado = estado)

@app.route("/buscar", methods=["POST"])
def buscar():
    diccionario_form = forms.DGuardar(request.form)
    diccionario2_form = forms.DBuscar(request.form)
    result = ''
    if request.method == 'POST' and diccionario2_form.validate():
        diccionario = pruebas.crearDiccionario()
        palabra = request.form.get('palabra')
        if request.form.get('idioma') == 'Esp':
            result = (pruebas.buscarEsp(diccionario, palabra))
        else:
            result = (pruebas.buscarIng(diccionario, palabra))        
    return render_template('Diccionario.html', form = diccionario_form, form2 = diccionario2_form, result = result)


if __name__ =="__main__":
    app.run(debug=True, port=5000)