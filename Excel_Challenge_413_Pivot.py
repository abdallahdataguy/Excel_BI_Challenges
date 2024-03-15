# Link to the challenge
# https://www.linkedin.com/feed/update/urn:li:activity:7174252973907197953/

import pandas as pd

file_path = 'Excel_Challenge_413 - Pivot.xlsx'
df = pd.read_excel(file_path, usecols='A:B')
df_test = pd.read_excel(file_path, usecols='D:I').dropna(subset=['ID.1']).rename(columns={'ID.1': 'ID'})

df['Serial'] = 'Num ' + (df.groupby('ID').cumcount() + 1).astype(str)
df = df.pivot(index='ID', columns='Serial', values='Num')
df = df.rename_axis(None, axis=1).reset_index()
print(df.columns)

for d in [df, df_test]:
    for col in [x for x in d.columns if 'Num' in x]:
        d[col] = df[col].apply(lambda x: pd.to_numeric(x, errors='coerce')).fillna(-1).astype(int).astype(str)
        d[col] = d[col].replace('-1', '')

print(f'Expected Results:\n{df_test}\n\nMy Results:\n{df}')


