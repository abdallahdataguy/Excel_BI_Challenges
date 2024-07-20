# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7220272337693122560-Mpkh/

from itertools import product

# Read the data ranges
df1 = xl("A2:C7", headers=True)
df2 = xl("A10:C16", headers=True)

# Perform data munging
minimum = df1.iloc[:, 1:].values.min()
maximun = df1.iloc[:, 1:].values.max()
df2.iloc[:, 1] = df2.iloc[:, 1].fillna(minimum)
df2.iloc[:, 2] = df2.iloc[:, 2].fillna(maximun)
df1 = df1.set_index(keys='Buyer')
df2 = df2.set_index(keys='Items')
df = pd.DataFrame(data=list(df1.index), columns=['Buyer / Items'])
for item in df2.index:
    df[item] = ''
for item, buyer in product(df2.index, df1.index):
        buy = pd.date_range(df1.at[buyer, 'Buy Date From'], df1.at[buyer, 'Buy Date To'])
        stock = pd.date_range(df2.at[item, 'Stock Start Date'], df2.at[item, 'Stock Finish Date'])   
        if any([x in stock for x in buy]):
            df[item][df['Buyer / Items'] == buyer] = 'X'

# Display the final results       
df
