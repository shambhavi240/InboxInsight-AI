print("STEP 1")

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",
    SCOPES
)

print("STEP 2")

creds = flow.run_local_server(port=0)

print("STEP 3")

gmail_service = build("gmail", "v1", credentials=creds)

print("STEP 4")

results = gmail_service.users().messages().list(
    userId="me",
    maxResults=5
).execute()

print("STEP 5")

messages = results.get("messages", [])

for msg in messages:
    message = gmail_service.users().messages().get(
        userId="me",
        id=msg["id"]
    ).execute()

    headers = message["payload"]["headers"]

    for header in headers:
        if header["name"] == "Subject":
            print(header["value"])