import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2024-12-31'

# Fetch historical stock prices for Alphabet Inc. (GOOGL)
googl_data = web.DataReader('GOOGL', 'yahoo', start_date, end_date)

# Create a line plot
googl_data['Close'].plot(title='Historical Stock Prices of Alphabet Inc. (GOOGL)', 
                          xlabel='Date', ylabel='Closing Price (USD)')
plt.show()
