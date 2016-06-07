    # data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    # you code

    pass


# print the default table of records from the file
def show_table(table):
    table = data_manager.get_table_from_file(table)
    table_str = ""
    for item in range(len(table)):
        table_str += str(table[item]) + ("\n")
    return table_str
    # your code


# Ask a new record as an input from the user than add it to @table, than return @table


def add(table):
    table = data_manager.get_table_from_file(table)
    record = ui.get_inputs(["name: ", "producer: ", "year: ", "number of pieces: "], " ")
    record.insert(0, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file("tools.csv", table)

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table


def remove(table, id_):
    table = data_manager.get_table_from_file(table)
    for item in range(len(table)):
        list_in_list = table[item]
        if id_ in list_in_list:
            table.pop(item)  # delete element of a table
    data_manager.write_table_to_file("tools.csv", table)

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    table = data_manager.get_table_from_file(table)
    for item in range(len(table)):
        list_in_list = table[item]
        if id_ in list_in_list:
            record = ui.get_inputs(["name: ", "producer: ", "year: ", "number of pieces: "], " ")

    data_manager.write_table_to_file("tools.csv", table)

    # your code

    return table


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
