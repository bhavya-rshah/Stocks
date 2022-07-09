import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mf
import datetime as dt

#Plot a simple stock
start = dt.datetime(2022,2,2)
end = dt.datetime.now()
data = web.DataReader('CAD=X', 'yahoo', start, end)

mf.plot(data, type="candle", style="yahoo")

#Look at basic crypto
