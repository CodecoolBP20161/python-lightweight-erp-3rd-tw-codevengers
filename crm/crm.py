# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start_module():
    table = data_manager.get_table_from_file(current_file_path + "/customers.csv")
    # print(table)
    list_options = ["Show Table", "Add to table", "Remove from table", "Update table", "Longest name", "Subscribed customers"]
    ui.print_menu("CRM menu", list_options, "Exit to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        show_table(table)
    elif option == 2:
        add(table)
    elif option == 3:
        id_ = ui.get_inputs(["Please enter an ID: "], "")[0]
        remove(table, id_)
    elif option == 4:
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        update(table, id_)
    elif option == 5:
        get_longest_name_id(table)
    elif option == 6:
        get_subscribed_emails(table)
    elif option == 0:
        exit()
    else:
        raise KeyError("There is no such option.")
    data_manager.write_table_to_file(current_file_path + "/customers.csv", table)


# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ['ID', 'Name', 'Email', 'Subscribed'])

# print(show_table(data_manager.get_table_from_file('customers.csv')))


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    added_line = ui.get_inputs(['name: ', 'email: ', 'subscribed: '], '')
    added_line.insert(0, common.generate_random(table))
    table.append(added_line)
    for i in table:
        for element, l in enumerate(i):
            i[element] = str(l)
    data_manager.write_table_to_file(current_file_path + "/customers.csv", table)  # data manager writes this back to file in one line
    return table

# print(add(data_manager.get_table_from_file('customers.csv')))
# Remove the record having the id @id_ from the @list, than return @table


def remove(table, id_):
    for i, l in enumerate(table):
        if id_ == l[0]:
            del table[i]
    return table

# print(remove(data_manager.get_table_from_file('customers.csv'), ui.get_inputs(['please enter an ID: '], '')[0]))


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    for item in range(len(table)):
        list_in_list = table[item]
        if id_[0] == list_in_list[0]:
            record = ui.get_inputs(["Name: ", "Email: ", "Subscribed: "], " ")
            record.insert(0, id_[0])
            table[item] = record
            for i in table:
                for element, l in enumerate(i):
                    i[element] = str(l)
            return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
# def get_longest_name_id(table):
#     glist = csv.reader(inputfile, delimiter="\t")
#     name = []
#     titles.append([row[1] for row in table])
#     titles = [item for slist in titles for item in slist]
#     return max(len(x) for x in titles)


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass

start_module()
