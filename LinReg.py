import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt
import datetime

# msft
df = yf.download("MSFT", period = "1mo")
# df
# df['Close'].plot()
df['Percent_change'] = (df['Close'] - df['Open'])/df['Open'] * 100
df['Dollar_change'] = (df['Close'] - df['Open'])
# df['Percent_change'].plot()
# df = df[['Close','Dollar_change','Percent_change']]
# df['Forecast']
#x = df['Date']
#y1 = df['Close']
#y2 = df['Dollar_change']
#plt.plot(x, y1)
df
