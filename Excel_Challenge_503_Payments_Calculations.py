# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7219913868800622592-0rTb/

# Create a function to calculate payment
def calc_payment(product, price):
    return price if product in dfn.values else 1.1 * price

# Read the data range
df = xl("A1:B9", headers=True)
dfn = xl("D1:D7", headers=True)

# Perform data munging
df['ProductPrice'] = df.iloc[:, 1].map(lambda x: x.split(', '))
df = df.explode(column='ProductPrice').reset_index(drop=True)
df[['Product', 'Price']] = df['ProductPrice'].map(lambda x: x.split(': ')).tolist()
df['Price'] = df['Price'].map(lambda x: int(x.replace(',', '')))
df['Payment'] = df.apply(lambda x: calc_payment(x['Product'], x['Price']), axis=1)
df1 = df.groupby('Customer')['Price'].agg(['sum', 'mean', 'max', 'min', 'count']).reset_index()
df2 = df.groupby('Customer')['Payment'].sum().reset_index(drop=True)
df = pd.concat([df1, df2], axis=1).set_index(keys='Customer')
df.columns = df.columns.str.upper()
df = df.rename(columns = {'MEAN': 'AVERAGE', 'PAYMENT': 'Payment'})
df.index.name = None

# Display the final results
df
