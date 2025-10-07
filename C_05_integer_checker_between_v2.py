# Functions go here
def int_check(question, low, high):
    """Checks that user enters an integer / float that is more than zero (or the optional exit code) """

    error = f"Oops - please enter an integer between {low} and {high}. "

    while True:
        response = input(question).lower()

        #Check for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

#Loop for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = int_check("choose a number: ", 1, 10)
    print(f"You chose {my_num}")