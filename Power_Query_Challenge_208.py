# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7228249881482600448-yXpt/

# Read the data range
df = xl("E1:G35", headers=True)

# Perform data manipulation
values = []
for i in df.index:
    if i > 2 and df.iat[i, 0] == df.iat[i - 3, 0]:
        values.append(round(df.iloc[i - 3: i, 2].mean()))
    else:
        values.append('')
        
df['3 Year MV'] = values
df = df[['Month', 'Year', '3 Year MV']]

# Display the final results
df
