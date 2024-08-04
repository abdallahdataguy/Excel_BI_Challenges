# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7225712087539286016-XgfP/

# Read the data range
df = xl("A1:D13", headers=True)

# Perform data munging
df = df.drop(index=[3, 10]).reset_index(drop=True)
df[['Value1', 'Value2']] = df[['Value1', 'Value2']].fillna(0).astype(int)

df = pd.concat(
    [
        pd.DataFrame([[df.iat[i, 0], df.iat[i, 1]], [df.iat[i, 2], df.iat[i, 3]]]) 
        for i in df.index
    ], ignore_index=True
)

dfs = [df.iloc[i : i + 6, :].reset_index(drop=True) for i in df.index[::6]]
dfs = [pd.concat([df.iloc[i : i + 2, :] for i in df.index[::2]], axis=1) for df in dfs]
for dfi in dfs:
    dfi.columns = ['Column' + str(i + 1) for i in range(len(dfi.columns))]
df = pd.concat(dfs).replace(0, '').dropna(how='all', ignore_index=True).fillna('')

# Display the final results
df
