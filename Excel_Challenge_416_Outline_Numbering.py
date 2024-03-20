# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7176064989001113601-Wq4x/

import pandas as pd

# Read the Excel file
file_path = 'Excel_Challenge_416 - Outline Numbering.xlsx'
df = pd.read_excel(file_path)

# Create a function to generate the required output
def outline_numbering(col):
    values = list(col)
    order = []
    ind = 1
    for i in range(len(values)):
        if i == 0:
            order.append('1')
        elif len(values[i]) == 1:
            ind += 1
            order.append(str(ind))
        elif len(values[i]) == len(values[i - 1]):
            order.append(order[-1][: order[-1].rfind('.')] + '.' +
                         str(int(order[-1][order[-1].rfind('.') + 1: ]) + 1))
        elif len(values[i]) > len(values[i - 1]):
            order.append(order[-1] + '.1')
        else:
            last_dot = order[-1].rfind('.')
            last_second_dot = order[-1].rfind('.', 0, order[-1].rfind('.'))
            order.append(order[-1][: last_second_dot] + '.' + 
                         str(int(order[-1][last_second_dot + 1: last_dot]) + 1))                            
    return order
        
# Add the results column using the above function
df['My Answer'] = pd.Series(outline_numbering(df['Strings']))

# Print the results
print(df)
