

##Andy Panagos
##Abstraction Assignment

from abc import ABC, abstractmethod
from ast import Pass

class Person1(ABC):
    @abstractmethod
    def walk(self): #Abtract method
        pass

    def stop(self): #Regular Function
        print("You stopped walking.")

class Person2(Person1): #Child Class
    def walk(self):
        print("He started walking.")

if __name__ == "__main__":
    p2 = Person2()
    p2.walk()
    p2.stop()
        
