# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7219189093883162624-_oe8/

# Read the data range
df = xl("B2:M10", headers=False)

# Perform data wrangling
df = df.replace(np.nan, "")
arr1 = df.values
arr2 = df.apply(lambda x: x.shift(1)).values
arr3 = df.apply(lambda x: x.shift(-1), axis=1).values
arr4 = ((arr1 == arr2) | (arr1 == arr3)) * arr1 
items = np.unique(arr4[(arr4 != '') & (arr4 != 0)])

# Display the final results
items
