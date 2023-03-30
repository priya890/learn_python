class Encapsulation:

    def __init__(self):
        self._a = 30
        self.__b = 40
        self.c = 50

    def get_var_a(self):
        return self._a

    def get_var_b(self):
        return self.__b

    def get_var_c(self):
        return self.c

    def __private_method(self):
        print(f"{self.c} This is private method")


class Child(Encapsulation):

    def display_a(self):
        print(self._a)


ex = Encapsulation()
# ex.__private_method()
# print(ex.get_var_a())
# print(ex.get_var_b())
# print(ex.get_var_c())
# print(ex.c)
print(ex._Encapsulation__b)
# ch = Child()
# ch.display_a()
