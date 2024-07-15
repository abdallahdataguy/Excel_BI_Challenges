# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7218464316188946432-hBpp/

# Create a function to generate Lynch Bell Numbers
def generate_lynch_bell_numbers(size):
    numbers = []
    number = 10
    while len(numbers) < size:
        str_num = str(number)
        cond1 = len(str_num) == len(set(str_num))
        cond2 = all(
            [
            False if char == '0' else 
            number/int(char) == int(number/int(char)) 
            for char in str_num
            ]
        )
        if cond1 and cond2:
            numbers.append(number)
        number += 1
    return numbers

# Generate the first 500 Lynch Bell Numbers 
numbers = generate_lynch_bell_numbers(500)

# Display the required results
numbers
