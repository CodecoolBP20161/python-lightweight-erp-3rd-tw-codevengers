

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):

    # your code

    pass


# An example output:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# see the function call in main.py
def print_menu(title, list_options, exit_message):
    print(title)
    for i, options in enumerate(list_options):
        print("(%d) %s" % (i + 1, options))
    print("(0) %s" % exit_message)
    pass


# see the function call in main.py
def get_inputs(list_titles, title):
    record = []
    for titles in list_titles:
        record.append(input(titles))
    return record


# see the function call in main.py
def print_error_message(message):

    # your code

    pass
