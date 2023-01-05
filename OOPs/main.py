# from Hero import Hero
# print("1st call")
# foo = Hero(age=24)
# print(foo.getage(),foo.getname())

# print("3rd call")
# foo.nameset("JBL")
# print(foo.getage(),foo.getname())
class A:
    def __init__(self,a) -> None:
        self.a = a
    def __add__(self,obj):
        return obj.a - self.a

