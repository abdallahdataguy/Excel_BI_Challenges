# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7226436838398337025-8-dv/

# read the data range
df = xl("A2:B7", headers=True)

# Perform data wrangling
df['Split'] = df['Data'].map(lambda x: x.replace('\t', '').split('\n'))

df = df.explode(column='Split')
df[['Name', 'Seq']] = df['Split'].map(lambda x: x.split(' :')).tolist()
df['Seq'] = df['Seq'].map(lambda x: [int(y) for y in x.split(', ')])
df = (
    df
    .explode(column='Seq')
    .loc[:, ['Seq', 'Name', 'State']]
    .sort_values(by='Seq', ignore_index=True)
)

# Display the final results
df
