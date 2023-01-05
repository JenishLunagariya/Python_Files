'''polymorphism: function overloading, operator overloading & method overiding'''
class Animal:
    def __init__(self) -> None:
        pass
    def speak(self):
        return "animal speaks"
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
    def speak(self): # method overiding
        '''it overrides parent speak method'''
        return "dog barks"
a = Animal()
print(a.speak())
b = Dog()
print(b.speak())
class A:
    def __init__(self,a) -> None:
        self.a = a
    def __add__(self,obj): # operator overloading
        '''+ operator sums up, but we are overriding it to return substraction, when two A class
           objects use + betweeen them'''
        return obj.a - self.a
x = A(4)
y = A(7)
print(x + y) #3 <-class method
print(4 + 3) #7 <-built-in method