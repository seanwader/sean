from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
Current_Date = datetime.date.today()

#
#  change dates
#
#

tickers = ['SPY']

start_date = '2014 - 01 - 01'
end_date = Current_Date

panel_data = data.DataReader(tickers, 'yahoo', start_date,end_date)

close = panel_data['Close']
opens = panel_data['Open']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
first_bis_day_of_mon = pd.date_range(start=start_date, end=end_date, freq='BMS')
weeklies = pd.date_range(start=start_date, end=end_date, freq='W-FRI')
close = close.reindex(weeklies)
close = close.fillna(method='ffill')
opens = opens.reindex(weeklies)
opens = opens.fillna(method='ffill')


spy = close.loc[weeklies, 'SPY']
spyo = opens.loc[weeklies, 'SPY']  

short_rolling_spy = spy.rolling(window=20).mean()
mid_rolling_spy = spy.rolling(window=50).mean()
long_rolling_spy = spy.rolling(window=200).mean()

fig, ax = plt.subplots(figsize=(16,9))



        # EMAs 
# emasix = spy.ewm(span=6,adjust=False).mean()
ema17 = spy.ewm(span=17,adjust=False).mean()
ema43 = spy.ewm(span=43,adjust=False).mean()

# ax.plot(spy.index, emasix, label='6ema', color = 'red')
ax.plot(spy.index, ema17, label='17ema', color = 'blue')
ax.plot(spy.index, ema43, label='43ema', color = 'red')




ax.plot(spy.index, spy, label='SPY', color = 'black')
ax.plot(spy.index, spyo, label='SPY-o', color = 'black')

# ax.plot(short_rolling_spy.index, short_rolling_spy, label='20 days rolling')
# ax.plot(mid_rolling_spy.index, mid_rolling_spy, label='50 days rolling')
# ax.plot(long_rolling_spy.index, long_rolling_spy, label='200 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
# ax.legend()
plt.title('Weekly 43&17 EMA')


hold = []
holdindex = []
holdtrash = []

hedge = []
hedgeindex = []
hedgetrash = []

for i in range(0,spy.size): 
    if spy[i] > ema43[i] and ema17[i] > ema43[i]:
        hold.append(spy[i])
        holdindex.append(weeklies[i])

    else:
        holdtrash.append(spy[i])
        
    if spy[i] < ema43[i] and ema17[i] < ema43[i]:
        hedge.append(spy[i])
        hedgeindex.append(weeklies[i])

    else:
        hedgetrash.append(spy[i])
        
# can use len('list') to check
    
plt.scatter(holdindex,hold,color='blue',s = 50,alpha=1)
plt.scatter(hedgeindex,hedge,color='red',s = 50,alpha=1)

