# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7240937984114491393-UPyv/

# Read the data range
df = xl("A1:C17", headers=True)

# Perform data manipulation
df['C'] = df.apply(lambda x: x[1] if pd.notna(x[2]) else '', axis=1)
df['N'] = df.apply(lambda x: x[1] if pd.isna(x[2]) else '', axis=1)

df = df.groupby('Project').agg(
    C = ('C', lambda x: ', '.join(filter(None, x))), 
    N = ('N', lambda x: ', '.join(filter(None, x)))
).reset_index()

df = df.rename(columns={'C': 'Completed Tasks', 'N': 'Not Completed Tasks'})

# Display the final results
df
