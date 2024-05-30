# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7201794455467659266-fnlj/

import pandas as pd
from datetime import datetime, time, timedelta

# Function to generate time intervals
def time_intervals(start_time, end_time, interval=15):
    start_date = datetime(1900, 1, 1)  # Arbitrary date
    start_time = datetime.combine(start_date, start_time)
    end_time = datetime.combine(start_date, end_time)
    times = []
    current_datetime = start_time
    while current_datetime <= end_time:
        times.append(current_datetime.time())
        current_datetime += timedelta(minutes=interval)
    return times

# Read the Excel file
file_path = 'Excel_Challenge_467 - Overlapping Times.xlsx'
df = pd.read_excel(file_path, usecols='A:C', nrows=7)

# Perform data wrangling
df = df.set_index('Task ID', drop=True)
items = []
for i in df.index:
    item = [i]
    for j in df.index:
        a, b = df.loc[i, 'From Time':], df.loc[j, 'From Time':]
        if i == j:
            item.append('')
        else:
            intersect = any([x in time_intervals(*b) for x in time_intervals(*a)])
            item.append('Y' if intersect else '')
    items.append(item)
    
df = pd.DataFrame(items, columns=[''] + list(df.index))   

# Display the final results
df
