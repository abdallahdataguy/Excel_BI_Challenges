# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7242744287510073344-6QTI/

from itertools import combinations
# Create a function to decrypt a text
def encrypt(df, text):
    chars = [char.upper() for char in text]
    values = []
    for char in chars:
        row, col = df[df['Character'] == char].reset_index().iloc[0, 2:]
        values.append('.' * row + ' ' + '.' * col)
    return ' '.join(values)

# Read the data ranges
df1 = xl("A1:F6", headers=True)
df2 = xl("H1:I10", headers=True)

# Perform data manipulation
df1[3] = df1[3].str.split('/')
df1 = df1.explode(column=3, ignore_index=True)
values = df1.apply(lambda x: zip(x[1:], [x.values[0] for y in x], df1.columns[1:]), axis=1)
items = []
for value in values:
    items.extend(value)
df1 = pd.DataFrame(data=items, columns=['Character', 'Row', 'Column'])
df1 = df1.drop_duplicates().sort_values(by='Character', ignore_index=True)
df2['My Answer'] = df2['Words'].map(lambda x: encrypt(df1, x))
df2['Check'] = df2['My Answer'] == df2['Answer Expected']

# Display the final results
df2
