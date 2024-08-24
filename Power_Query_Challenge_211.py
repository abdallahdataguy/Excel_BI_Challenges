# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7232959812286771200-vPok/

# Read the data range
df = xl("A1:F10", headers=True)

# Perform data munging
dfs = []
for i in range(df.shape[1])[::2]:
    dfi = df.iloc[:, i : i + 2].drop(index=0)
    dfi.insert(0, 'Group', dfi.columns[0].split()[1])
    dfi.columns = ['Group', 'Name', 'Income']
    dfi = dfi.sort_values(by='Income', ascending=False).dropna()
    dfs.append(dfi)

dfs = sorted(dfs, key=lambda x: -sum(x['Income']))
df = pd.concat(dfs, ignore_index=True)

# Display the final results
df
