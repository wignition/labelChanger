#Built off of the gmail api quickstart at https://developers.google.com/gmail/api/quickstart/python - tw
#Input a list of gmail labels, the output from getLabels()
#program will ask for a search term
#Output will be a list of the labels including that search term

def labelSearch(labels):
    label_id = []
    label_name = []
    label_matrix = []
    searchTerm = input("Enter search term... ")
    for label in labels:
        if searchTerm.lower() in label["name"].lower():
            label_id.append(label["id"])
            label_name.append(label["name"])

    print(len(label_id), "search results for", '"'+searchTerm+'"')
    
#TODO refine_search - give user option to search again if the list of results
# is long (10-50), or "really long" (50+)

    for i in range(len(label_id)):
        label_matrix.append([label_name[i], label_id[i]])

#    return label_id, label_name
    return searchTerm, label_matrix
