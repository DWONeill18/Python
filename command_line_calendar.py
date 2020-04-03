# Command Line Calendar

"""
The user will be able to view, add, updte and delete events,
on the calendar using the command line
"""
from time import sleep, strftime
FIRST_NAME = "David"

calendar = {}
def welcome():
    print("Hello " + FIRST_NAME + "!")
    print("Calendar is starting..")
    sleep(1)
    print("The current date is: " + strftime("%A %B %d %Y") )
    #current = str(strftime("%H:%M:%S"))
    
    sleep(1)
    print("What would you like to do?")

def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete or X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            # for no objects in calendar
            if len(calendar.keys()) < 1:
                print("Calendar is empty")
            else:
                # print remainder of calendar
                print(calendar)
        elif user_choice == "U":
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update complete")
            print(calendar)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date(MM/DD/YYYY): ")
            # incorrect date
            if len(date) > 10 or (int(date[6:]) < int(strftime("%Y"))):
                print("Date entered invalid")
                try_again = input("Try again? Y for Yes, N for No: ")  
                try_again = try_again.upper()
                if try_again == "Y":
                    # sending back to beginning of the loop
                    continue
                else:
                    # exit the start(while) loop
                    start = False
            else:
                calendar[date] = event
                print("Added date successful")
                print(calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                 print("Calendar is empty")
            else:
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("Event was deleted successfully")
                        print(calendar)
        elif user_choice == "X":
            start = False
        else:
            print("Invalid input")
            start = False

start_calendar()
        
            
        


