# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
from datetime import date
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
    table = data_manager.get_table_from_file(current_file_path + "/tools.csv")
    list_options = ["Show Table", "Add to table", "Remove from table", "Update table"]
    ui.print_menu("Tool manager menu", list_options, "Exit to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == 1:
        show_table(table)
    elif option == 2:
        add(table)
    elif option == 3:
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        remove(table, id_)
    elif option == 4:
        id_ = ui.get_inputs(["Please enter an ID: "], "")
        update(table, id_)
    elif option == 5:
        get_lowest_price_item_id(table)
    elif option == 6:
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == 0:
        exit()
    else:
        raise KeyError("There is no such option.")
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)


# print the default table of records from the file

def show_table(table):
    ui.print_table(table, ['ID', 'Name', 'Producer', 'Year', 'Durability'])

#  Ask a new record as an input from the user than add it to @table, than return @table


def add(table):
    record = ui.get_inputs(["Name: ", "Producer: ", "Year: ", "Durability: "], " ")
    record.insert(0, common.generate_random(table))
    table.append(record)
    for i in table:
        for element, l in enumerate(i):
            i[element] = str(l)
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table


def remove(table, id_):
    for item in range(len(table)):
        if table[item][0] == id_[0]:
            del table[item]
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table


def update(table, id_):
    table = data_manager.get_table_from_file(table)
    for item in range(len(table)):
        list_in_list = table[item]
        if id_ in list_in_list:
            record = ui.get_inputs(["Name: ", "Producer: ", "year: ", "durability: "], " ")
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table

start_module()
# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)


def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
def get_average_durability_by_manufacturers(table):

    # your code

    pass
