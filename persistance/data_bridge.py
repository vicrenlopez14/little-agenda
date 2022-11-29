import sqlite3


# Load schema from schema.sql file
def read_script_content():
    with open("schema.sql", "r") as file:
        return file.read()


def __new_connection__():
    return sqlite3.connect('base.sqlite')


class DataBridge:
    def __init__(self):
        DataBridge.execute_script(read_script_content())

    @staticmethod
    def execute_script(script):
        conn = __new_connection__()
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()

    @staticmethod
    def execute_script_and_read_all(script):
        conn = __new_connection__()
        cursor = conn.cursor()
        cursor.execute(script)

        return cursor.fetchall()

    @staticmethod
    def execute_script_and_read_one(script):
        conn = __new_connection__()
        cursor = conn.cursor()
        cursor.execute(script)
        return cursor.fetchone()
