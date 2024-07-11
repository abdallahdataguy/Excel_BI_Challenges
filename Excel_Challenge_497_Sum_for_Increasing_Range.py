# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7217014764516831234-HJwa/

# Read the data range
df = xl("A1:A100", headers=True)

# Perform data wrangling
df['Cells'] = float('nan')
serial = 0
start = 0
while start < len(df.index):
    start = serial * (serial + 1) // 2
    end = (serial + 1) * (serial + 2) // 2
    df.iloc[start:end, 1] = serial + 1
    serial += 1

largest = df['Cells'].max()
df['Cells'] = df['Cells'].where(df['Cells'] < largest, 'Remaining')
df = df.groupby('Cells')['Numbers'].sum().reset_index()
df = df.rename(columns={'Numbers': 'Sum'})

# Display the final results
df
