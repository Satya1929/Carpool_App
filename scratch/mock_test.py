import pandas as pd
import datetime
import sys
import os
sys.path.append(os.getcwd())
from utils import handle_nan, categorize_time

# Mock data based on user's input
# Headers: Name, Contact, Date, Time, Destination, Message
data = pd.DataFrame([
    ["Satya", "Testing", "4/30/2026", "3:00:00 AM", "MGR station", "Testing"]
], columns=["Name", "Contact", "Travel Date", "Travel Time", "Destination", "Message"])

print("Original Data:")
print(data)

# Simulate app logic
date_input = datetime.date(2026, 4, 30)
data['Travel Date'] = pd.to_datetime(data['Travel Date'], errors='coerce')
filtered_data = data[data['Travel Date'] == pd.to_datetime(date_input)]

print("\nFiltered Data (Before Drop):")
print(filtered_data)

if not filtered_data.empty:
    # Drop Travel Date
    filtered_data = filtered_data.drop(columns=['Travel Date'])
    print("\nFiltered Data (After Drop):")
    print(filtered_data)
    
    # Display logic simulation
    for index, row in filtered_data.iterrows():
        print(f"\nPerson 1:")
        # Use .iloc as in my fix
        print(f"Name: {handle_nan(row.iloc[0])}")
        print(f"Contact: {handle_nan(row.iloc[1])}")
        print(f"Travel Time: {handle_nan(row.iloc[2])}")
        print(f"Destination: {handle_nan(row.iloc[3])}")
        print(f"Message: {handle_nan(row.iloc[4])}")

    # Chart logic simulation
    # filtered_data.columns[2] should be Travel Time
    print(f"\nColumn at index 2: {filtered_data.columns[2]}")
    
    filtered_data['Travel Time Interval'], filtered_data['Hour'] = zip(*filtered_data[filtered_data.columns[2]].apply(categorize_time))
    print("\nWith Time Intervals:")
    print(filtered_data[['Travel Time Interval', 'Hour']])
    
    time_distribution = filtered_data['Travel Time Interval'].value_counts()
    
    # Sorting logic simulation
    hour_mapping = dict(zip(filtered_data['Travel Time Interval'], filtered_data['Hour']))
    sorted_intervals = sorted(time_distribution.index, key=lambda x: hour_mapping.get(x, 0))
    print(f"\nSorted Intervals: {sorted_intervals}")
else:
    print("\nNo data found.")
