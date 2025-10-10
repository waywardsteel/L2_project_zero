# Functions go here
def int_check(question):
    """Check users enter an integer"""

    error = "Oops - please enter an integer "

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main routine goes here

#Loop for testing purposes
while True:
    print()

    # Ask user for their name
    name = input("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} brought a ticket")