from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
Current_Date = datetime.date.today()

#
#  change date - no need to change ticker
#
#
tickers = ['SPY']

start_date = '2007 - 01 - 01'
end_date = Current_Date

panel_data = data.DataReader(tickers, 'yahoo', start_date,end_date)

close = panel_data['Close']
opens = panel_data['Open']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
first_bis_day_of_mon = pd.date_range(start=start_date, end=end_date, freq='BMS')
weeklies = pd.date_range(start=start_date, end=end_date, freq='W-FRI')
close = close.reindex(first_bis_day_of_mon)
close = close.fillna(method='ffill')
opens = opens.reindex(first_bis_day_of_mon)
opens = opens.fillna(method='ffill')


spy = close.loc[first_bis_day_of_mon, 'SPY']
spyo = opens.loc[first_bis_day_of_mon, 'SPY']  

short_rolling_spy = spy.rolling(window=20).mean()
mid_rolling_spy = spy.rolling(window=50).mean()
long_rolling_spy = spy.rolling(window=200).mean()

fig, ax = plt.subplots(figsize=(16,9))



        # EMAs 
emasix = spy.ewm(span=6,adjust=False).mean()
ematen = spy.ewm(span=10,adjust=False).mean()
ematwenty = spy.ewm(span=20,adjust=False).mean()

ax.plot(spy.index, emasix, label='6ema', color = 'red')
ax.plot(spy.index, ematen, label='10ema', color = 'blue')





ax.plot(spy.index, spy, label='SPY', color = 'black')
ax.plot(spy.index, spyo, label='SPY-o', color = 'black')

# ax.plot(short_rolling_spy.index, short_rolling_spy, label='20 days rolling')
# ax.plot(mid_rolling_spy.index, mid_rolling_spy, label='50 days rolling')
# ax.plot(long_rolling_spy.index, long_rolling_spy, label='200 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.title('Monthly 10&6 EMA')


hold = []
holdindex = []
holdtrash = []

hedge = []
hedgeindex = []
hedgetrash = []

for i in range(0,spy.size): 
    if spy[i] > ematen[i] and emasix[i] > ematen[i]:
        hold.append(spy[i])
        holdindex.append(first_bis_day_of_mon[i])

    else:
        holdtrash.append(spy[i])
        
    if spy[i] < ematen[i] and emasix[i] < ematen[i]:
        hedge.append(spy[i])
        hedgeindex.append(first_bis_day_of_mon[i])

    else:
        hedgetrash.append(spy[i])
        
# can use len('list') to check
    
plt.scatter(holdindex,hold,color='blue',s = 50,alpha=1)
plt.scatter(hedgeindex,hedge,color='red',s = 50,alpha=1)

