#from quickstart.py on gmail api documentation
#input a string with a gmail user account
#output returns a List named labels which contains all the labels in that account

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def getLabels(account):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None


    ### CREATE A TOKEN NAME WHICH INCLUDES THE ACCOUNT,
    ### MAKES MULTIPLE TOKENS SO I CAN SWITCH ACCOUNTS WITHOUT DELETING
    token_account = account.replace("@", "AT")
    token_account = token_account.replace(".", "DOT")
    token = 'token_getLabels+'+token_account+'.json'
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId=account).execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return

        return labels #THIS IS THE ONE CHANGE BY ME - TW 2022-11-26 HAPPY THANKSGIVING ON SATURDAY

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
