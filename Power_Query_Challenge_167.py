# Link to the challenge
# https://www.linkedin.com/posts/excelbi_challenge-powerquerychallenge-daxchallenge-activity-7177152088689307648-dOfs/

import pandas as pd

# Create functions to add results columns to the data frame 
def clean_values1(col1, col2, col3):
    try: return (int(col1), col2, float('nan'))
    except: return (float('nan'), float('nan'), col3)

def clean_values2(col1, col2):
    values = [(x, y) for x in col1.unique() for y in col2.unique()]
    return pd.DataFrame(values, columns=['Vaccine', 'Name']) 

def clean_values3(col):
    if pd.isna(col): return 'No'
    else: return 'Yes'

def clean_values4(col1, col2):
    if col1 == 'No': return float('nan')
    elif pd.isna(col2): return 'No'
    else: return 'Yes'

# Read the Excel file and transform data
file_path = 'Power_Query_Challenge_167.xlsx'
df = pd.read_excel(file_path, usecols='A:D', nrows=13)
df.insert(2, 'Name', df['Vaccine'])

# Data transformation and cleansing
df[['Camp No', 'Vaccine', 'Name']] = df.apply(
    lambda x: clean_values1(x['Camp No'], x['Vaccine'], x['Name']), axis=1).tolist()
df[['Camp No', 'Vaccine']] = df[['Camp No', 'Vaccine']].ffill()
df.dropna(subset='Name', inplace=True)
df2 = clean_values2(df['Vaccine'].dropna(), df['Name'].dropna().sort_values())
df = pd.merge(df2, df, on=['Vaccine', 'Name'], how='left')
df = df.drop(columns='Camp No')
df.insert(0, 'Camp No', df.groupby('Vaccine').cumcount() + 1)
df['Notified'] = df['Notification Date'].apply(clean_values3)
df['Administered'] = df.apply(lambda x: clean_values4(x['Notified'], x['Administration Date']), axis=1)

# Filter the required columns and print the results
df = df[[col for col in df.columns if not 'Date' in col]]
print(f'\nFinal Results:\n{df}')
