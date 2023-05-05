import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            r'C:\Users\Shadow\Desktop\python_basics\14.2_Tets_framework'
            r'\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers " \
                f"WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
