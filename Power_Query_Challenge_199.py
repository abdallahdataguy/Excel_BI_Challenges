# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7217739351147872256-3VjL/

import re

# Select a data range
df = xl("A1:A5", headers=True)

# Perform data wrangling
df['Part No.'] = df['String'].map(
lambda x: re.findall(r' (\d+)(?!\/)', x)[0]
)
df['Date'] = df['String'].map(
lambda x: [y.replace('//', '/') for y in re.findall(r'(\d+/\d+//?\d+)', x)]
)
df = df.explode(column='Date')
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
df = df.sort_values(by=['Part No.', 'Date'], ignore_index=True)
df = df[['Part No.', 'Date']]

# Display the final dataset
df
