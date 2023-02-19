from wtforms import Form
from flask import Flask
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField
from wtforms import validators

class UseForm(Form):
    matricula = StringField('Matricula',[
        validators.data_required(message = 'La matricula es requerida')]
                            )
    nombre = StringField('Nombre')
    apaterno = StringField('Apaterno')
    apmaterno = StringField('Amaterno')
    email = EmailField('Email')
    
class NumberForm(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Este campo es requerido')])
    
