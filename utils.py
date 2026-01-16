import pandas as pd

def handle_nan(value):
    """Returns 'Nil' if the value is NaN, otherwise returns the value."""
    return "Nil" if pd.isna(value) else value

def categorize_time(time_str):
    """Categorizes a time string into a 1-hour interval (e.g., '2PM - 3PM')."""
    try:
        time = pd.to_datetime(time_str)
        hour = time.hour
        if hour == 0:
            return "12AM - 1AM", 0
        elif hour < 12:
            return f"{hour}AM - {hour + 1}AM" if hour != 11 else "11AM - 12PM", hour
        elif hour == 12:
            return "12PM - 1PM", 12
        else:
            h = hour - 12
            return f"{h}PM - {h + 1}PM" if h != 11 else "11PM - 12AM", hour
    except Exception:
        return "Invalid Time", 0
