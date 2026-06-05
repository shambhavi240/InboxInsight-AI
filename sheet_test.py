import gspread
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",
    SCOPES
)

creds = flow.run_local_server(port=0)

print("Authenticated!")

gc = gspread.authorize(creds)

print("GSpread connected!")

sheet = gc.open_by_key(
    "1DnDzJlIe-uaeaMkT0e8m-YNXW7yPmWUQtXA_h0XpMng"
)


print("Sheet opened!")