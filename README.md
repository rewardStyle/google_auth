# google_auth
A Python3 library for handling Google authentication for services such as Google Drive and Google Docs

## Required configuration

In order to authenticate with Google API services ( such as Google Drive ),
this module requires a valid `client_secret.json` file in the working directory
of the application using the module.

This file can be obtained from devops@rewardstyle.com and will resemble this:

```
{"installed":{"client_id":"xxxxx.apps.googleusercontent.com","project_id":"carbon-inkwell-194003","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"xxxxx","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
```

## Use Cases

This module is intended to serve as a universal means of authenticating
with Google services such as Google Drive and Google Sheets.

It is probably best used as a submodule within other libraries
that are purpose-built for accessing those Google services.

### Usage

In a module which needs to authenticate with Google:

```python
import httplib2
from google_auth import get_credentials

credentials = get_credentials('myUniqueAppName')
http = credentials.authorize(httplib2.Http())
```

If no valid credentials have been stored, then the module will
complete the OAuth2 flow ( with Google ) in order to obtain
new credentials ( stored locally as `client_credentials.json` ).

### Scopes

- Scopes  are defined at https://developers.google.com/identity/protocols/googlescopes
- Scopes are space separated
- If modifying the module's scopes, delete the previously saved credentials at `client_credentials.json`

## The WHYs

### Why was this module developed ?

Authenticating ( and subsequently using ) Google services
can be somewhat arcane, at least from within Python
applications.

This module was developed to make authentication as
simple as possible.

### Why use OAuth2?
( AKA, "Why not use simple token authentication?" )

Using Google API keys are only usable for accessing _public_ resources in Google.
Accessing _private_ resources ( Sheets, Docs, etc. ) requires OAuth2.

**Important Note**: Authenticating via OAuth2 from scratch requires manual intervention the first time.

### Reference
https://developers.google.com/sheets/api/quickstart/python
