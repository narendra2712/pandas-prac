import pandas as pd
import numpy as np
#to read data from csv file
poke = pd.read_csv('Financial Sample.csv')
print(poke.head(2))
#---to read data from xlsx file-----
doke = pd.read_excel("D:\prac\dataset\Financial Sample.xlsx")
print(doke.tail(3))

#---for reading txt file syntax is-----
#pd.read_csv('Financial Sample.csv', delimiter='\t')-----It gives raw data into a table data

print(doke.columns) #To print all the column names
print(doke['Country']) # To get data under specific column in a table
print(doke['Country'][0:3]) # To get range of data under given section
print(doke[['Country', 'Product', 'Profit']][0:3])

print(doke.iloc[1])  #print specific row
print(doke.iloc[697:699])
print(doke.iloc[697:699])

print(doke.iloc[698,1])# print specifc column in specific row

print(doke.loc[doke['Country']=="Canada"]) #loc is used to get the data of specific column having specific value

print(doke.describe())  #describe the mean standard deviation count etc...

print(doke.sort_values('Country')) #Sort data with respect to given parameter

print(doke.sort_values('Country', ascending=False))  #to print sorted data in descending order

print(doke.sort_values(['Country','Product'], ascending=[1,0]))
