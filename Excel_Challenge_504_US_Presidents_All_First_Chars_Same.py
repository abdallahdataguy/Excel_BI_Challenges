# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7221001608107593728-f1dg/

# Read the data range
df = xl("A1:A47", headers=True)

# Perform data munging
lst = df['US Presidents'][
    df['US Presidents'].map(
        lambda x: all([y[0] == x[0] for y in x.split()])
    )
].reset_index(drop=True).values

# Display the final results
lst
