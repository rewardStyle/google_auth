from __future__ import print_function
import argparse
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


# https://developers.google.com/sheets/api/quickstart/python

# SCOPES are defined at https://developers.google.com/identity/protocols/googlescopes
# SCOPES are space separated
# If modifying these scopes, delete your previously saved credentials
# at CLIENT_CREDENTIALS_FILE
_SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file')
CLIENT_SECRET_FILE = 'client_secret.json'
CLIENT_CREDENTIALS_FILE = 'client_credentials.json'


def get_credentials(app_name, scopes=_SCOPES):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    scopes = ' '.join(list(scopes))
    clientfile = os.path.join(os.path.expanduser('.'), CLIENT_SECRET_FILE)
    credfile = os.path.join(os.path.expanduser('.'), CLIENT_CREDENTIALS_FILE)

    store = Storage(credfile)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(clientfile, scopes)
        flow.user_agent = app_name
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args(args=[])
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credfile)
    return credentials
