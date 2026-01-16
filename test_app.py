import pytest
import pandas as pd
from utils import handle_nan, categorize_time

def test_handle_nan_with_real_value():
    assert handle_nan("John Doe") == "John Doe"
    assert handle_nan(123) == 123

def test_handle_nan_with_nan():
    assert handle_nan(pd.NA) == "Nil"
    assert handle_nan(float('nan')) == "Nil"

def test_categorize_time_pm():
    interval, hour = categorize_time("2024-01-01 14:00:00")
    assert interval == "2PM - 3PM"
    assert hour == 14

def test_categorize_time_am():
    interval, hour = categorize_time("2024-01-01 09:00:00")
    assert interval == "9AM - 10AM"
    assert hour == 9

def test_categorize_time_noon():
    interval, hour = categorize_time("2024-01-01 12:00:00")
    assert interval == "12PM - 1PM"
    assert hour == 12

def test_categorize_time_midnight():
    interval, hour = categorize_time("2024-01-01 00:00:00")
    assert interval == "12AM - 1AM"
    assert hour == 0

def test_categorize_time_invalid():
    interval, hour = categorize_time("not a time")
    assert interval == "Invalid Time"
    assert hour == 0
