'''Inheritence: Male and Female class will have properties from Human class
   __ means private variable, _ means protected variable and without _ means public variable'''
class Human: # Parent class
    '''Human class is parent class for heirarchcal inheritence, bcz it is parent of Male and Female both class'''
    def __init__(self,weight = 50,height = 160) -> None:
        # print("Human class created...")
        self.__weight = weight # Kg
        self.__height = height # cm
    def getheight(self):
        return self.__height
    def getweight(self):
        return self.__weight
    def setheight(self,height):
        self.__height  = height
    def setweight(self,weight):
        self.__weight = weight
    def __del__(self):
        # print("Human class ended...")
        pass
class Male(Human): # single level inheritence "Human -> Male"
    def __init__(self, weight=50, height=160,name = "Name") -> None:
        # print("Male class created...")
        super().__init__(weight, height)
        self.__name = name
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name
    def __del__(self):
        # print("Male class ended..")
        return super().__del__()

class Female(Human): 
    def __init__(self, weight=50, height=160,name = "SName") -> None:
        super().__init__(weight, height)
        self.__name = name
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name
    @staticmethod
    def talkitive():
        return "Yes, female are talkitive"
    def __del__(self):
        # print("Female class ended...")
        return super().__del__()

class Indian(Male): # multi level inheritence "Human -> Male -> Indian"
    def __init__(self, weight=50, height=160, name="Name") -> None:
        super().__init__(weight, height, name)
        self.__language = "Hindi"
    def getlanguage(self):
        return self.__language
    def __del__(self):
        # print("Indian class ended...")
        return super().__del__()


class American(Male):
    def __init__(self, weight=50, height=160, name="Name") -> None:
        super().__init__(weight, height, name)
        self.__language = "English"
        self.booze = "Beer"
    def getlanguage(self):
        return self.__language
    def __del__(self):
        # print("American class ended...")
        return super().__del__()

class Sundar(Indian,American): # multiple inheritence "American -> Sundar <- Indian"
    def __init__(self, weight=50, height=160, name="Name") -> None:
        super().__init__(weight, height, name)
        self.profession = "CEO"
        self.resident = "CA"
    def __del__(self):
        # print("Sundar class ended...")
        return super().__del__()

foo = Sundar()
# foo.__name = "Jenish"
# foo.__height = 189
# foo.__weight = 78

foo.setname("Sundar")
foo.setheight(170)
foo.setweight(56)
# foo.language = "Gujarati"
# foo.resident = "NY"
# foo.booze = "Vodka"
# foo.profession = "oops"

print(f"height :{foo.getheight()}")
print(f"weight :{foo.getweight()}")
print(f"name :{foo.getname()}")
print(f"language :{foo.getlanguage()}")
# print(f"booze :{foo.booze}")
# print(f"profession :{foo.profession}")
# print(f"resident :{foo.resident}")