def not_blank(question):
    """Checks that a user response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


# main routine starts here
who = not_blank("please enter your name: ")
print(f"Hello {who}")