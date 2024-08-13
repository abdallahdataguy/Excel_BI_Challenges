# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7228973550890549248-kesL/

# Read the data range
df = xl("A1:I4", headers=True)

# Perform data munging
cols = df.columns.tolist()
half_cols = len(cols) // 2
headers1 = cols[1: half_cols + 1]
headers2 = cols[half_cols + 1: ]

values = []
for i in df.index:
    f = [i + 1]
    a = df.iloc[i, 1: half_cols + 1].tolist()
    b = df.iloc[i, half_cols + 1:].tolist()
    if len([x for x in a if pd.notna(x)]) > 1:
        values.extend([f + headers1, f + a])
    if len([x for x in b if pd.notna(x)]) > 1:
        values.extend([f + headers2, f + b])

df = pd.DataFrame(values).fillna('')

# Display the final results
df
