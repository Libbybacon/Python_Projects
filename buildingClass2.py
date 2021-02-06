
# Parent class Building

class Building:
    # Define attributes:
    numberSides = 4
    numberLevels = 1
    architectureType = 'unknown'
    primaryUse = 'unknown'
    energyEfficient = True

    def getBuildingDetails(self):
        numberSides = input("How many sides does the building have?\n>>> ")
        numberLevels = input("How many levels are in the building?\n>>> ")
        architectureType = input("What is the architecture style of the building?\n>>> ")
        primaryUse = input("What is the primary use of the building?\n>>> ")
        return numberSides,numberLevels,architectureType,primaryUse

    def addLevel(self):
       moreLevels = input("How many levels would you like to add to the building?\n>>> ")
       numberLevels += moreLevels
       return numberLevels
       
        

# Child class House 
class Home(Building):
    homeType: 'unknown'
    age = 0
    hasGarage = True
    locationType = 'unknown'
    lastSaleValue = 0

        # Same method as parent class except it asks for homeType and locationType 
        # and not primaryUse
    def getBuildingDetails(self):
        numberSides = input("How many sides does the building have?\n>>> ")
        numberLevels = input("How many levels are in the building?\n>>> ")
        architectureType = input("What is the architecture style of the building?\n>>> ")
        homeType = input("Is this home a house, an apartment, or a condominium?\n>>> ")
        locationType = input("Is this home in a city, town, or rural area?\n>>> ")
        return numberSides,numberLevels,architectureType,homeType,locationType

    
# Child class Business    
class Business(Building):
    businessType = 'unkown'
    numberEmployees = 0
    totalAnnualProfits = 0
    squareFootage = 0

        # Same method as parent class except it asks for businessType and squareFootage 
        # and not primaryUse
    def getBuildingDetails(self):
        numberSides = input("How many sides does the building have?\n>>> ")
        numberLevels = input("How many levels are in the building?\n>>> ")
        architectureType = input("What is the architecture style of the building?\n>>> ")
        businessType = input("What type of business is in this building?\n>>> ")
        squareFootage = input("What is the square footage of the building?\n>>> ")
        return numberSides,numberLevels,architectureType,businessType,squareFootage

# Code to invoke getBuildingDetails method in each class


if __name__ == "__main__":
buildingOwner = Building()
buildingOwner.getBuildingDetails()

homeOwner = Home()
homeOwner.getBuildingDetails

businessOwner = Business()
businessOwner = getBuildingDetails()
