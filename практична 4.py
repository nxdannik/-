def r_duplicate(*a):
    list(a)
    element = []
    for item in a:
        if item in element:
            pass
        elif type(item) == str:
            for letters in item:
                if letters in element:
                    pass
                else:
                    element.append(letters)
        else:
            element.append(item)
    return element


def sortingg(sorting_element):
    number = []
    strings = []
    for item in sorting_element:
        if type(item) == int or type(item) == float:
            number.append(item)
        elif type(item) == str:
            strings.append(item)
    number.sort()
    strings.sort()
    return number + strings


uniq_list_element = (r_duplicate(3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Паралелепіпед', 'Случик'))
uniq_list_element_sort = (sortingg(uniq_list_element))
print(f'uniq list {uniq_list_element} \n\n sort_uniq_list {uniq_list_element_sort} ')