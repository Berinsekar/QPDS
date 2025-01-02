import pandas as pd


series1 = pd.Series([1, 2, 3], name='A')
series2 = pd.Series([4, 5, 6], name='B')


vertical_stack = pd.concat([series1, series2])

print("Vertical Stack:\n", vertical_stack)
