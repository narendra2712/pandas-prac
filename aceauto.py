"""n=[]
p=int(input("enter p"))
for i in range (p):

    name=input("enter name")
    mail=input("enter mail")
    thisdict = ({
        "name": name,
        "mail": mail,
    })
print(thisdict)"""

'''import numpy as np
import pandas as pd
mydata= pd.read_excel("D:\prac\dataset\Financial Sample.xlsx")
ser1=pd.Series(mydata)
print(ser1)'''
#merge two dictionaries
a={'v':1,'d':2}
b={'e':4,'f':5}
c={**a,**b}
print(c)