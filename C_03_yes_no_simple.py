# functions go here
def yes_no(question):
    """Checks that user enters yes / y or n / no to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please print yes (y) or no (n)")


# main routine goes here

# looping
while True:
    want_instructions = yes_no("Do you want the instructions? ")
    print(f"You chose {want_instructions}\n")