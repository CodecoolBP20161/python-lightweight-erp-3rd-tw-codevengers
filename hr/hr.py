# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    title = "HR"
    exit_message = "Back to da future"
    list_options = ["Show the table",
                    "Add to table",
                    "Remove from table",
                    "Update the table",
                    "Get the oldest person(s)",
                    "Get the closest persons(s) to average",
                    "Back to the main menu"]
    while True:
        table = data_manager.get_table_from_file(current_file_path + "/persons.csv")
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["\nEnter a num: "], " ")
        user_input = int(inputs[0])
        if user_input == 1:
            show_table(table)
        elif user_input == 2:
            add(table)
        elif user_input == 3:
            id_ = ui.get_inputs(["Which ID do you want to remove? "], " ")
            remove(table, id_)
        elif user_input == 4:
            id_ = ui.get_inputs(["Which ID dou you want to update? "], " ")
            update(table, id_)
        elif user_input == 5:
            get_oldest_person(table)
        elif user_input == 6:
            get_persons_closest_to_average(table)
        elif user_input == 0:
            exit()
        else:
            raise KeyError("There is no such option.")
        data_manager.write_table_to_file(current_file_path + "/persons.csv", table)


# print the default table of records from the file
def show_table(table):
    title_list = ["ID", "Name", "Birth Date"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):



    return table


# Remove the record having the id @id_ from the @list, than return @table
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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass

start_module()
