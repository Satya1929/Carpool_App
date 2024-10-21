import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

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

# Streamlit app
def main():
    st.title("Google Sheets Data Viewer")

    # Input for Sheet ID and Range
    sheet_id = st.text_input("Enter Google Sheet ID", "1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk")
    range_name = st.text_input("Enter Range (e.g., 'Form Responses 1!C:H')", "Form Responses 1!C:H")

    # Input for date
    date_input = st.text_input("Enter Date (mm-dd-yyyy)")

    if st.button("Fetch Data"):
        if sheet_id and range_name and date_input:
            # Fetch the data
            df = fetch_data_from_google_sheet(sheet_id, range_name)

            # Check if the DataFrame is not empty
            if not df.empty:
                # Convert the 'Date' column to datetime format for filtering
                df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%Y', errors='coerce')

                # Filter the DataFrame for the specified date
                filter_date = pd.to_datetime(date_input, format='%m-%d-%Y', errors='coerce')
                filtered_df = df[df['Date'] == filter_date]

                # Display the filtered DataFrame
                if not filtered_df.empty:
                    st.write("Data for the specified date:")
                    st.dataframe(filtered_df)
                else:
                    st.warning("No data found for the specified date.")
            else:
                st.warning("No data found in the specified range.")
        else:
            st.error("Please provide Sheet ID, Range, and Date.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
