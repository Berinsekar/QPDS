import pandas as pd

def series_to_dataframe(series):
    """
    Convert a Pandas Series into a DataFrame, moving the index to a column
    and resetting the index to the default integer index.

    Parameters:
    series (pd.Series): The input Pandas Series.

    Returns:
    pd.DataFrame: The resulting DataFrame with the index as a column.
    """
    if not isinstance(series, pd.Series):
        raise ValueError("Input must be a Pandas Series.")

    dataframe = series.reset_index()
    
   
    dataframe.columns = ['index', 'value']
    
    return dataframe

if __name__ == "__main__":
 
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
    
    dataframe = series_to_dataframe(series)
    print("Converted DataFrame:\n", dataframe)
