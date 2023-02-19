from flask import Flask, render_template
from flask import request

import forms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def iniciar():
    numero = 0
    num_form = forms.NumberForm(request.form)
    if request.method == 'POST':
        numero =  int(request.form.get("numero"))
    return render_template("Actividad1.html", num = numero, form = num_form)
    
@app.route("/resultado", methods=["POST"])
def generarResultado():
    valores = request.form.getlist("num")
    for i in range(0, len(valores)):
        valores[i] = int(valores[i])
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores)/len(valores)
    repetidos = {}
    mensajes = []
    for num in valores:
        if num in repetidos:
            repetidos[num] += 1
        else:
            repetidos[num] = 1

    for num, cantidad in repetidos.items():
        if cantidad > 1:
            mensajes.append("El número {} se repite {} veces.".format(num, cantidad))

    listResult = {'minimo': minimo, 
                  'maximo':maximo, 
                  'promedio': promedio,
                  'listaRep': mensajes
                  }
        
    return render_template('resultado.html', lista = listResult)


if __name__ =="__main__":
    app.run(debug=True, port=5000)