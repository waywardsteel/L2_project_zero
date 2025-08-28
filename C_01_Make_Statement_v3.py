#functions go here
def make_statement(statement, decoration, lines=1):
    """Creates heading (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 lines). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


#main routine goes here
make_statement("programming is fun", "=", 3)
print()
make_statement("programming is still fun", "*", 2)
print()
make_statement("emoji in action", "🐌")