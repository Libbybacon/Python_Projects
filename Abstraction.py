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
            print('A new car costs $5,000 before tax')
        if item == 'boat':
            itemPrice = 8000.00
            print('A new boat costs $8,000 before tax')
        
    @abstractmethod
    def calculateTax(self, tax):
        pass
            
class californiaSale(sale):
    def calculateTax(self, tax):
        total = itemPrice * tax
        print('Your total today with tax is: {}'.format(total))

CAcost = californiaSale()
CAcost.price()
CAcost.calculateTax(7.25)









    
