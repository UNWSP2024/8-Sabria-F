#By: Sabria Fafach
#Date: March 3, 2025
#Title: program_1.py

def initials_generator(personsName):

    personsInitials = ""
    for char in personsName:
        if char.isupper()==True:
            personsInitials+=char+"."

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name:')

initials = initials_generator(personsName)

print(initials)