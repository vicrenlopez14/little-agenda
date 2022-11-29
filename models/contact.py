from persistance.database import database

from webargs import fields, flaskparser


def get_all_contacts():
    script = "SELECT * FROM contacts"
    contacts = database.execute_script_and_read_all(script)

    return [Contact.from_result_set(contact) for contact in contacts]


class Contact:
    def __init__(self, id=None, name=None, email=None, phone=None, address=None, alias=None, picture=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.alias = alias
        self.picture = picture

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Message: {self.alias}"

    @staticmethod
    def from_result_set(result_set):
        return Contact(result_set[0], result_set[1], result_set[2], result_set[3], result_set[4], result_set[5],
                       result_set[6])

    def get_by_id(self):
        script = f"SELECT * FROM contacts WHERE id = {self.id}"
        contact = database.execute_script_and_read_one(script)
        return Contact.from_result_set(contact)

    def create(self):
        script = f"INSERT INTO contacts (name, email, phone, address, alias, picture) VALUES ('{self.name}', '{self.email}', '{self.phone}', '{self.address}', '{self.alias}', '{self.picture}')"
        database.execute_script(script)

    def update(self):
        script = f"UPDATE contacts SET name = '{self.name}', email = '{self.email}', phone = '{self.phone}', address = '{self.address}', alias = '{self.alias}', picture = '{self.picture}' WHERE id = {self.id}"
        database.execute_script(script)

    def delete(self):
        script = f"DELETE FROM contacts WHERE id = {self.id}"
        database.execute_script(script)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "alias": self.alias,
            "picture": self.picture
        }
