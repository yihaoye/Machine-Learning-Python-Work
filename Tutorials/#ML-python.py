#ML-python

# configurations
#pip install quandl
#pip install pandas
#copyright: youtuber: "sentdex"





#lecture 2 Regression
import pandas as pandas	#
import Quandl #

df = Quandl.get('WIKI/GOOGL')

#print(df.head()) #
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

#
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

#
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
print(df.head())





#lecture 3