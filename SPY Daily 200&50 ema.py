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

start_date = '2015 - 01 - 01'
end_date = Current_Date

panel_data = data.DataReader(tickers, 'yahoo', start_date,end_date)

close = panel_data['Close']
opens = panel_data['Open']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
# first_bis_day_of_mon = pd.date_range(start=start_date, end=end_date, freq='BMS')
# weeklies = pd.date_range(start=start_date, end=end_date, freq='W-FRI')
close = close.reindex(all_weekdays)
close = close.fillna(method='ffill')
opens = opens.reindex(all_weekdays)
opens = opens.fillna(method='ffill')


spy = close.loc[all_weekdays, 'SPY']
spyo = opens.loc[all_weekdays, 'SPY']  

short_rolling_spy = spy.rolling(window=20).mean()
mid_rolling_spy = spy.rolling(window=50).mean()
long_rolling_spy = spy.rolling(window=200).mean()

fig, ax = plt.subplots(figsize=(16,9))



        # EMAs 
# emasix = spy.ewm(span=6,adjust=False).mean()
ema200 = spy.ewm(span=200,adjust=False).mean()
ema50 = spy.ewm(span=50,adjust=False).mean()

# ax.plot(spy.index, emasix, label='6ema', color = 'red')
ax.plot(spy.index, ema200, label='200ema', color = 'blue')
ax.plot(spy.index, ema50, label='50ema', color = 'red')




ax.plot(spy.index, spy, label='SPY', color = 'black')
ax.plot(spy.index, spyo, label='SPY-o', color = 'black')

# ax.plot(short_rolling_spy.index, short_rolling_spy, label='20 days rolling')
# ax.plot(mid_rolling_spy.index, mid_rolling_spy, label='50 days rolling')
# ax.plot(long_rolling_spy.index, long_rolling_spy, label='200 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.title('Daily 200&50 EMA')


hold = []
holdindex = []
holdtrash = []

hedge = []
hedgeindex = []
hedgetrash = []

for i in range(0,len(spy)): 
    if spy[i] > ema200[i] and ema50[i] > ema200[i]:
        hold.append(spy[i])
        holdindex.append(all_weekdays[i])

    else:
        holdtrash.append(spy[i])
        
    if spy[i] < ema200[i] and ema50[i] < ema200[i]:
        hedge.append(spy[i])
        hedgeindex.append(all_weekdays[i])

    else:
        hedgetrash.append(spy[i])
        
# can use len('list') to check
    
plt.scatter(holdindex,hold,color='blue',s = 20,alpha=1)
plt.scatter(hedgeindex,hedge,color='red',s = 20,alpha=1)

