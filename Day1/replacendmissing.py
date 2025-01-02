import pandas as pd

def replace_missing_spaces(input_string):
    
    char_counts = pd.Series(list(input_string)).value_counts()
    
   
    least_frequent_char = char_counts.idxmin()
    
   
    modified_string = input_string.replace(' ', least_frequent_char)
    
    return modified_string


input_string = "This is an ex mple string with m ssing spaces."
result = replace_missing_spaces(input_string)
print("Modified string:", result)
