# Challenge:
# Create a script that will find out the current times in Portland, NYC and London branches
# Compare that time with each branch's hours (9am-5pm) to see if they are open or closed
# Print out to screen the three branches and whether they are open or closed



import datetime
import pytz

# Get branch time zones
portlandZone = pytz.timezone('US/Pacific')
nycZone = pytz.timezone('US/Eastern')
londonZone = pytz.timezone('Europe/London')

# Get current time in each time zone
# Then get current hour for each
# Then use range to determine if branch is open; print corresponding statement
def getTime():
    portlandNow = datetime.datetime.now(portlandZone)
    portlandHour = portlandNow.strftime('%H')
    print(portlandHour) # Printing the hour just so I can see it while I work on it
    if portlandHour in range(9,23):
        print("The Portland branch is open.")
    else:
        print("The portland branch is closed.")
    nycNow = datetime.datetime.now(nycZone)
    nycHour = nycNow.strftime('%H')
    print(nycHour)
    if nycHour in range(9, 17):
        print("The NYC branch is open.")
    else:
        print("The NYC branch is closed.")
   
    londonNow = datetime.datetime.now(londonZone)
    londonHour = londonNow.strftime('%H')
    print(londonHour)
    if londonHour in range(9,17):
        print("The London branch is open.")
    else:
        print("The London branch is closed.")
    

if __name__ == "__main__":
    getTime()


