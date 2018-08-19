from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from flask_wtf.file import FileField

class TranslitForm(FlaskForm):

    translit = TextAreaField("Translit", render_kw={"placeholder": "Translit"})
    translit_arm = TextAreaField("Armenian", render_kw={"placeholder": "Armenian"})

    message = TextAreaField("Comments", render_kw={"placeholder": "Please Write your comment here in the following format. \n Incorrect Translit \n Proceed with a detailed message"})

    upload = SubmitField("Upload")
    save = SubmitField("Save")
