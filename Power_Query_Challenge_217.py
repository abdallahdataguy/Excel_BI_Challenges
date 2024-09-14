# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7240571624696012800-4aqc/

# Read the data range
df = xl("A1:H5", headers=True)

# Perform data wrangling
values = df.apply(
    lambda x: [x[i] if i < 2 else x[i] * x[1] for i in range(len(df.columns))], 
    axis=1
).tolist()
df = pd.DataFrame(data=values, columns=df.columns).drop(columns='Amt')
df['Total'] = df.apply(lambda x: sum(x[1:]), axis=1)
df = df.set_index('Customer').transpose().reset_index()
df['Total'] = df.apply(lambda x: sum(x[1:]), axis=1)
df = df.rename(columns={'index': 'Month'})
df.columns.name = ''

# Display the final results
df
