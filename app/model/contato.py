class Contato():
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__tell = None
        self.__email = None

    @property
    def id (self):
        return self.__id

    @id.setter
    def id (self, var):
        self.__id = str(var)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, var):
        self.__name = str(var)


    @property
    def tell (self):
        return self.__tell

    @tell.setter
    def tell (self, var):
        self.__tell = str(var)

    @property
    def email (self):
        return self.__email

    @email.setter
    def email(self, var):
        self.__email = str(var)
