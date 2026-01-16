# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import pandas as pd
# import matplotlib.pyplot as plt

# # Google Sheets URL
# url = "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?usp=sharing"

# # Connect to Google Sheets
# conn = st.connection("gsheets", type=GSheetsConnection)

# # Read data from Google Sheets
# data = conn.read(spreadsheet=url, usecols=[2, 3, 4, 5, 6, 7])  # 'Travel Date' is in column 5 (index 4)

# # Input for date search using a date picker
# date_input = st.date_input("Select a Travel Date:")

# # Enhanced CSS to style the card
# def card_style():
#     st.markdown(""" 
#         <style>
#         .card {
#             background: linear-gradient(135deg, #f0f0f0 0%, #ffffff 100%);
#             padding: 20px;
#             margin: 15px 0;
#             border-radius: 15px;
#             box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
#             transition: transform 0.2s ease;
#         }
#         .card:hover {
#             transform: scale(1.02);
#         }
#         .card h4 {
#             font-family: 'Arial', sans-serif;
#             font-weight: bold;
#             color: #333;
#         }
#         .card p {
#             margin: 5px 0;
#             color: #555;
#             font-family: 'Arial', sans-serif;
#         }
#         .card strong {
#             color: #2c3e50;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# # Function to handle NaN values
# def handle_nan(value):
#     return "Nil" if pd.isna(value) else value

# # Function to categorize time into intervals
# def categorize_time(time_str):
#     # Convert to datetime and extract hour
#     try:
#         time = pd.to_datetime(time_str)
#         return f"{time.hour}PM - {time.hour + 1}PM" if time.hour < 12 else f"{time.hour - 12}PM - {time.hour - 11}PM", time.hour
#     except Exception:
#         return "Invalid Time", 0  # Default hour for invalid time

# # Search button
# if st.button("Search"):
#     try:
#         # Convert 'Travel Date' column to datetime
#         data['Travel Date'] = pd.to_datetime(data['Travel Date'], errors='coerce')
        
#         # Filter the data based on the selected date
#         filtered_data = data[data['Travel Date'] == pd.to_datetime(date_input)]

#         # Remove 'Travel Date' column from the displayed results
#         if not filtered_data.empty:
#             filtered_data = filtered_data.drop(columns=['Travel Date'])
            
#             # Apply card styling
#             card_style()

#             # Get total number of results
#             total_results = len(filtered_data)
            
#             # Display each row in a card format
#             count = 1 
#             for index, row in filtered_data.iterrows():
#                 with st.container():
#                     st.markdown(f"""
#                         <div class="card">
#                             <h4>Person {count} of {total_results}</h4>
#                             <p><strong>👤 Name:</strong> {handle_nan(row[0])}</p>
#                             <p><strong>📞 Contact:</strong> {handle_nan(row[1])}</p>
#                             <p><strong>⏰ Travel Time:</strong> {handle_nan(row[2])}</p>
#                             <p><strong>📍 Destination :</strong> {handle_nan(row[3])}</p>
#                             <p><strong>📱 Message:</strong> {handle_nan(row[4])}</p>
#                         </div>
#                     """, unsafe_allow_html=True)
#                     count += 1
            
#             # Create a pie chart for Travel Time distribution with intervals
#             plt.figure(figsize=(8, 4))
#             filtered_data['Travel Time Interval'], filtered_data['Hour'] = zip(*filtered_data[filtered_data.columns[2]].apply(categorize_time))
#             time_distribution = filtered_data['Travel Time Interval'].value_counts()

#             # Sort the time_distribution based on the hour
#             sorted_intervals = sorted(time_distribution.index, key=lambda x: int(x.split('PM')[0].strip()))
#             sorted_distribution = time_distribution.reindex(sorted_intervals)

#             # Reverse the order for clockwise display and set startangle to 90
#             plt.pie(sorted_distribution[::-1], labels=sorted_distribution.index[::-1], autopct=lambda p: f'{p:.1f}%', startangle=90, textprops={'fontsize': 10})
#             plt.title('Distribution of Travel Times')
#             st.pyplot(plt)

