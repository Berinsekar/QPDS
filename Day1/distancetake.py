import pandas as pd
import numpy as np

def euclidean_distance(series1, series2):
    # Convert Pandas Series to NumPy arrays
    array1 = series1.to_numpy()
    array2 = series2.to_numpy()
    
    # Compute the Euclidean distance
    distance = np.sqrt(np.sum((array1 - array2) ** 2))
    return distance

# Example usage
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])

distance = euclidean_distance(series1, series2)
print("Euclidean Distance:", distance)
