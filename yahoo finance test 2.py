import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from tabulate import tabulate
# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Define the ticker list
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']
# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)
# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker,
                               start_date,
                               end_date,)['Adj Close']
# Print first 5 rows of the data
data.tail()
# ptabulate is for formating the printed data in a tabular format
pdtabulate=lambda tail:tabulate(data.tail(),headers='keys',tablefmt='psql')
# printed the data in tabular format
print(pdtabulate(data.tail()))


# import for plotting data of tickers
import matplotlib.pyplot as plt
# Plot adjusted close price data
data.plot(figsize=(10,7))
plt.legend()
plt.title("Adjusted Close price of %s"%tickers_list,fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='blue', linestyle='-.', linewidth=0.5)
plt.show()