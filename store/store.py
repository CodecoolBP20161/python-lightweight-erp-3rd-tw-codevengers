# data structure:
# id: string
# Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    while True:
        table = data_manager.get_table_from_file(current_file_path + "/games.csv")
        list_options = ["Show Table", "Add to table", "Remove from table", "Update table"]
        ui.print_menu("Sellings menu", list_options, "Exit to main menu")
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
            id_ = ui.get_inputs(["Please enter an ID: "], "")[0]
            update(table, id_)
        elif option == 5:
            get_lowest_price_item_id(table)
        elif option == 6:
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif option == 0:
            break
        else:
            raise KeyError("There is no such option.")
        data_manager.write_table_to_file(current_file_path + "/games.csv", table)


# print the default table of records from the file
def show_table(table):
    ui.print_table(table, ['ID', 'title', 'manufacturer', 'price', 'in_stock'])


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    record = ui.get_inputs(["title: ", "manufacturer: ", "price: ", "in_stock: "], " ")
    record.insert(0, common.generate_random(table))
    table.append(record)
    common.lists_in_list_to_str(table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for item in range(len(table)):
        if table[item][0] == id_:
            del table[item]
            return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    for item in range(len(table)):
        list_in_list = table[item]
        if id_ == list_in_list[0]:
            record = ui.get_inputs(["title: ", "manufacturer: ", "price: ", "in_stock: "], " ")
            record.insert(0, id_)
            table[item] = record
            common.lists_in_list_to_str(table)
            return table


# special functions:
# ------------------
# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number

def get_average_by_manufacturer(table, manufacturer):

    pass
