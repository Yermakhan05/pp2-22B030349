import os
from datetime import datetime

# Read the CSV file into a pandas dataframe
df = os.read_csv("scrubbed.csv")

# Identify which columns contain date and time information
datetime_cols = []
for col in df.columns:
    if 'date' in col.lower() or 'time' in col.lower():
        datetime_cols.append(col)

# Loop through each row in the identified columns and update the format
for col in datetime_cols:
    df[col] = os.to_datetime(df[col], errors='coerce')
    df[col] = df[col].dt.strftime('%B %d of %Y at %I:%M %p')

# Save the updated data to a new CSV file
df.to_csv("format_scrubbed.csv", index=False)
