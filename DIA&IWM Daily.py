from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
Current_Date = datetime.date.today()

#
#  change dates
#
#

tickers = ['DIA', 'IWM']

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

 
dia = close.loc[all_weekdays, 'DIA']
diao = opens.loc[all_weekdays, 'DIA'] 
iwm = close.loc[all_weekdays, 'IWM']
iwmo = opens.loc[all_weekdays, 'IWM']


fig, ax = plt.subplots(figsize=(16,9))


ax.plot(dia.index, dia, label='DIA', color = 'red')
ax.plot(dia.index, diao, color = 'red')
ax.plot(iwm.index, iwm, label='IWM', color = 'blue')
ax.plot(iwm.index, iwmo, color = 'blue')


# ax.plot(short_rolling_spy.index, short_rolling_spy, label='20 days rolling')
# ax.plot(mid_rolling_spy.index, mid_rolling_spy, label='50 days rolling')
# ax.plot(long_rolling_spy.index, long_rolling_spy, label='200 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.title('DIA & IWM Daily')
