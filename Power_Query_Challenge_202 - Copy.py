# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7220638624931848193-YT_y/

# Read the data range
df = xl("A1:C18", headers=True)

# Perform data munging
name1 = df['Name1'].replace(np.nan, '')
df['Name1'] = df['Name1'].ffill()
df['Level1'] = (df['Name1'] != df['Name1'].shift(1)).cumsum()
df['Level2'] = df.dropna(subset='Name2')[['Name1', 'Name2']].groupby('Name1').transform('cumcount') + 1
df['Level2'] = df['Level2'].ffill()
df['Level3'] = pd.notna(df['Name3'])
df['Level3'] = df[['Name1', 'Name3', 'Level3']].dropna().groupby('Name1')['Level3'].transform('cumsum')
df = df.fillna(0)
df[['Level1', 'Level2', 'Level3']] = df[['Level1', 'Level2', 'Level3']].astype(int)
df = df.astype(str).replace('0', '')
df['Level2'] = df['Level2'] * ((df['Name2'] != '') + (df['Name3'] != ''))
df['Name1'] = name1
df['Serial'] = df.apply(lambda x: '.'.join([y for y in x[3:] if y]), axis=1)
df['Names'] = df.apply(lambda x: ''.join(x[:3]), axis=1)
df = df[['Serial', 'Names']]

# Display the final results.
df
