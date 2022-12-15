#def labelChanger():
"""Calls labelSearch(), then asks if you'd like to change the label"""

from inputAccount import inputAccount
from getLabels import getLabels
from labelSearch import labelSearch
from numerator import numerator
from resultSelector import resultSelector
from updateLabels import updateLabels
from patchLabels import patchLabels
from bulkPatchLabels import bulkPatchLabels

#gets input account
account = inputAccount()

#loads all labels from input account using gmail quickstart.py
#Set the name of the token file unique to the user so
# multiple users can use the program without need to delete
# the token

labels = getLabels(account)

#search "labels" and return the label id and label name
searchTerm, label_results = labelSearch(labels)
print(label_results)
#TODO - give user option to search again if the list of results
# is long (10-50), or "really long" (50+)

#select to update single selected label, or all (FUTURE: select-by-comma-separated-numbers())
select_version = input("\nselect the version\n1 - update individual label\n2 - update all labels")
print("run the", select_version)

#numerate the results
label_results = numerator(label_results)

#select the filtered result
selected_result, name, ID = resultSelector(label_results)
 
#update the selected label
patchLabels(account, ID)

#update all the labels in label_results
bulkPatchLabels(account, searchTerm, label_results)
