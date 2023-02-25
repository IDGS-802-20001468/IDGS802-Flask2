from wtforms import Form
from flask import Flask
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField
from wtforms import validators

def mi_validacion(form, field):
     if len(field.data) == 0:
          raise validators.ValidationError('El campo no tiene datos')

class UseForm(Form):
    matricula = StringField('Matricula',[
        validators.data_required(message = 'La matricula es requerida')]
                            )
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=5, max=15, message='Ingresa un numero minimo')])
    apaterno = StringField('Apaterno',[mi_validacion])
    apmaterno = StringField('Amaterno',[
        validators.data_required(message = 'El apellido es requerido')])
    email = EmailField('Email',[
        validators.data_required(message = 'El email es requerido')])
    
class NumberForm(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Este campo es requerido')])
        
class DGuardar(Form):
    palabraIng = StringField('palabraIng',[
        validators.data_required(message = 'La palabra es requerida')])
    palabraEsp = StringField('palabraEsp',[
        validators.data_required(message = 'La palabra es requerida')])

class DBuscar(Form):
    palabra = StringField('palabra',[
        validators.data_required(message = 'La palabra es requerida')])
    idioma = RadioField('idioma', [validators.DataRequired(message='Seleccione una opcion')] ,choices=[('Esp','Español'),('Ing','Ingles')])

class LoginForm(Form):
    username = StringField('usuario',[
        validators.data_required(message = 'El usuario es requerido')]
                            )
    password = PasswordField('contraseña', [validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=5, max=15, message='Ingresa un numero minimo')]
                        )