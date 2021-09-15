class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
        self.__color()
 
    def display(self):
        print(self.name)
        print(self.__age)
        print(self.__color())
    #getter method to get age
    def getage(self):
        print(self.__age)
    #setter method to set age
    def setage(self,age):
        self.__age = age
    def __color(self):
        print("color is black")

    

 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
person.setage(25)
person.getage()
person._Person__color()

