import pandas as pd

def find_positions(series):
    positions = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            positions.append(i)
    return positions

# Example usage
series = pd.Series([1, 3, 2, 4, 1, 5, 2])
positions = find_positions(series)
print("Positions of values neighbored by smaller values on both sides:", positions)
