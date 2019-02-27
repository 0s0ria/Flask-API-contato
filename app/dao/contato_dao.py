import sqlite3


class Contato_Dao():
    def connect(self):
        self.__db = sqlite3.connect('/home/leonardo/WORKSPACE/Flask-API-contato/app/dao/contato.db')
        self.__cursor = self.__db.cursor()

    def create(self,contato):
        Contato_Dao.connect(self)
        __query = """ INSERT INTO contato (name, tell, email)
                            VALUES(?,?,?);"""
        self.__cursor.execute(__query, (contato.name, contato.tell, contato.email))
        self.__db.commit()

    def read_all(self):
        Contato_Dao.connect(self)
        __query = """ SELECT * FROM contato """
        self.__cursor.execute(__query)
        return self.__cursor.fetchall()

    def read_one(self,contato):
        Contato_Dao.connect(self)
        __query = """ SELECT * FROM contato WHERE id = {}; """
        self.__cursor.execute(__query.format(contato.id))
        return self.__cursor.fetchall()

    def search(self,name):
        Contato_Dao.connect(self)
        __query = """ SELECT * FROM contato WHERE name LIKE '%{}%' ORDER BY name;"""
        self.__cursor.execute(__query.format(name))
        return self.__cursor.fetchall()

    def update(self,contato):
        Contato_Dao.connect(self)

        __query = """ UPDATE contato
        SET name = ?,
            tell = ?,
            email = ? WHERE id = ?"""
        self.__cursor.execute(__query)
        self.__db.commit()

    def delete(self,contato):
        Contato_Dao.connect(self)
        __query = """ DELETE FROM contato WHERE id = {} """
        self.__cursor.execute(__query.format(contato.id))
        self.__db.commit()

    
