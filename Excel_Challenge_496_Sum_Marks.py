# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7216652353792294912-Ytng/

import re

# Read the data range
df = xl("A2:B7", headers=True)

# Perform data wrangling
values = [(x[0], int(x[1])) for y in df['Subjects'] 
          for x in re.findall('([A-Za-z]+)\D*(\d+)', y)]

df = pd.DataFrame(data=values, columns=['Subjects', 'Total'])
df = df.groupby('Subjects')['Total'].sum().reset_index()

# Display the final results
df
