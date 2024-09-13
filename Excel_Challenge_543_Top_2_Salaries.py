# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/excelbi_excel-challenge-problem-activity-7240229346810937344-E0nC/

# Read the data range
df = xl("A1:C20", headers=True)

# Perform data manipulation
df = df.sort_values(
    by=['Department', 'Salary', 'Emp Name'], ascending=[True, False, True]
)
values = []
for dep in df['Department'].unique():
    df_dep = df[df['Department'] == dep]
    salaries = df_dep['Salary'].unique()
    if len(salaries) > 2:
        employees = df_dep['Emp Name'][df_dep['Salary'] > salaries[2]]
    else:
        employees = df_dep['Emp Name'][df_dep['Salary'] >= salaries[-1]]
    values.append([dep, ', '.join(employees)])
    
df = pd.DataFrame(data=values, columns=df.columns[:2])

# Display the final results
df
