# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7218830492781932545-ikMV/

# Read the data range
df = xl("A2:D11", headers=True)

# Perform data wrangling
columns = df.columns
df[1] = df['Amt1'].where(
    cond=pd.isna(df['Amt1'].shift(1)),
    other=df['Amt1']-df['Amt3'].shift(1)
)
df[2] = df['Amt2']-df['Amt1']
df[3] = df['Amt3']-df['Amt2']

df = df.filter(regex='^[^A]', axis=1)
df.columns = columns

# Display the final results
df
