# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    table = data_manager.get_table_from_file("items.csv")
    list_options = ["Show Table", "Add to table", "Remove from table", "Update table", "Highest profit", "Average profit"]
    ui.print_menu("Accounting menu", list_options, "Exit to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        show_table(table)
    elif option == 2:
        add(table)
    elif option == 3:
        # id_ = ui.get_inputs(["Please enter an ID: "], "")
        remove(table, ui.get_inputs(["Please enter an ID: "], ""))
    elif option == 4:
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        update(table, id_)
    elif option == 5:
        which_year_max(table)
    elif option == 6:
        year = ui.get_inputs(["Please enter a year: "], "")
        avg_amount(table, xear)
    elif option == 0:
        exit()
    else:
        raise KeyError("There is no such option.")
    data_manager.write_table_to_file("items.csv", table)
    pass


# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount'])
    pass

# print(show_table(data_manager.get_table_from_file('items.csv')))


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    added_line = ui.get_inputs(['month: ', 'number: ', 'day: ', 'year: ', 'type: ', 'amount: '], '')
    added_line.insert(0, common.generate_random(table))
    table.append(added_line)
    for i in table:
        for element, l in enumerate(i):
            i[element] = str(l)
    data_manager.write_table_to_file('items.csv', table)  # data manager writes this back to file in one line
    return table

# print(add(data_manager.get_table_from_file('items.csv')))


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for item in range(len(table)):
        list_in_list = table[item]
        if id_ in list_in_list:
            table.pop(item)
    return table

# print(remove(data_manager.get_table_from_file('items.csv'), ui.get_inputs(['please enter an ID: '], '')[0]))


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass

start_module()
