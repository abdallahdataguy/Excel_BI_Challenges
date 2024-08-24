# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7229698321567629312-ujKt/

# Create a function to generate combinations
def get_odd_combinations(number):
    odd_numbers = [x for x in range(1, number) if x % 2]
    for i in range(len(odd_numbers), 1, -1):
        for j in range(len(odd_numbers) - i + 1):
            cons_odd_numbers = odd_numbers[j : j + i]
            if sum(cons_odd_numbers) == number:
               return ', '.join(str(x) for x in cons_odd_numbers)
    return 'NP'

# Read the data range
df = xl("A1:B8", headers=True)

# Perform data munging
df['My Answer'] = df['Number'].map(get_odd_combinations)
df['Check'] = df['Answer Expected'] == df['My Answer']

# Display the final results
df
