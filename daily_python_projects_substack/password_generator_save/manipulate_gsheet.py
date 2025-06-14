# quickstart.py - Your Reusable Toolbox

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_sheets_service() :
    """
    Handles authentication with Google and returns an authorized service object.
    Creates or refreshes 'token.json' as needed.

    Returns:
        Resource: An authorized Google Sheets API service object.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)


### --- YOUR 4 CORE TOOLBOX FUNCTIONS --- ###

def read_data(service, spreadsheet_id: str, range_name: str) -> list:
    """
    Reads data from a specified range in a sheet.

    Args:
        service (Resource): The authorized Google Sheets service object.
        spreadsheet_id (str): The ID of the spreadsheet to read from.
        range_name (str): The A1 notation of the range to read (e.g., 'Sheet1!A1:C5').

    Returns:
        List[List[Any]]: A list of lists representing the rows and cells of the read range.
                         Returns an empty list if no data is found.
    """
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])


def append_data(service, spreadsheet_id: str, range_name: str, data: list) -> dict:
    """
    Appends new rows to the end of a table in a sheet.

    Args:
        service (Resource): The authorized Google Sheets service object.
        spreadsheet_id (str): The ID of the spreadsheet.
        range_name (str): The A1 notation of a range indicating the table to append to.
                          E.g., 'Sheet1' or 'Sheet1!A1'. Google finds the last row automatically.
        data (List[List[Any]]): A list of rows to append. Each row is a list of cell values.
                                E.g., [['valueA1', 'valueB1'], ['valueA2', 'valueB2']]

    Returns:
        dict: The API response containing details about the update.
    """
    sheet = service.spreadsheets()
    body = {'values': data}
    result = sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='USER_ENTERED',
        body=body
    ).execute()
    print("Data successfully added to sheet.")
    return result


def modify_data(service, spreadsheet_id: str, range_name: str, data: list) -> dict:
    """
    Writes or overwrites data in a specific range of a sheet.

    Args:
        service (Resource): The authorized Google Sheets service object.
        spreadsheet_id (str): The ID of the spreadsheet.
        range_name (str): The A1 notation of the exact range to write to (e.g., 'Sheet1!B5').
        data (List[List[Any]]): A list of rows to write. Each row is a list of cell values.

    Returns:
        dict: The API response containing details about the update.
    """
    sheet = service.spreadsheets()
    body = {'values': data}
    result = sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='USER_ENTERED',
        body=body
    ).execute()
    return result


def delete_row(service, spreadsheet_id: str, sheet_gid: int, row_number: int) -> dict:
    """
    Deletes a specific row from a sheet, causing rows below to shift up.

    Args:
        service (Resource): The authorized Google Sheets service object.
        spreadsheet_id (str): The ID of the spreadsheet.
        sheet_gid (int): The numerical ID of the specific sheet (tab).
                         Find it in the URL as the 'gid' parameter (e.g., ...#gid=0).
        row_number (int): The 1-based number of the row to delete (e.g., row 5).

    Returns:
        dict: The API response.
    """
    sheet = service.spreadsheets()
    # Convert 1-based row number to 0-based index for the API
    start_index = row_number - 1
    end_index = row_number

    request_body = {
        'requests': [{
            'deleteDimension': {
                'range': {
                    'sheetId': sheet_gid,
                    'dimension': 'ROWS',
                    'startIndex': start_index,
                    'endIndex': end_index
                }
            }
        }]
    }
    result = sheet.batchUpdate(spreadsheetId=spreadsheet_id, body=request_body).execute()
    return result


# You can keep this block if you ever want to test this file directly

if __name__ == '__main__':
    print("This is a toolbox file. Import it in your main script.")
    print("Service object created successfully.")
    SPREADSHEET_ID: str = "1E7YogxyTbP4kENkD22nNk59xZBIzSe6tnh0jd2FxUhY"
    CELLS_RANGE: str = "Sheet1!A1:C"
    SERVICE = get_sheets_service()
    CURRENT_GSHEET_DATA: list = read_data(service=SERVICE, range_name=CELLS_RANGE,
                                          spreadsheet_id=SPREADSHEET_ID)
    data_to_add: list = [["2025-06-14", "Testos", "ultim_test"],
                         ["2025-06-14", "Testos", "ultim_test"],
                         ["2025-06-14", "Testos", "ultim_test"]]
    append_data(service=SERVICE, spreadsheet_id=SPREADSHEET_ID, range_name="Sheet1",data=data_to_add)