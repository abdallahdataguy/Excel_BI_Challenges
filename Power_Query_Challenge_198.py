# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7215565192485621760-otuB/

# Read the data range
df = xl("A1:B20", headers=True)

# Perform data wrangling
df['Period'] = df['Date'].map(lambda x: f'{x.year}{x.month}')
df2 = df.groupby('Period')['Value'].max().cumsum()
df2 = df2.reset_index().rename(columns={'Value': 'Running Total'})
df = pd.merge(df, df2, on='Period').drop(columns='Period')

# Display the final dataset
df
