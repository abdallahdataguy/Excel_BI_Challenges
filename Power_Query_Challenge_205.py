# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7225350748308480001-W_Q7/

# Read the data ranges
df1 = xl("A2:B13", headers=True)
df2 = xl("D2:E13", headers=True)

# Perform data munging
df3 = pd.merge(df2, df1)
df3 = df3.sort_values(by='YesNo', ascending=False, ignore_index=True)

df = pd.DataFrame(columns=['YesNo', 'Item', 'Sum'])
for value in df3['YesNo'].unique():
    dfn = df3[df3['YesNo'] == value].reset_index(drop=True)
    items = [dfn['Item'].tolist()[i: i + 2] for i in range(0, len(dfn), 2)]
    items = [x + [''] if len(x) == 1 else x for x in items]
    values = [sum(dfn['Value'].tolist()[i: i + 2]) for i in range(0, len(dfn), 2)]
    df.loc[len(df)] = [value, items, values]

df = df.explode(column=['Item', 'Sum'], ignore_index=True)
df[['Item1', 'Item2']] = df['Item'].tolist()
df['Cumsum'] = df.groupby('YesNo')['Sum'].transform('sum')
df['%age'] = df.apply(lambda x: f'{x.Sum / x.Cumsum:.0%}', axis=1)
df = df.iloc[:, [0, 3, 4, 2, 6]]

# Display the final results
df
