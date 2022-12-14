#adds ID return to resultSelector()
def resultSelector(label_results):

    selection = "No Selection Made."
    selected_result = []
    name = ""
    ID = ""

    if(len(label_results)) > 1:
        for item in label_results:
            print(item)

        selection = input("\nPlease enter the number of your selection:\n")
        for item in label_results:
            if item[0] == int(selection):
                selected_result.append([item[1], item[2]])
                name = item[1]
                ID = item[2]
                print(item[1], item[2])
    else:
        for item in label_results:
            selected_result.append([item[1], item[2]])
            name = item[1]
            ID = item[2]
            print(item[1], item[2])

    return selected_result, name, ID
