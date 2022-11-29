from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators, EmailField, IntegerField


class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=35), validators.DataRequired()])
    phone = IntegerField('Phone', [validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=6, max=35), validators.DataRequired()])
    alias = StringField('Alias', [validators.Length(min=6, max=35), validators.DataRequired()])
