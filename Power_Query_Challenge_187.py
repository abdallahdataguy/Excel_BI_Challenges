# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7202521030186172416-lZi1/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_187.xlsx'
df = pd.read_excel(file_path, usecols='A:C', nrows=11, keep_default_na=False)

# Perform data wrangling
df1 = pd.DataFrame(sorted(df['Continent'].unique()), columns=['Continent'])
years = sorted(df['Year'].unique())

dfs = []
for year in years:
    dfn = pd.merge(df1, df[df['Year'] == year], how='left')
    dfn['Year'] = dfn['Year'].fillna(year).astype(int)
    dfn['Sales'] = dfn['Sales'].fillna(0).astype(int)
    dfn = dfn.astype(str)
    dfn.loc[len(dfn)] = ['TOTAL', str(year), str(sum(df['Sales'][df['Year'] == year]))]
    dfn.loc[len(dfn)] = ['', '', '']
    dfs.append(dfn)

overall = ['GRAND TOTAL', str(years[0]) + '-' + str(years[-1]), str(sum(df['Sales']))]
df = pd.concat(dfs, ignore_index=True)
df.loc[len(df)] = overall

# Display the final results
df
