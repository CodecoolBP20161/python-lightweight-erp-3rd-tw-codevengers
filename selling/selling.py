# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
# main module
# main = SourceFileLoader("main", current_file_path + "/../main.py").load_module()


# start this manager by a menu
def start_module():
    while True:
        table = data_manager.get_table_from_file(current_file_path + "/sellings.csv")
        list_options = ["Show Table",
                        "Add to table",
                        "Remove from table",
                        "Update table",
                        "Lowest price ID",
                        "Sold in a period"]
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
            lowest_price_ID = get_lowest_price_item_id(table)
            ui.print_table([[lowest_price_ID]], ["Lowest price"])
        elif option == 6:
            list_titles = ["Start month: ", "Start day: ", "Start year: ", "End month:  ", "End day: ", "End year: "]
            dates = ui.get_inputs(list_titles, "")
            filtered_table = get_items_sold_between(table, dates[0], dates[1], dates[2], dates[3], dates[4], dates[5])
            show_table(filtered_table)
        elif option == 0:
            break
        else:
            raise KeyError("There is no such option.")
        data_manager.write_table_to_file(current_file_path + "/sellings.csv", table)


# print the default table of records from the file
def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    list_titles = ["Game name?: ", "Game price?: ", "Month?: ", "Day?:", "Year?:"]
    add_records = ui.get_inputs(list_titles, "")
    add_records.insert(0, common.generate_random(table))
    table.append(add_records)
    common.lists_in_list_to_str(table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for i, l in enumerate(table):
        if id_ == l[0]:
            del table[i]
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    remove(table, id_)
    list_titles = ["Game name?: ", "Game price?: ", "Month?: ", "Day?:", "Year?:"]
    add_records = ui.get_inputs(list_titles, "")
    add_records.insert(0, id_)
    table.append(add_records)
    common.lists_in_list_to_str(table)
    return table


# special functions:
# ------------------


# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    prices = []
    for line in table:
        prices.append(line[2])
    lowest_price = min(prices)
    for i in range(len(prices)):
        if prices[i] == lowest_price:
            return table[i][0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    filtered_table = []
    for i in table:
        for l in range(3, len(i)):
            i[l] = int(i[l])
    for i, element in enumerate(table):
        if element[-1] > year_from and element[-1] < year_to:
            filtered_table.append(element)
        elif element[-1] == year_from:
            if element[-3] > month_from:
                filtered_table.append(element)
            elif element[-3] == month_from:
                if element[-2] > day_from:
                    filtered_table.append(element)
        elif element[-1] == year_to:
            if element[-3] < month_to:
                filtered_table.append(element)
            elif element[-3] == month_to:
                if element[-2] < day_to:
                    filtered_table.append(element)
    common.lists_in_list_to_str(table)
    return filtered_table
