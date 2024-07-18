# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7219556340132691968-EaNE/

from itertools import combinations

# Create a function to generate the required results
def cube_number(number):
    str_nums = list(str(number))
    cube = 0
    for n in range(len(str_nums) - 1, 0, -1):
        if cube: break
        for comb in combinations(sorted(str_nums, reverse=True) if n == 1 else str_nums, n):
            num = int(''.join(comb))
            cube_root = round(num ** (1/3), 9)
            if cube_root == int(cube_root):
                cube = num
                break
    digits = [x for x in str_nums if x not in str(cube)]
    unique = sorted([x for key, x in enumerate(digits) if digits[: key + 1].count(x) == 1])
    return (', '.join(unique), cube) if cube else ('', '')

# Read the data range
df = xl("A2:C10", headers=True)

# Perform data wrangling
df[['My Removed Digits', 'My Cube Number']] = df['Numbers'].map(cube_number).tolist()
df = df.fillna('')

# Display the final results
df
