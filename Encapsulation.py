# Create class that uses encapsulation with a private and a protected attribute
# Create object that uses protected and private attributes


# Create class User
class User:
    # Initialize User, set Phone to protected, and Password to private
    def __init__(self):
        self.Fname = 'Sarah'
        self.Lname = 'Butler'
        self._Phone = '000-000-0000'
        self.__Password = '!@#$%'

    def getInfo(self):
        print('First Name: {}, Last Name: {}, Phone: {}, Password: {}'.format(self.Fname, self.Lname, self._Phone, self.__Password))
        
    # Function to change private attribute Password
    def changePassword(self, private):
        self.__Password = private

# Create object info and use it to show user info and change password
Info = User()
Info.getInfo()
Info.changePassword('12345')
Info.getInfo()

if __name__ == "__main__":
    User()
