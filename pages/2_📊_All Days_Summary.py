# # Diwali (Back to home)
# # google sheet - column g name is "Destination"
# # google sheet - column f name is "Travel Time (Leaving from campus , Not train/plane time)"

# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import pandas as pd
# import matplotlib.pyplot as plt

# # Google Sheets URL
# url = "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?usp=sharing"

# # Connect to Google Sheets
# conn = st.connection("gsheets", type=GSheetsConnection)

# # Read data from Google Sheets
# data = conn.read(spreadsheet=url, usecols=[2, 4, 6])  

# # Convert 'Travel Date' to datetime format
# data['Travel Date'] = pd.to_datetime(data['Travel Date'], errors='coerce')

# # Format 'Travel Date' to 'dd-mm-yyyy'
# data['Travel Date'] = data['Travel Date'].dt.strftime('%d-%m-%Y')

# # Summary of total persons for each date
# summary_dates = data['Travel Date'].value_counts()

# # # Summary of total persons for each destination
# # destinations_column_name = 'Destination'  # Adjust this based on the actual column name in your data
# # summary_destinations = data[destinations_column_name].value_counts() if destinations_column_name in data.columns else None

# # Create Pie Chart for Travel Dates
# plt.figure(figsize=(10, 6))
# plt.pie(summary_dates, labels=summary_dates.index, autopct='%1.1f%%', startangle=140)
# plt.title('Summary of Total Persons for Each Travel Date')
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
# st.pyplot(plt)  # Use Streamlit to display the plot
# plt.clf()  # Clear the figure for the next plot

# # Create Pie Chart for Destinations if available
# if summary_destinations is not None:
#     plt.figure(figsize=(10, 6))
#     plt.pie(summary_destinations, labels=summary_destinations.index, autopct='%1.1f%%', startangle=140)
#     plt.title('Summary of Total Persons for Each Destination')
#     plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
#     st.pyplot(plt)  # Use Streamlit to display the plot
# else:
#     st.error(f"The column '{destinations_column_name}' was not found in the data.")








# Diwali (Back to college)
# google sheet - column g name is "Starting Location"
# google sheet - column f name is "Travel Time (Leaving from Starting Point , Not train/plane time)"

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt

# Google Sheets URL
url = "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?usp=sharing"

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from Google Sheets
data = conn.read(spreadsheet=url, usecols=[2, 4, 6])  

# Convert 'Travel Date' to datetime format
data['Travel Date'] = pd.to_datetime(data['Travel Date'], errors='coerce')

# Format 'Travel Date' to 'dd-mm-yyyy'
data['Travel Date'] = data['Travel Date'].dt.strftime('%d-%m-%Y')

# Summary of total persons for each date
summary_dates = data['Travel Date'].value_counts()

# Summary of total persons for each destination
destinations_column_name = 'Starting Location'  # Adjust this based on the actual column name in your data
summary_destinations = data[destinations_column_name].value_counts() if destinations_column_name in data.columns else None

# Create Pie Chart for Travel Dates
plt.figure(figsize=(10, 6))
plt.pie(summary_dates, labels=summary_dates.index, autopct='%1.1f%%', startangle=140)
plt.title('Summary of Total Persons for Each Travel Date')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
st.pyplot(plt)  # Use Streamlit to display the plot
plt.clf()  # Clear the figure for the next plot

# Create Pie Chart for Destinations if available
if summary_destinations is not None:
    plt.figure(figsize=(10, 6))
    plt.pie(summary_destinations, labels=summary_destinations.index, autopct='%1.1f%%', startangle=140)
    plt.title('Summary of Total Persons for Each Starting Location')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    st.pyplot(plt)  # Use Streamlit to display the plot
else:
    st.error(f"The column '{destinations_column_name}' was not found in the data.")
