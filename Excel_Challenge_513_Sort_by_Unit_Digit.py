# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7224987653379653632-5uY2/

# Read the data range
df = xl("A1:B10", headers=True)

# Perform data munging
df['My Answer'] = sorted(df['Numbers'], key=lambda x: str(x)[-1])
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
