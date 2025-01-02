import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Example datasets
data1 = {'Customer Names': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Chris Evans']}
data2 = {'Customer Names': ['Jon Doe', 'Jane Smyth', 'Alicia Johnson', 'Christ Evans']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Function to compare names using FuzzyWuzzy
def compare_names(name, names_list):
    best_match = process.extractOne(name, names_list, scorer=fuzz.token_sort_ratio)
    return best_match

# Identify matches and calculate similarity scores
results = []

for name in df1['Customer Names']:
    best_match = compare_names(name, df2['Customer Names'])
    results.append({
        'Original Name': name,
        'Matched Name': best_match[0],
        'Similarity Score': best_match[1]
    })

results_df = pd.DataFrame(results)
print(results_df)
