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


fig, ax = plt.subplots(figsize=(16,9))




ax.plot(spy.index, spy, label='SPY', color = 'black')
ax.plot(spy.index, spyo, color = 'black')


# ax.plot(short_rolling_spy.index, short_rolling_spy, label='20 days rolling')
# ax.plot(mid_rolling_spy.index, mid_rolling_spy, label='50 days rolling')
# ax.plot(long_rolling_spy.index, long_rolling_spy, label='200 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.title('SPY Daily')
