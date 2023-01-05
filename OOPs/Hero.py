from copy import deepcopy
class Hero:
    # static variables
    profession = "Student"
    # constructor
    def __init__(self,orig=None,age=22,name="Name",password = "12345678") -> None:
        # print("constructor called...")
        if orig is None:
            self.__name = name
            self.__age = age
            self.__password = password
        else:
            self.copy_constructor(orig)

    def copy_constructor(self,orig):
        self.__dict__ = deepcopy(orig.__dict__)
    # static methods
    @staticmethod
    def ronaldo():
        print(Hero.profession)
        return "He is G.O.A.T."
    # methods
    def getname(self):
        return self.__name
    def __setname(self,name): #securing access to setname method, only accessible from inside class
        self.__name = name
    def nameset(self,name): # nameset function accessing setname method from inside
        self.__setname(name)
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age = age
    def getpassword(self):
        return self.__password
    def setpassword(self,password):
        self.__password = password
    
    def __del__(self):
        # print("destructor called...")
        pass

