# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7227523994650873856-k7Vp/

# Read the data range.
df = xl("A1:C20", headers=True)

# Perform data wrangling
arr = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
df['Ind'] = df['Grades'].map(
    lambda x: np.nan if x == 'F' else arr.index(x)
)

df['My Answer'] = df['Ind'].rank(method='dense')
df = df[['Name', 'Grades', 'Answer Expected', 'My Answer']].fillna('')

# Display the final results
df
