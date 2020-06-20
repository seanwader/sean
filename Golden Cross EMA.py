# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:22:18 2020

@author: seanw
"""

#
#  change ticker (line 20,36,37), and time (line 22, 23)
#
#
#
#

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


tickers = ['SPY']      ### ONE ###

start_date = '2015 - 01 - 01'
end_date = '2020 - 06 - 19'

panel_data = data.DataReader(tickers, 'yahoo', start_date,end_date)

close = panel_data['Close']
opens = panel_data['Open']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
close = close.reindex(all_weekdays)
close = close.fillna(method='ffill')
opens = opens.reindex(all_weekdays)
opens = opens.fillna(method='ffill')


spyw = close.loc[all_weekdays, 'SPY'] 
spywo = opens.loc[all_weekdays, 'SPY'] 



ematwo = spyw.ewm(span=200,adjust=False).mean()
emafifty = spyw.ewm(span=50,adjust=False).mean()
plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(spyw.index, spyw, label='SPY', color = 'black') 
plt.plot(spyw.index, spywo, label='SPYo', color = 'black')
plt.plot(spyw.index, ematwo, label='200ema') 
plt.plot(spyw.index, emafifty, label='50ema') 


    # plotting the crosses
buy = []
buyindex = []
trashbuy = []

for i in range(49,spyw.size): 
        if emafifty[i-1] < ematwo[i] and emafifty[i] > ematwo[i]:
                buy.append(spyw[i])
                buyindex.append(all_weekdays[i])
        else:
            trashbuy.append(spyw[i])
        
plt.scatter(buyindex,buy,color='blue',s = 100,alpha=1)