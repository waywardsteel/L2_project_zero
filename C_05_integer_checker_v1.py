# Functions go here
def num_check(question, num_type, exit_code=None):
    """Checks that user enters an integer / float that is more than zero (or the optional exit code) """


    if num_type == "integer":
        error = "Oops - please enter an integer more than zero"
        change_to = int
    else:
        error = "Oops - please enter an integer more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        #Check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

#Loop for testing purposes
while True:
    my_float = num_check("Please enter a number more than zero: ", "float")
    print(f"Thanks you chose {my_float}")
    my_int = num_check("please enter an integer more than zero: ","integer", "")

    if my_int == "":
        print("You have chosen infinite mode ")
    else:
        print(f"Thanks you have chose {my_int}")
