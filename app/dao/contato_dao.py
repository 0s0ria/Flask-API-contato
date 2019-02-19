import sqlite3


class Contato_Dao():
    def __init__(self, contato):
        self.__id = contato.id
        self.__name = contato.name
        self.__tell = contato.tell
        self.__email = contato.email
        self.__db = sqlite3.connect('/home/leonardo/WORKSPACE/Flask-API-contato/app/dao/contato.db')
        self.__cursor = self.__db.cursor()

    def create(self):
        self.__query = """ INSERT INTO contato (name, tell, email)
                            VALUES(?,?,?);"""
        self.__cursor.execute(self.__query, (self.__name, self.__tell, self.__email))
        self.__db.commit()

    def read_all(self):
        self.__query = """ SELECT * FROM contato """
        self.__cursor.execute(self.__query)
        return self.__cursor.fetchall()

    def read_one(self):
        self.__query = """ SELECT * FROM contato WHERE id = ?; """
        self.__cursor.execute(self.__query, (self.__id))
        return self.__cursor.fetchall()

    def search(self):
        self.__query = """ SELECT * FROM contato WHERE name LIKE '%{}%' ORDER BY name;"""
        self.__cursor.execute(self.__query.format(self.__name))
        return self.__cursor.fetchall()

    def update(self):
        self.__query = """ UPDATE contato
        SET name = ?,
            tell = ?,
            email = ? WHERE id = ?"""
        self.__cursor.execute(self.__query,(self.__name,self.__tell,self.__email,self.__id))
        self.__db.commit()

    def delete(self):
        self.__query = """ DELETE FROM contato WHERE id = ? """
        self.__cursor.execute(self.__query,(self.__id))
        self.__db.commit()
