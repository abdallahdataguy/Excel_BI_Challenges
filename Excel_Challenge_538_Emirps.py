# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7237670857911730176--4uy/

from sympy import isprime

# Create a function to identify emirp numbers
def isemirp(num):
    rev = int(str(num)[::-1])
    emirp = isprime(num) and isprime(rev) and num != rev
    return emirp

# Perform data munging 
numbers = filter(isemirp, range(10,10000000))  
df = pd.DataFrame(data={"My Answer": numbers})

# Display the final results
df
