# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7215927608440479744-KxUI/

def is_tech_number(number):
    str_num = str(number)
    length = len(str_num)
    half_len = length // 2
    result = (
        int(str_num[ : half_len]) + int(str_num[half_len : ])
    ) ** 2 == number
 
    if length % 2 != 0:
        return False
    else:
        return result
    
def generate_tech_numbers(n):
    numbers = [c for x in range(4, 10 ** 4) if is_tech_number(c := x ** 2)]
    return numbers[ : 10]

generate_tech_numbers(10)
