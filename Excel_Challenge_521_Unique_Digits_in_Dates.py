# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7229335942967304192-v0FP/

# Create a list of dates
dates = np.arange('1900-01-01', '3000-01-01', dtype='datetime64[D]')

# Filter the dates with unique digits
dates = filter(
    lambda x: 
    all(
        str(x).count(y) == 1 for y in str(x) if y != '-'
    ), dates
)
df = pd.DataFrame(data=dates, columns=['Dates'])

# Display the final results (3060 results)
df
