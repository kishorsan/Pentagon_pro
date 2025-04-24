class Shop:
    def __init__(self):
        self.__price = 1000

    def getter(self):
        return self.__price
    
    def setter(self):
        self.__price = self.__price * (100-10)/100

    getset = property(getter, setter)

s1 = Shop()
print(s1.getset)
s1.setter()
print(s1.getset)
