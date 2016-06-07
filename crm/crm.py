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
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()
common = SourceFileLoader("module.name", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start_module():

    # you code

    pass


# print the default table of records from the file
def show_table(table):
    t_temp = ""
    for item in range(len(table)):
        t_temp += str(table[item]) + ("\n")
    return t_temp
    pass

print(show_table(data_manager.get_table_from_file('customers.csv')))


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

# Remove the record having the id @id_ from the @list, than return @table

    return table

def remove(table, id_):

    # your code
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
