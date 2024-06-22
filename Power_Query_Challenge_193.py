# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7210129241378639872-vLfS/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_193.xlsx'
df = pd.read_excel(file_path, nrows=5)

# Perform data wrangling
columns = df.columns
df.columns = [columns[i - 1] if col.startswith('Un') else col for i, col in enumerate(columns)]
df.columns = [f'{col}_{df.iloc[0][i]}' for i, col in enumerate(df.columns)]
df = df.drop(0)
df = pd.melt(df, id_vars='Quarters_Persons', value_vars=df.columns[1:])
df = pd.concat([df, df['variable'].str.split('_', expand=True)], axis=1)
df = df.drop(columns='variable').iloc[:, [0, 2, 3, 1]]
df.columns = [str(x) for x in df.columns]
df = df.pivot_table(values='value', index=['Quarters_Persons', '1'], columns=['0'], aggfunc='sum')
df = df.reset_index().rename(columns={'Quarters_Persons': 'Persons', '1': 'Category'})

values = []
unique_persons = df['Persons'].unique()
for key, person in enumerate(unique_persons):
    persons = unique_persons[ : key + 1]
    sales_cond = df['Persons'].isin(persons) & (df['Category'] == 'Sales')
    bonus_cond = df['Persons'].isin(persons) & (df['Category'] == 'Bonus')
    total_cond = df['Persons'].isin(persons)
    sales = df.loc[:, 'Q1':][sales_cond].sum().tolist()
    bonus = df.loc[:, 'Q1':][bonus_cond].sum().tolist()
    total = df.loc[:, 'Q1':][total_cond].sum().tolist()
    values.extend([[', '.join(persons), 'Sales'] + sales, ['', 'Bonus'] + bonus, ['', 'Total'] + total])

df = pd.DataFrame(data=values, columns=df.columns)
    
# Display the final dataset
df
