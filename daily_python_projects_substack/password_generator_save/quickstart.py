import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# This scope allows for both reading and writing to Google Sheets.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# --- PASTE YOUR SPREADSHEET ID HERE ---
YOUR_SPREADSHEET_ID = "1E7YogxyTbP4kENkD22nNk59xZBIzSe6tnh0jd2FxUhY"


def main():
    """Shows basic usage of the Sheets API.
  Connects to a specific sheet, reads data, and appends new data.
  """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        # === EXAMPLE 1: READING DATA ===
        # Reads the first 10 rows from columns A and B of 'Sheet1'
        # Change 'Sheet1!A1:B10' to the sheet and range you want to read.
        read_range = "Sheet1!A1:B10"
        result = (
            sheet.values()
            .get(spreadsheetId=YOUR_SPREADSHEET_ID, range=read_range)
            .execute()
        )
        values = result.get("values", [])

        print("\n--- Reading Data ---")
        if not values:
            print("No data found.")
        else:
            print("First 10 rows:")
            for row in values:
                print(row)

        # === EXAMPLE 2: WRITING (APPENDING) DATA ===
        # This will add a new row to the end of your sheet.
        # The data to be added. For your 'passwords' sheet, this could be
        # [website, username, password]
        new_row_data = [
            ["example.com", "my_user", "pa$$w0rd123"]
        ]

        # The sheet and range where data should be appended.
        # 'A1' means it will find the first empty row in the table starting at A1.
        append_range = "Sheet1!A1"

        body = {"values": new_row_data}

        append_result = (
            sheet.values()
            .append(
                spreadsheetId=YOUR_SPREADSHEET_ID,
                range=append_range,
                valueInputOption="USER_ENTERED",  # This treats the data as if you typed it in the UI
                body=body,
            )
            .execute()
        )
        print("\n--- Writing Data ---")
        print(f"Appended new row. {(append_result.get('updates').get('updatedCells'))} cells updated.")


    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()