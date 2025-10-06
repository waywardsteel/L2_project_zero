# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """Checks that user enters full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            #Check if the response is the entire word
            if response == item:
                return item

            #Check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# Main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? ",
                           yes_no_list, 1)

print(f"You choose {like_coffee}")
pay_method = string_check("payment method: ", payment_list, 2)
print(f"You choose {pay_method}")