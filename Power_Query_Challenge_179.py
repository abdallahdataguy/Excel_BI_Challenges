# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7192372368030232577-zv0e/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_179.xlsx'
df = pd.read_excel(file_path, usecols='A:C')

# Perform data transformation and cleansing
max_players = df.groupby('Team')['Player'].count().max()
values = []
for team in df['Team'].unique():
    players = df['Player'][df['Team'] == team].tolist()
    high_score = df.groupby('Team')['Runs Scored'].max()[team]
    hs_players = ', '.join(df['Player'][(df['Team'] == team) & (df['Runs Scored'] == high_score)].tolist())
    players = [team] + players + [''] * (max_players - len(players)) + [hs_players, high_score]
    values.append(players)

# Make players columns dynamic
names = ['Team'] + ['Player' + str(x) for x in range(1, max_players + 1)] + ['Highest Scoring Player', 'Highest Score']
df = pd.DataFrame(values, columns=names)

# Display the output
df
