import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Function to fetch data from Google Sheets using API
def fetch_data_from_google_sheet(sheet_id, range_name):
    # Load the service account key
    creds = service_account.Credentials.from_service_account_file(
        "C:\\Users\\ASUS\\Desktop\\Carpool_App\\carpool-app-439312-f34c14940ecb.json",  # Update the path to your JSON file
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]  # Read-only access
    )

    # Build the service
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get('values', [])

    # Convert to DataFrame if there are values
    if values:
        return pd.DataFrame(values[1:], columns=values[0])  # First row as column names
    else:
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    # Replace with your actual Google Sheet ID and range (e.g., "Sheet1!A1:D")
    sheet_id = "1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk"
    range_name = "Form Responses 1!C:H"  # Adjust the range as needed

    # Fetch the data
    df = fetch_data_from_google_sheet(sheet_id, range_name)

    # Display the DataFrame
    print(df)
