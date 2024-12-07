library(readxl)
library(tidyr)
library(dplyr)

# Load the Excel file
file_path <- 'C:/Users/ABDALLAH/Downloads/PQ_Challenge_240.xlsx'
df <- read_excel(file_path, range = cell_cols('A:C'))

# Perform data manipulation
df <- df %>%
  mutate(Date = as.Date(Date), Items = strsplit(Items, ', ')) %>%
  unnest(Items) %>%
  separate(Items, into = c('Item', 'Value'), sep = ': ') %>%
  arrange(Item) %>%
  pivot_wider(names_from = Item, values_from = Value) %>%
  arrange(Supplier, desc(Date))

# Display the final results
df
