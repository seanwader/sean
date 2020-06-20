# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:03:21 2020

@author: seanw
"""

# Change ticker(lines 30, 47, 48), start and end date (lines 32, 33), and flat (line 54) as a decimal(ie. 1% == .001)
# make sure dates match the tickers or days will be off

## Expected output:
# total number days are x
# days all good
# day proportions add up [should be to 1]
# green days all good
# red days all good
# flat days all good
#   note: whatever day is off by 1 is what happen on the start date
# Matrix:  


#
# markov chain matrix outputs at bottom of script with 'flat' being between 1% and -1%

from pandas_datareader import data
import pandas as pd



tickers = ['SPY']                   ### ONE ###

start_date = '1995 - 01 - 03'       ### TWO ###
end_date = '2020 - 06 - 18'         ### THREE ###

panel_data = data.DataReader(tickers, 'yahoo', start_date,end_date)


close = panel_data['Close']
opens = panel_data['Open']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
close = close.reindex(all_weekdays)
opens = opens.reindex(all_weekdays)
close = close.fillna(method='ffill')
opens = opens.fillna(method='ffill')


spyc = close.loc[all_weekdays, 'SPY']    ### FOUR ###
spyo = opens.loc[all_weekdays, 'SPY']    ### FIVE ###

###



flat = .0005


###


# to count days into green, flat, red

spygreen = []
spynotgreen = []

spyred = []
spynotred = []

spyflat = []
spynotflat = []

for i in range(0, len(spyc)):
    if ((spyc[i]-spyo[i])/spyo[i]) > flat:
        spygreen.append(spyc[i])
    else:
        spynotgreen.append(spyc[i])
        
    if ((spyc[i]-spyo[i])/spyo[i]) < -flat:
        spyred.append(spyc[i])
    else:
        spynotred.append(spyc[i])
        
    if ((spyc[i]-spyo[i])/spyo[i]) < flat and ((spyc[i]-spyo[i])/spyo[i]) > -flat:
            spyflat.append(spyc[i])
    else:  spynotflat.append(spyc[i])
    
    
print('total number days are',len(spyc) )
if (len(spyc) == (len(spygreen) + len(spyred) + len(spyflat) )):
    print('days all good')
else:
    print('days dont add up')


propgreen = len(spygreen)/len(spyc)
propred = len(spyred)/len(spyc)
propflat = len(spyflat)/len(spyc)

if (propgreen + propred + propflat == 1):
    print('day proportions all good')
else:
    print('day proportions dont add up') 
    print('        day proportions add up to ',propgreen+propred+propflat) 
    
    
    
    
# current compared to yesterday for green today

spygreengreen = []
spynotgreengreen = []       #trash collector

spyredgreen = []
spynotredgreen = []       #trash collector

spyflatgreen = []
spynotflatgreen = []       #trash collector


for i in range(1, len(spyc)):
    if ((spyc[i]-spyo[i])/spyo[i]) > flat:
        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > flat:
            spygreengreen.append(spyc[i])
        else:
            spynotgreengreen.append(spyc[i])

        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) < -flat:
            spyredgreen.append(spyc[i])
        else:
            spynotredgreen.append(spyc[i])
            
        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > -flat:
            if((spyc[i-1]-spyo[i-1])/spyo[i-1]) < flat:
                spyflatgreen.append(spyc[i])
            else:
                spynotflatgreen.append(spyc[i])
        else:
            spynotflatgreen.append(spyc[i])
                       
    else:
        spynotgreengreen.append(spyc[i])
        
        
# current compared to yesterday for red today

spygreenred = []
spynotgreenred = []      #trash collector

spyredred = []
spynotredred = []       #trash collector

spyflatred = []
spynotflatred = []       #trash collector


for i in range(1, len(spyc)):
    if ((spyc[i]-spyo[i])/spyo[i]) < -flat:
        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > flat:
            spygreenred.append(spyc[i])
        else:
            spynotgreenred.append(spyc[i])

        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) < -flat:
            spyredred.append(spyc[i])
        else:
            spynotredred.append(spyc[i])
            
        if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > -flat:
            if((spyc[i-1]-spyo[i-1])/spyo[i-1]) < flat:
                spyflatred.append(spyc[i])
            else:
                spynotflatred.append(spyc[i])
        else:
            spynotflatred.append(spyc[i])
                       
    else:
        spynotredred.append(spyc[i])
        
        
    
# current compared to yesterday for flat today

spygreenflat = []
spynotgreenflat = []       #trash collector

spyredflat = []
spynotredflat = []       #trash collector

spyflatflat = []
spynotflatflat = []       #trash collector


for i in range(1, len(spyc)):
    if ((spyc[i]-spyo[i])/spyo[i]) > -flat and ((spyc[i]-spyo[i])/spyo[i]) < flat:
            if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > flat:
                spygreenflat.append(spyc[i])
            else:
                spynotgreenflat.append(spyc[i])

            if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) < -flat:
                spyredflat.append(spyc[i])
            else:
                spynotredflat.append(spyc[i])
            
            if ((spyc[i-1]-spyo[i-1])/spyo[i-1]) > -flat:
                if((spyc[i-1]-spyo[i-1])/spyo[i-1]) < flat:
                    spyflatflat.append(spyc[i])
                else:
                    spynotflatflat.append(spyc[i])
            else:
                 spynotflatflat.append(spyc[i])
    else:
         spynotflatflat.append(spyc[i])
    
    
totalgreendays = len(spygreengreen) + len(spyredgreen) + len(spyflatgreen)
totalreddays = len(spygreenred) + len(spyredred) + len(spyflatred)
totalflatdays = len(spygreenflat) + len(spyredflat) + len(spyflatflat)
    

if (totalgreendays == len(spygreen)):
    print('green days all good')
else:
    print('green days dont add up') 
    print('        total green days are', len(spygreen))
    print('        total green days for comparison are', totalgreendays)
    
    
if (totalreddays == len(spyred)): 
    print('red days all good')
else:
    print('red days dont add up') 
    print('        total red days are', len(spyred))
    print('        total red days for comparison are', totalreddays)
    
    
if (totalflatdays == len(spyflat)):
    print('flat days all good')
else:
    print('flat days dont add up') 
    print('        total flat days are', len(spyflat))
    print('        total flat days for comparison are', totalflatdays)
    
# print('total number of days from comparison are', totalgreendays+totalreddays+totalflatdays)

print('   note: whatever day is off by 1 is what happen on the start date')
    
    
    # values for markov chain matrix

# green day prop (end with 'green')
propstartgreenandendgreen = (len(spygreengreen)/len(spygreen))  # Matrix Position (1,1) for (Row #, Col#)
propstartgreenandendred = (len(spygreenred)/len(spygreen))      # Matrix Position (3,1) for (Row #, Col#)
propstartgreenandendflat = (len(spygreenflat)/len(spygreen))    # Matrix Position (2,1) for (Row #, Col#)

# red day props
propstartredandendgreen = (len(spyredgreen)/len(spyred))        # Matrix Position (1,3) for (Row #, Col#)
propstartredandendred = (len(spyredred)/len(spyred))            # Matrix Position (3,3) for (Row #, Col#)
propstartredandendflat = (len(spyredflat)/len(spyred))          # Matrix Position (2,3) for (Row #, Col#)
    
# flat day props
propstartflatandendgreen = (len(spyflatgreen)/len(spyflat))     # Matrix Position (1,2) for (Row #, Col#)
propstartflatandendred = (len(spyflatred)/len(spyflat))         # Matrix Position (3,2) for (Row #, Col#)
propstartflatandendflat = (len(spyflatflat)/len(spyflat))       # Matrix Position (2,2) for (Row #, Col#)

print('\n')
print('Matrix:  ')
print(propstartgreenandendgreen, propstartflatandendgreen, propstartredandendgreen )
print(propstartgreenandendflat, propstartflatandendflat, propstartredandendflat )
print(propstartgreenandendred, propstartflatandendred, propstartredandendred)



# to see long term trends , find the eiganvector with eiganvalue = 1 (all entries will be (-) but you can multiply by -1)
#       then nomalize this matrix (divide each entry by the total) 
#           to get proportions for desired ticker, dates, and flatness

# finally, the last 3 lines printed will be the rows for your matrix in order
#       note that each column is a probabilty vector, so each column sum should = 1
# using matlab, just let A be a 3x3 matrix with each row given in order from output (add semicolons to each row printed)
# then run command '[P,D] = eig(A)'  which P will give eiganvectors and D their corresponding eiganvalues


# my results are :

#   for SPY:
#   for 1/3/1995 - 6/18/2020:
#   for flat = .001 [1%];  Green days are 46.30%, Flat days are 13.46%, and Red days are 40.24%
#   for flat = .0005 [0.5%];  Green days are 49.82%, Flat days are 6.84%, and Red days are 43.34%


# thanks for looking
# sorry if something is off, I wrote this in 4 hours, and only studied Markov Chains for less than 3 hours for my summer class
# fell free to email me quesitons seanwader@gmail
    
    
    
    
    
    
    
    
    
    
    