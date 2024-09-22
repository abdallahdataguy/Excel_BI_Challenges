# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7243469077933965313-hFh4/

from datetime import datetime

# Read the data range
df = xl("A1:D9", headers=True)

# Perform data manipulation
df['Dates'] = df.apply(lambda x: [y.strftime('%b-%y') for y in pd.date_range(x[2], x[3])], axis=1)
df = df.explode(column='Dates').drop_duplicates()
df = df.groupby(['Project', 'Dates'], sort=False)['Activities'].agg(', '.join).reset_index()
df = pd.pivot(data=df, index='Project', columns='Dates', values='Activities').reset_index()
df.columns.name = ''

values = []
for i in df.index:
    a = df.iloc[i, :].values
    b = max([len(x.split(', ')) if pd.notna(x) else 0 for x in a[1:]])
    c = [[a[0]] * b] + [[''] * b if pd.isna(x) else x.split(', ') + [''] * (b - len(x.split(', '))) for x in a[1:]]
    values.extend(zip(*c)) # Unpacking list items and zip

df = pd.DataFrame(values, columns=df.columns).fillna('')
df = df[['Project'] + sorted(df.columns[1:], key=lambda x: datetime.strptime(x, '%b-%y'))]

# Display the final results
df
