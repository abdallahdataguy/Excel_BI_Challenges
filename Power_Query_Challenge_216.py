# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7238395630518194176-u4rK/

# Read the data range
df = xl("A1:E6", headers=True)

# Perform data manipulation
columns = [
    'Items ' + c[0].replace('Item', '') + ' - ' + c[-1].replace('Item', '') 
    for i in df.index if (c:=[x for x in df.iloc[i] if pd.notna(x)])
]
values = {columns[i]: df.iloc[i].values for i in df.index}
df = pd.DataFrame(data = values).fillna('')

# Display the final results
df
