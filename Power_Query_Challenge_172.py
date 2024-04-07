# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7182587900008488960-NtYQ/

import pandas as pd

# Read the Excel file
file_path = 'PQ_Challenge_172.xlsx'
df = pd.read_excel(file_path, usecols='A:F')

# Data transformation and cleansing
df.iloc[:, 5].fillna('100', inplace=True)
agents = set(df['Agent1'].dropna().unique()).union(set((df['Agent2'].dropna().unique())))
agents_dict = {key: 0 for key in sorted(list(agents))}
for row in df.iterrows():
    if not pd.isnull(row[1][2]):
        agents_dict[row[1][2]] += 0.0001 * row[1][1] * row[1][4] * float(row[1][5].split(', ')[0])
    if not pd.isnull(row[1][3]):
        try:
            agents_dict[row[1][3]] += 0.0001 * row[1][1] * row[1][4] * float(row[1][5].split(', ')[1])
        except:
            agents_dict[row[1][3]] += 0.0001 * row[1][1] * row[1][4] * float(row[1][5].split(', ')[0])

agents_dict = {'Agent': agents_dict.keys(), 'Commission': agents_dict.values()}
df = pd.DataFrame(agents_dict)
df.loc[df.shape[0]] = ['Total', sum(df['Commission'])]
df['Commission'] = round(df['Commission']).astype(int)

# Print the output
print(f'Final Results:\n\n{df}')
