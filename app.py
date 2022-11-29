from flask import Flask, render_template, url_for, request, redirect, flash

import models.contact
from forms.agenda_forms import ContactForm
from models.contact import Contact

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    contacts = models.contact.get_all_contacts()
    return render_template("index.html", contacts=contacts)


@app.route('/create', methods=['GET', 'POST'])
def create_contact():
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        contact = Contact(name=form.name.data, email=form.email.data, phone=form.phone.data, address=form.address.data,
                          alias=form.alias.data)
        contact.create()
        return redirect(url_for('index'))

    return render_template("create_contact.html", form=form)


@app.route('/delete/<id>')
def delete_contact(id):
    contact = Contact(id=id)
    contact.delete()
    return redirect(url_for('index'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update_contact(id):
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        contact = Contact(id=id, name=form.name.data, email=form.email.data, phone=form.phone.data,
                          address=form.address.data,
                          alias=form.alias.data)
        contact.update()
        return redirect(url_for('index'))

    contact = Contact(id=id)
    contact = contact.get_by_id()

    form.name.data = contact.name
    form.email.data = contact.email
    form.phone.data = contact.phone
    form.address.data = contact.address
    form.alias.data = contact.alias
    
    return render_template("update_contact.html", contact=contact, form=form)


if __name__ == '__main__':
    app.run(debug=True)
