# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7221728409410842624-hFYz/

# Create a function to split and combine text
def split_concat(text1, text2):
    text = text2.split(', ')
    str_nums = [x.split('-') for x in text]
    str_nums = [x if len(x) == 1 else 
                [str(y) for y in range(int(x[0]), int(x[1]) + 1)] 
                for x in str_nums
               ]
    str_nums = [text1 + x for y in str_nums for x in y]
    return ', '.join(str_nums)

# Read the data range
df = xl("A1:B6", headers=True)

# Perform data munging
df['NewNums'] = df.apply(
    lambda x: split_concat(x['Alphabets'], x['Numbers']), axis=1
)
df = df['NewNums'].str.split(', ', expand=True)
values = [x for x in df.values.flatten(order='F') if x]

# Display the final results
values
