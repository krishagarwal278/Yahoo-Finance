import inline
import matplotlib
import yfinance as yf
from tabulate import tabulate
start_date = '1990-01-01'
end_date = '2021-07-12'
ticker1 = 'AMZN'
ticker2 = 'MSFT'
ticker3 = 'IBM'
ticker4 = 'AAPL'
ticker5 = 'TSLA'
data1 = yf.download(ticker1, start_date, end_date)
data2 = yf.download(ticker2, start_date, end_date)
data3 = yf.download(ticker3, start_date, end_date)
data4 = yf.download(ticker4, start_date, end_date)
data5 = yf.download(ticker5, start_date, end_date)
data1.tail()
data2.tail()
pdtabulate=lambda tail:tabulate(data1.tail(),headers='keys',tablefmt='psql')
# printed the data in tabular format
print("DATA FOR AMZN\n",pdtabulate(data1.tail()))
print("DATA FOR MSFT\n",pdtabulate(data2.tail()))
# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot adjusted close price data
fig = plt.figure()
fig.patch.set_facecolor('#7D7D7D')
fig.patch.set_alpha(0.6)
ax = plt.axes()
ax.set_facecolor("black")
ax.set(facecolor="black")
fancyfont = {'fontname':'Times New Roman'}
#styling over

data1['Adj Close'].plot(figsize=(10, 7),linestyle='-', linewidth=0.65)
plt.legend()
plt.title("Adjusted Close price of %s"% ticker1,**fancyfont, color='blue', fontsize=16)
plt.ylabel('Price($)', **fancyfont,color='blue', fontsize=14)
plt.xlabel('Year',**fancyfont, color='blue', fontsize=14)
plt.grid(which="major", color='blue', linestyle='-.', linewidth=0.3)
plt.show()

# subplot 2
fig = plt.figure()
fig.patch.set_facecolor('#7D7D7D')
fig.patch.set_alpha(0.6)
ax = plt.axes()
ax.set_facecolor("black")
ax.set(facecolor="black")
#beautification over

data2['Adj Close'].plot(figsize=(10, 7),linestyle='-', linewidth=0.65)
plt.legend()
plt.title("Adjusted Close price of %s" % ticker2,**fancyfont, fontsize=16)
plt.ylabel('Price($)',**fancyfont,fontsize=14)
plt.xlabel('Year',**fancyfont,fontsize=14)
plt.grid(which="major", color='blue', linestyle='-.', linewidth=0.3)
plt.show()
