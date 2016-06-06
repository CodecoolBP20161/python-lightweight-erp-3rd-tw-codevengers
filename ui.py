

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):
    max_len = []
    for i, title in enumerate(title_list):
        max_len.append(len(title))
        for games in table:
            if len(str(games[i])) > max_len[i]:
                max_len[i] = len(str(games[i]))
    for i, length in enumerate(max_len):
        if length % 2 == 0:
            max_len[i] = length + 3
        else:
            max_len[i] = length + 4
    for i, length in enumerate(max_len):
        print("|" + "-"*(length), end="")
    print("|\n")
    for i, length in enumerate(max_len):
        print("|".ljust(1) + title_list[i].center(int(((length)))), end="")
    print("|\n")
    for games in table:
        for i, length in enumerate(max_len):
            print("|" + "-"*(length), end="")
        print("|\n")
        for i, length in enumerate(max_len):
            print("|".ljust(1) + str(games[i]).center(int(((length)))), end="")
        print("|\n")
    for i, length in enumerate(max_len):
        print("|" + "-"*(length), end="")
    print("|\n")
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
    print(title + "\n")
    for titles in list_titles:
        try:
            record.append(int(input(titles)))
        except:
            record.append(input(titles))
    return record


# see the function call in main.py
def print_error_message(message):
    print(message)
    pass
