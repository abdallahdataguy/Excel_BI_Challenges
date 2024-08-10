# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7227888316916895744-G7Zp/

# Read the data range
df = xl("A2:H13", headers=True)

# Perform data wrangling
values = []
for col in df.columns[1 : ]:
    names = ', '.join(df['Name'][df[col] == 'Y'])
    values.append([col, names])

df = pd.DataFrame(data=values, columns=['Day of Week', 'names'])
df = pd.concat([df, df['names'].str.split(', ', expand=True)], axis=1)
df.columns = [
    'Name' + str(x + 1) if str(x).isdigit() else x for x in df.columns
]
df = df.drop(columns='names').fillna('')

# Display the final results
df
