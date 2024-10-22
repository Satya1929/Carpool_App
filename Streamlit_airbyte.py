
import json
import streamlit as st
import airbyte as ab

def _read_service_account_secret():
    with open("carpool-app-439312-f34c14940ecb.json") as f:
        return json.load(f)

st.title("Stocks Dashboard")

service_account = _read_service_account_secret()
st.json(service_account)

# google sheets connection and storing in server side cache for uncesseary calling and redownloads of the excel file
# for multiple usersession
@st.cache_resource
def connect_to_gsheets():
    s_acc = _read_service_account_secret()
    gsheets_connection = ab.get_source(
        "source-google-sheets",
        config={
            "spreadsheet_id": "1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk",
            # "spreadsheet_id": "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?gid=1935460621#gid=1935460621",
            # https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?gid=1935460621#gid=1935460621
            "credentials": {
                "auth_type": "Service",
                "service_account_info": json.dumps(s_acc), 
            }
        }
    )
    gsheets_connection.select_all_streams()
    return gsheets_connection

# @st.cache_data
# def download_data(_gsheets_connection):
#     airbyte_streams = _gsheets_connection.read()

#     ticker_df = airbyte_streams["ticker"].to_pandas()

#     history_dfs = {}

#     for ticker in list(ticker_df["ticker"]):
#         d = airbyte_streams[ticker].to_pandas()
#         history_dfs[ticker] = d

#     return ticker_df, history_dfs

st.title("Stocks Dashboard")
gsheets_connection = connect_to_gsheets()

# ticker_df, history_dfs = download_data(gsheets_connection)

# st.write(ticker_df)
# st.write(history_dfs)
