

class Boat:
    # Class attributes:
    length = 0
    name = ' '
    color = ' '
    maxSpeed = 0
    currentSpeed = 0

    # Define change speed method:
    def changeSpeed(self):
        newSpeed = input("Enter desired new speed: ")
        currentSpeed = newSpeed
            

# Child classes with attributes:

class sailBoat(Boat):
    numberSails = 0
    steeringMechanism = 'tiller'

class motorBoat(Boat):
    engineType = 'diesel'
    maxPassengers = 0
    
    
    
    
