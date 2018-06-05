import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile
from scipy.interpolate import *
from numpy import *
from matplotlib.pyplot import *
from entry import Entry
#x=input("enter the date:")
#y=[1,1,1950]
#p=x.split("/")
#n=[None]*3
##n[0]=int(p[0])
#n[1]=int(p[1])
#n[2]=int(p[2])
#print(n)

#print(n)
#k=n[1]-y[0]+(12*(n[2]-y[2]))+1
#print(k)

x=Entry.location
 
df = pd.read_excel('C:\\Users\\Student\\Desktop\\data.xlsx', sheetname='data')

#print("Column headings:")
#print(df.head())
l1 = df['price'].tolist()

l3 = df['conversion'].tolist()
p1=polyfit(l3,l1,1)
p2=polyfit(l3,l1,2)
p3=polyfit(l3,l1,5)

print(p3)

plot(l3,l1,'o')
#plot(l3,polyval(p1,l3),'r-')
#plot(l3,polyval(p2,l3),'b--')
plot(l3,polyval(p3,l3),'m:')
show()

yfit=polyval(p3,l3)
#yfit=p3[0]+(p3[1]*l3)+(p3[2]*pow(l3,2))+(p3[3]*pow(l3,3))
#print(yfit)



