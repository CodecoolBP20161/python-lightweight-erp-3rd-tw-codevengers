# implement commonly used functions here


# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):
    import random
    string_list = []
    not_unique = True
    while not_unique:
        option0, option1, option2, option3 = 0, 0, 0, 0
        while option0 < 2 or option1 < 2 or option2 < 2 or option3 < 2:
            option = random.randrange(4)
            if option == 0 and option0 < 2:
                string_list.append(chr(random.randrange(48, 58)))
                option0 += 1
            elif option == 1 and option1 < 2:
                string_list.append(chr(random.randrange(97, 123)))
                option1 += 1
            elif option == 2 and option2 < 2:
                string_list.append(chr(random.randrange(65, 91)))
                option2 += 1
            elif option == 3 and option3 < 2:
                string_list.append(chr(random.randrange(33, 45)))
                option3 += 1
        string = "".join(string_list)
        if string not in table:
            not_unique = False
    return(string)


def lists_in_list_to_str(list_to_convert):
    for lists in list_to_convert:
        for i, element in enumerate(lists):
            lists[i] = str(element)
    return list_to_convert
