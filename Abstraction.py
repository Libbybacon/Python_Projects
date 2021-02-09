##Create a class that utilizes the concept of abstraction.
##
##1. Your class should contain at least one abstract method and one regular method.
##
##2. Create a child class that defines the implementation of its parents abstract method.
##
##3. Create an object that utilizes both the parent and child methods.

from abc import ABC, abstractmethod

class sale(ABC):
    def price(self):
        item = input('Which item, car or boat, are you purchasing?\n>>>  ').lower()
        if item == 'car':
            itemPrice = 5000.00
            
        if item == 'boat':
            itemPrice = 8000.00
            
        return itemPrice
    @abstractmethod
    def calculateTax(self):
        pass
            
class californiaSale(sale):
    def calculateTax(self):
        total = self.price() * .0725 + self.price()
        print('Your total today in California with tax is: {}'.format(total))

CAcost = californiaSale()
CAcost.price()
CAcost.calculateTax()


class massachusettsSale(sale):
    def calculateTax(self):
        total = self.price() * .0625 + self.price()
        print('Your total including tax in Massachusetts is: {}'.format(total))

MAcost = massachusettsSale()
MAcost.price()
MAcost.calculateTax()









    
