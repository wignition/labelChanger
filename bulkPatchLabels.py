#from https://developers.google.com/gmail/api/quickstart/python

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.labels']


def bulkPatchLabels(account, searchTerm, label_results):

    creds = None
    token = 'token_'+SCOPES[0].rsplit("/")[-1].replace(".","DOT")+account.replace("@", "AT").replace(".", "DOT")+'.json'

#check or create valid token
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(creds.to_json())

#get the new string that will replace the searchTerm
    searchTerm = input("Input the phrase you'd like to replace.\n")
    new = input("Input the new phrase that will replace the term you searched.\n")
    
#replace the searchstring with the newstring
    print("\nEnter Replace For Loop\n")
    for item in label_results:
        item[0] = item[0].replace(searchTerm,new)
        print(item)

    print("\nExit Replace For Loop\n")

#patch the lables
    try:
        print("\nEnter Patch For Loop\n")
        for item in label_results:
            label_obj = {"name": item[0], "id": item[1]}
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().labels().patch(userId=account,
                                                     id=item[1],
                                                     body=label_obj).execute()
            print("successfully updated", item[1], "to", new)

        return new, label_results

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

