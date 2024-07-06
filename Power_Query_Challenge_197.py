# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7215203817972260864-fmSP/

from itertools import product

# Read a data range
df = xl("A1:E21", headers=True)

# Perform data wrangling
df['Order'] = df.index
dfs = []
items = df['Item'].unique()
stores = df['Store'].unique()
for item, store in product(items, stores):
    dfn = df[(df['Item'] == item) & (df['Store'] == store)].reset_index(drop=True)
    dfn[['Start stock', 'End Stock']] = float('nan')
    for i in dfn.index:
        dfn.iat[i, 6] = dfn.iat[i, 3] if i == 0 else dfn.iat[i - 1, 7]
        dfn.iat[i, 7] = (i > 0) * dfn.iat[i, 6] + dfn.iat[i, 3] - dfn.iat[i, 4]
    dfs.append(dfn)

df = pd.concat(dfs).sort_values(by='Order', ignore_index=True).drop(columns='Order')
df[['Start stock', 'End Stock']] = df[['Start stock', 'End Stock']].astype(int)

# Display the final dataset
df
