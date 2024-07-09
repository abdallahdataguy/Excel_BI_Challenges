# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7216290180268232705-8KRk/

# Create a function to generate the summary
def pallindrome_info(length):
    min_num = 10 ** (length - 1)
    max_num = 10 ** length
    rng = range(min_num, max_num)
    numbers = list(filter(lambda x: x == int(str(x)[::-1]), rng))
    return len(numbers), sum(numbers)

# Read the data range
df = xl("A2:A9", headers=True)

# Perform data wrangling
df[['Count', 'Sum']] = df['N'].map(pallindrome_info).tolist()

# Display the final results
df
