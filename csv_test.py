#from sys import argv
#script , date = argv
#print ('date')
import pandas as pd
import numpy as np
df=pd.read_csv('backupall.csv')
headers = ["Febin" , "Status" , "Level"]
#x1 = df.parse("Status")
#Total_Backup = df.count()
#print ('Total_Backup' is df['Full'].value_counts())
df1=df.dropna()
ReqFields = df1[['Status']]
#print (ReqFields)
#print (df[['Started', 'Status','Level']])
Total_Backup = (df['Full'].value_counts())
print (Total_Backup)
#for x in (df[['Started', 'Status','Level']]):
#print ('Level')
#for 'Status' in df:
	#Details = (df[['Started', 'Status','Level']])
	#print (Details)
#o = ReqFields.sort_values('Started',ascending=True)
#print (o)

#for success in 'ReqFields'
#	print (o.count())
#pandas.core.series.Series
#print (df.count())
output = (df['Status'].value_counts())
#print (pd.to_csv('result.csv)
#print (output)
#Total_Backup = df.groupby (
#print (Total_Backup)
print (output.to_csv('result.csv'))

