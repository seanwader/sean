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



emaonefifty = spyw.ewm(span=150,adjust=False).mean()
emafive = spyw.ewm(span=5,adjust=False).mean()
emathree = spyw.ewm(span=300,adjust=False).mean()
emafivehun = spyw.ewm(span=500,adjust=False).mean()
ematwenty = spyw.ewm(span=20,adjust=False).mean()
emafifty = spyw.ewm(span=50,adjust=False).mean()
plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(spyw.index, spyw, label='SPY', color = 'black') 
plt.plot(spyw.index, spywo, label='SPYo', color = 'black')
plt.plot(spyw.index, emathree, label='300ema', color = 'purple') 
# plt.plot(spyw.index, emafifty, label='50ema', color = 'purple') 
# plt.plot(spyw.index, ematwenty, label='20ema', color = 'orange') 
# plt.plot(spyw.index, emafive, label='5ema',color = 'purple') 
plt.plot(spyw.index, emaonefifty, label='150ema', color = 'red') 
 

    # plotting the crosses
buy = []
buyindex = []
trashbuy = []

carry = []
carryindex = []
trashcarry = []

hedge = []
hedgeindex = []
trashhedge = []

another = []
anotherindex = []
trashanother = []

for i in range(150,spyw.size): 
        if spyw[i] < emaonefifty[i] and emafive[i] < ematwenty[i]:
                buy.append(spyw[i])
                buyindex.append(all_weekdays[i])
        else:
            trashbuy.append(spyw[i])
            
for i in range(150,spyw.size): 
        if spyw[i] > emaonefifty[i] and emafive[i] > ematwenty[i] and spyw[i] > emathree[i]:
                carry.append(spyw[i])
                carryindex.append(all_weekdays[i])
        else:
            trashcarry.append(spyw[i])
            
for i in range(300,spyw.size): 
        if spyw[i] < emathree[i] and emafive[i] < ematwenty[i]:
                hedge.append(spyw[i])
                hedgeindex.append(all_weekdays[i])
        else:
            trashhedge.append(spyw[i])
        
            
            
plt.scatter(buyindex,buy,color='orange',s = 50,alpha=1)
plt.scatter(hedgeindex,hedge,color='red',s = 50,alpha=1)
plt.scatter(carryindex,carry,color='blue',s = 50,alpha=1)
