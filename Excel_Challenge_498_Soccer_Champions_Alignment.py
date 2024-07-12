# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7217376417670430722-4VUX/

# Read the data range
df = xl("A2:B10", headers=True)

# Perform data wrangling
df.columns = [col[: -1] for col in df.columns]
df['Year'] = df['Year'].map(lambda x: x.split(', '))
df = df.explode(column='Year')
df = df.sort_values(by='Year', ascending=False, ignore_index=True)
df = df[['Year', 'Winner']]

# Display the final results
df
