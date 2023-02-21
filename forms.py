from wtforms import Form
from flask import Flask
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField
from wtforms import validators

class UseForm(Form):
    matricula = StringField('Matricula',[
        validators.data_required(message = 'La matricula es requerida')]
                            )
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=5, max=15, message='Ingresa un numero minimo')])
    apaterno = StringField('Apaterno',[
        validators.data_required(message = 'El apellido es requerido')])
    apmaterno = StringField('Amaterno',[
        validators.data_required(message = 'El apellido es requerido')])
    email = EmailField('Email',[
        validators.data_required(message = 'El email es requerido')])
    
class NumberForm(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Este campo es requerido')])
        
class DiccionarioForm(Form):
    palabraIng = StringField('palabraIng',[
        validators.data_required(message = 'La palabra es requerida')])
    palabraEsp = StringField('palabraEsp',[
        validators.data_required(message = 'La palabra es requerida')])

    certification = RadioField('certification', choices = ['option1', 'option2'])