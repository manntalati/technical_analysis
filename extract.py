# To use: pip install tradingview-datafeed

from tvDatafeed import TvDatafeed, Interval
import pandas as pd

# Initialize without login (public access)
tv = TvDatafeed()

# Fetch historical data for Microsoft (MSFT) from NASDAQ
msft_data = tv.get_hist(symbol='MSFT', exchange='NASDAQ', interval=Interval.in_daily, n_bars=500  # Number of data points to retrieve
)

# Display the dataframe
print(msft_data)
