# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:07:31 2020

@author: seanw
"""

# Buy when price < 150ma - green
# Hedge when price < 250ma - red
# Carry when price > 150ma - blue
#
#
#  Can switch ticker(lines 26, 41, 42, 49) and dates (lines 28 and 29)
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
spywo = opens.loc[all_weekdays, 'SPY']      ### TWO ###

mid_rolling_spyw = spyw.rolling(window=300).mean()     ### THREE ###

fig, ax = plt.subplots(figsize=(16,9))


ax.plot(spyw.index, spyw, label='SPY', color = 'black')     ### FOUR ###
ax.plot(spyw.index, spywo, color = 'black') 

ax.plot(mid_rolling_spyw.index, mid_rolling_spyw, label='300 days rolling')      ### FIVE ###

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
ax.grid(True)



#  MAs
buy = []
buyindex = []
trashbuy = []

hedge = []
hedgeindex = []
trashhedge = []

carry = []
carryindex = []
trashcarry = []

for i in range(250,spyw.size): 
        spywtwofifty = ((spyw[i-249]+spyw[i-248]+spyw[i-247]+spyw[i-246]+spyw[i-245]+\
                  spyw[i-244]+spyw[i-243]+spyw[i-242]+spyw[i-241]+spyw[i-240]+\
                  spyw[i-239]+spyw[i-238]+spyw[i-237]+spyw[i-236]+spyw[i-235]+\
                  spyw[i-234]+spyw[i-233]+spyw[i-232]+spyw[i-231]+spyw[i-230]+\
                  spyw[i-229]+spyw[i-228]+spyw[i-227]+spyw[i-226]+spyw[i-225]+\
                  spyw[i-224]+spyw[i-223]+spyw[i-222]+spyw[i-221]+spyw[i-220]+\
                  spyw[i-219]+spyw[i-218]+spyw[i-217]+spyw[i-216]+spyw[i-215]+\
                  spyw[i-214]+spyw[i-213]+spyw[i-212]+spyw[i-211]+spyw[i-210]+\
                  spyw[i-209]+spyw[i-208]+spyw[i-207]+spyw[i-206]+spyw[i-205]+\
                  spyw[i-204]+spyw[i-203]+spyw[i-202]+spyw[i-201]+spyw[i-200]+\
                  spyw[i-199]+spyw[i-198]+spyw[i-197]+spyw[i-196]+spyw[i-195]+\
                  spyw[i-194]+spyw[i-193]+spyw[i-192]+spyw[i-191]+spyw[i-190]+\
                  spyw[i-189]+spyw[i-188]+spyw[i-187]+spyw[i-186]+spyw[i-185]+\
                  spyw[i-184]+spyw[i-183]+spyw[i-182]+spyw[i-181]+spyw[i-180]+\
                  spyw[i-179]+spyw[i-178]+spyw[i-177]+spyw[i-176]+spyw[i-175]+\
                  spyw[i-174]+spyw[i-173]+spyw[i-172]+spyw[i-171]+spyw[i-170]+\
                  spyw[i-169]+spyw[i-168]+spyw[i-167]+spyw[i-166]+spyw[i-165]+\
                  spyw[i-164]+spyw[i-163]+spyw[i-162]+spyw[i-161]+spyw[i-160]+\
                  spyw[i-159]+spyw[i-158]+spyw[i-157]+spyw[i-156]+spyw[i-155]+\
                  spyw[i-154]+spyw[i-153]+spyw[i-152]+spyw[i-151]+spyw[i-150]+\
                  spyw[i-149]+spyw[i-148]+spyw[i-147]+spyw[i-146]+spyw[i-145]+\
                  spyw[i-144]+spyw[i-143]+spyw[i-142]+spyw[i-141]+spyw[i-140]+\
                  spyw[i-139]+spyw[i-138]+spyw[i-137]+spyw[i-136]+spyw[i-135]+\
                  spyw[i-134]+spyw[i-133]+spyw[i-132]+spyw[i-131]+spyw[i-130]+\
                  spyw[i-129]+spyw[i-128]+spyw[i-127]+spyw[i-126]+spyw[i-125]+\
                  spyw[i-124]+spyw[i-123]+spyw[i-122]+spyw[i-121]+spyw[i-120]+\
                  spyw[i-119]+spyw[i-118]+spyw[i-117]+spyw[i-116]+spyw[i-115]+\
                  spyw[i-114]+spyw[i-113]+spyw[i-112]+spyw[i-111]+spyw[i-110]+\
                  spyw[i-109]+spyw[i-108]+spyw[i-107]+spyw[i-106]+spyw[i-105]+\
                  spyw[i-104]+spyw[i-103]+spyw[i-102]+spyw[i-101]+spyw[i-100]+\
                  spyw[i-99]+spyw[i-98]+spyw[i-97]+spyw[i-96]+spyw[i-95]+\
                  spyw[i-94]+spyw[i-93]+spyw[i-92]+spyw[i-91]+spyw[i-90]+\
                  spyw[i-89]+spyw[i-88]+spyw[i-87]+spyw[i-86]+spyw[i-85]+\
                  spyw[i-84]+spyw[i-83]+spyw[i-82]+spyw[i-81]+spyw[i-80]+\
                  spyw[i-79]+spyw[i-78]+spyw[i-77]+spyw[i-76]+spyw[i-75]+\
                  spyw[i-74]+spyw[i-73]+spyw[i-72]+spyw[i-71]+spyw[i-70]+\
                  spyw[i-69]+spyw[i-68]+spyw[i-67]+spyw[i-66]+spyw[i-65]+\
                  spyw[i-64]+spyw[i-63]+spyw[i-62]+spyw[i-61]+spyw[i-60]+\
                  spyw[i-59]+spyw[i-58]+spyw[i-57]+spyw[i-56]+spyw[i-55]+\
                  spyw[i-54]+spyw[i-53]+spyw[i-52]+spyw[i-51]+spyw[i-50]+\
                  spyw[i-49]+spyw[i-48]+spyw[i-47]+spyw[i-46]+spyw[i-45]+\
                  spyw[i-44]+spyw[i-43]+spyw[i-42]+spyw[i-41]+spyw[i-40]+\
                  spyw[i-39]+spyw[i-38]+spyw[i-37]+spyw[i-36]+spyw[i-35]+\
                  spyw[i-34]+spyw[i-33]+spyw[i-32]+spyw[i-31]+spyw[i-30]+\
                  spyw[i-29]+spyw[i-28]+spyw[i-27]+spyw[i-26]+spyw[i-25]+\
                  spyw[i-24]+spyw[i-23]+spyw[i-22]+spyw[i-21]+spyw[i-20]+\
                  spyw[i-19]+spyw[i-18]+spyw[i-17]+spyw[i-16]+spyw[i-15]+\
                  spyw[i-14]+spyw[i-13]+spyw[i-12]+spyw[i-11]+spyw[i-10]+\
                  spyw[i-9]+spyw[i-8]+spyw[i-7]+spyw[i-6]+spyw[i-5]+\
                  spyw[i-4]+spyw[i-3]+spyw[i-2]+spyw[i-1]+spyw[i])/250)
            
        spywonefifty = ((spyw[i-149]+spyw[i-148]+spyw[i-147]+spyw[i-146]+spyw[i-145]+\
                  spyw[i-144]+spyw[i-143]+spyw[i-142]+spyw[i-141]+spyw[i-140]+\
                  spyw[i-139]+spyw[i-138]+spyw[i-137]+spyw[i-136]+spyw[i-135]+\
                  spyw[i-134]+spyw[i-133]+spyw[i-132]+spyw[i-131]+spyw[i-130]+\
                  spyw[i-129]+spyw[i-128]+spyw[i-127]+spyw[i-126]+spyw[i-125]+\
                  spyw[i-124]+spyw[i-123]+spyw[i-122]+spyw[i-121]+spyw[i-120]+\
                  spyw[i-119]+spyw[i-118]+spyw[i-117]+spyw[i-116]+spyw[i-115]+\
                  spyw[i-114]+spyw[i-113]+spyw[i-112]+spyw[i-111]+spyw[i-110]+\
                  spyw[i-109]+spyw[i-108]+spyw[i-107]+spyw[i-106]+spyw[i-105]+\
                  spyw[i-104]+spyw[i-103]+spyw[i-102]+spyw[i-101]+spyw[i-100]+\
                  spyw[i-99]+spyw[i-98]+spyw[i-97]+spyw[i-96]+spyw[i-95]+\
                  spyw[i-94]+spyw[i-93]+spyw[i-92]+spyw[i-91]+spyw[i-90]+\
                  spyw[i-89]+spyw[i-88]+spyw[i-87]+spyw[i-86]+spyw[i-85]+\
                  spyw[i-84]+spyw[i-83]+spyw[i-82]+spyw[i-81]+spyw[i-80]+\
                  spyw[i-79]+spyw[i-78]+spyw[i-77]+spyw[i-76]+spyw[i-75]+\
                  spyw[i-74]+spyw[i-73]+spyw[i-72]+spyw[i-71]+spyw[i-70]+\
                  spyw[i-69]+spyw[i-68]+spyw[i-67]+spyw[i-66]+spyw[i-65]+\
                  spyw[i-64]+spyw[i-63]+spyw[i-62]+spyw[i-61]+spyw[i-60]+\
                  spyw[i-59]+spyw[i-58]+spyw[i-57]+spyw[i-56]+spyw[i-55]+\
                  spyw[i-54]+spyw[i-53]+spyw[i-52]+spyw[i-51]+spyw[i-50]+\
                  spyw[i-49]+spyw[i-48]+spyw[i-47]+spyw[i-46]+spyw[i-45]+\
                  spyw[i-44]+spyw[i-43]+spyw[i-42]+spyw[i-41]+spyw[i-40]+\
                  spyw[i-39]+spyw[i-38]+spyw[i-37]+spyw[i-36]+spyw[i-35]+\
                  spyw[i-34]+spyw[i-33]+spyw[i-32]+spyw[i-31]+spyw[i-30]+\
                  spyw[i-29]+spyw[i-28]+spyw[i-27]+spyw[i-26]+spyw[i-25]+\
                  spyw[i-24]+spyw[i-23]+spyw[i-22]+spyw[i-21]+spyw[i-20]+\
                  spyw[i-19]+spyw[i-18]+spyw[i-17]+spyw[i-16]+spyw[i-15]+\
                  spyw[i-14]+spyw[i-13]+spyw[i-12]+spyw[i-11]+spyw[i-10]+\
                  spyw[i-9]+spyw[i-8]+spyw[i-7]+spyw[i-6]+spyw[i-5]+\
                  spyw[i-4]+spyw[i-3]+spyw[i-2]+spyw[i-1]+spyw[i])/150)
            
            #  Buy when price < 150ma
        if spyw[i] < spywonefifty:
                buy.append(spyw[i])
                buyindex.append(all_weekdays[i])
        else:
            trashbuy.append(spyw[i])
            
            #  Hedge when price < 250ma
        if spyw[i] < spywtwofifty:
                hedge.append(spyw[i])
                hedgeindex.append(all_weekdays[i])
        else:
            trashhedge.append(spyw[i])
            
            #  Carry when price > 150ma
        if spyw[i] > spywonefifty:
                carry.append(spyw[i])
                carryindex.append(all_weekdays[i])
        else:
            trashcarry.append(spyw[i])
            
            
        # plotting colored dots    
            
plt.scatter(buyindex,buy,color='green',s = 50,alpha=1)
plt.scatter(hedgeindex,hedge,color='red',s = 20,alpha=1)
plt.scatter(carryindex,carry,color='blue',s = 15,alpha=1)
