import pandas as pd
import sys

try:
    s = pd.Series([10], index=['Name'])
    print(f"Accessing s[0]: {s[0]}")
except Exception as e:
    print(f"Error accessing s[0]: {type(e).__name__}: {e}")

try:
    raise KeyError(0)
except Exception as e:
    print(f"str(KeyError(0)): '{e}'")
