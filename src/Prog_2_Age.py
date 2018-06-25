__author__ = 'Shubhraj'

def age_program():
    option = input("1. Convert Age -> Seconds\n2. Convert Seconds -> Age\n")
    if option == '1':
        age = input("Enter age in Years: ")
        seconds = int(age) * 365 * 24 * 60 * 60
        print("Your age in seconds: {}".format(seconds))
    elif option == '2':
        seconds = input("Enter your age in Seconds: ")
        age = int(seconds)/(365 * 24 * 60 * 60)
        print("Your age in years: {}".format(age))
    else:
        print("Wrong option selected")

age_program()