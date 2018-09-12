
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:09:44 2018

@author: admin
"""
#Import data

import os
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib

#file
filename ='AS1.csv'
locationdata ='E:/Data sci/Data'
os.getcwd()
os.listdir()
os.chdir(locationdata)

df = pd.read_csv(filename,encoding = 'ISO-8859-1')


df.columns
print(df['Data Visualization'].value_counts(dropna=False))
print(df['Machine Learning'].value_counts(dropna=False))
print(df['Data Analysis / Statistics'].value_counts(dropna=False))
print(df['Big Data (Spark / Hadoop)'].value_counts(dropna=False))
print(df['Data Journalism'].value_counts(dropna=False))
print(df['Deep Learning'].value_counts(dropna=False))

df.drop(df.columns[[0]], axis=1, inplace=True)

A = {}
for x in df.columns :
    B = df[x].value_counts(dropna=False)
    
    A[x] = B
    
C = pd.DataFrame(data=A)      
D = C.T
D.drop(D.columns[[-1]], axis=1, inplace=True)

D['Somewhat interested']
D.sort_values(by='Very interested', ascending=False, inplace=True)




matplotlib.rcParams.update({'font.size': 14})
Z =D.plot(kind='bar',figsize=(20,8),width=0.8,color =['#5cb85c','#5bc0de','#d9534f'])
                    
plt.yticks([])
plt.annotate('Percentage of Respondents'' Interest in Data Science Areas',
             xy=(1.2, 1650),size=16)

#for i in range(len(r4)):
#plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 6)
#plt.subplots_adjust(bottom= 0.2, top = 0.98)










#plt.title('Percentage of Respondents'' Interest in Data Science Areas')











