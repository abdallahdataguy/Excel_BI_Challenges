# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7218101919368527872-2XEd/

# Read the data ranges
df1 = xl("A1:D6", headers=True)
df2 = xl("F1:I6", headers=True)

# Perform data wrangling
df = pd.concat([df1, df2])
df = df.groupby('Student')[sorted(df.columns[1:])].max().reset_index()
df = df.replace(np.nan, 0)
df[df.columns[1:]] = df[df.columns[1:]].astype(int).replace(0, '')

# Display the final results
df