#             # Create a pie chart for Destination distribution
#             plt.figure(figsize=(8, 4))
#             destination_distribution = filtered_data[filtered_data.columns[3]].apply(handle_nan).value_counts()  # Adjust index if necessary
#             plt.pie(destination_distribution, labels=destination_distribution.index, autopct=lambda p: f'{p:.1f}%', startangle=90, textprops={'fontsize': 10})
#             plt.title('Distribution of Starting Point')
#             st.pyplot(plt)
#         else:
#             st.write("Sorry , No data found for the selected Travel Date.")
#     except Exception as e:
#         st.write(f"Error occurred: {e}")



# st.balloons()  # A fun touch!






import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
from utils import handle_nan, categorize_time

# Google Sheets URL
url = "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?usp=sharing"

# Function to fetch real-time data (disable caching)
def fetch_data():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn.read(spreadsheet=url, usecols=[2, 3, 4, 5, 6, 7])  # 'Travel Date' is in column 5 (index 4)

# Input for date search using a date picker
date_input = st.date_input("Select a Travel Date:")

# Enhanced CSS to style the card
def card_style():
    st.markdown(""" 
        <style>
        .card {
            background: linear-gradient(135deg, #f0f0f0 0%, #ffffff 100%);
            padding: 20px;
            margin: 15px 0;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
        }
        .card:hover {
            transform: scale(1.02);
        }
        .card h4 {
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            color: #333;
        }
        .card p {
            margin: 5px 0;
            color: #555;
            font-family: 'Arial', sans-serif;
        }
        .card strong {
            color: #2c3e50;
        }
        </style>
    """, unsafe_allow_html=True)

# Utility functions are imported from utils.py

# Search button
if st.button("Search"):
    try:
        # Clear cache to ensure we fetch fresh data
        st.cache_data.clear()

        # Fetch data every time the button is clicked (Disabling caching here)
        data = fetch_data()

        # Convert 'Travel Date' column to datetime
        data['Travel Date'] = pd.to_datetime(data['Travel Date'], errors='coerce')

        # Filter the data based on the selected date
        filtered_data = data[data['Travel Date'] == pd.to_datetime(date_input)]

        # Remove 'Travel Date' column from the displayed results
        if not filtered_data.empty:
            filtered_data = filtered_data.drop(columns=['Travel Date'])

            # Apply card styling
            card_style()

            # Get total number of results
            total_results = len(filtered_data)

            # Display each row in a card format
            count = 1
            for index, row in filtered_data.iterrows():
                with st.container():
                    st.markdown(f"""
                        <div class="card">
                            <h4>Person {count} of {total_results}</h4>
                            <p><strong>👤 Name:</strong> {handle_nan(row[0])}</p>
                            <p><strong>📞 Contact:</strong> {handle_nan(row[1])}</p>
                            <p><strong>⏰ Travel Time:</strong> {handle_nan(row[2])}</p>
                            <p><strong>📍 Destination :</strong> {handle_nan(row[3])}</p>
                            <p><strong>📱 Message:</strong> {handle_nan(row[4])}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    count += 1

            # Create a pie chart for Travel Time distribution with intervals
            plt.figure(figsize=(8, 4))
            filtered_data['Travel Time Interval'], filtered_data['Hour'] = zip(*filtered_data[filtered_data.columns[2]].apply(categorize_time))
            time_distribution = filtered_data['Travel Time Interval'].value_counts()

            # Sort the time_distribution based on the hour
            sorted_intervals = sorted(time_distribution.index, key=lambda x: int(x.split('PM')[0].strip()))
            sorted_distribution = time_distribution.reindex(sorted_intervals)

            # Reverse the order for clockwise display and set startangle to 90
            plt.pie(sorted_distribution[::-1], labels=sorted_distribution.index[::-1], autopct=lambda p: f'{p:.1f}%', startangle=90, textprops={'fontsize': 10})
            plt.title('Distribution of Travel Times')
            st.pyplot(plt)

            # Create a pie chart for Destination distribution
            plt.figure(figsize=(8, 4))
            destination_distribution = filtered_data[filtered_data.columns[3]].apply(handle_nan).value_counts()  # Adjust index if necessary
            plt.pie(destination_distribution, labels=destination_distribution.index, autopct=lambda p: f'{p:.1f}%', startangle=90, textprops={'fontsize': 10})
            plt.title('Distribution of Destination')
            st.pyplot(plt)
        else:
            st.write("Sorry , No data found for the selected Travel Date.")
    except Exception as e:
        st.write(f"Error occurred: {e}")

st.balloons()  # A fun touch!
