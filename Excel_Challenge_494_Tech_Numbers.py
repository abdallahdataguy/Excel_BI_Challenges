# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7215927608440479744-KxUI/

def is_tech_number(number):
    str_num = str(number)
    length = len(str_num)
    half_len = length // 2
    result = (
        int(str_num[:half_len]) + int(str_num[half_len:])
    ) ** 2 == number
 
    if length % 2 != 0:
        return False
    else:
        return result
    
def generate_tech_numbers(n):
    numbers = []
    number = 10
    while len(numbers) < n:
        if is_tech_number(number):
            numbers.append(number)
        number += 1
    return numbers

generate_tech_numbers(10)
