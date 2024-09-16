# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7241297931998244864-tSIH/

import re

# Create a function to extract numbers
def get_numbers(text):
    nums = [int(x) for x in re.findall('\d+', text)]
    result = nums[0] + nums[-1] if len(nums) > 1 else sum(nums)
    return result

# Read the data range
df = xl("A1:A10", headers=True)

# Perform data manipulation
total = df['Strings'].map(get_numbers).sum()

# Display the final results
total
