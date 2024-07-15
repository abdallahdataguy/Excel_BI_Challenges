# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7218464316188946432-hBpp/

from itertools import islice, count

# Create a function to check if a number
# is Lynch Bell Number or not
def is_lynch_bell_number(number):
    str_num = str(number)
    cond1 = len(str_num) == len(set(str_num))
    cond2 = all(
        [
        False if char == '0' else 
        number/int(char) == number//int(char)
        for char in str_num
       ]
    )
    return cond1 and cond2

# Generate the first 500 Lynch Bell Numbers 
numbers = filter(is_lynch_bell_number, count(10))   
numbers = list(islice(numbers, 500))

# Display the required results
numbers
