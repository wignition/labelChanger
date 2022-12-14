def numerator(list_to_numerate):
    count = 0
    for item in list_to_numerate:
        count += 1
        item.insert(0,count)

    return list_to_numerate

