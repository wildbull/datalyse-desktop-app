#!/usr/bin/env python3

'''
Entry example which takes any entered text and displays it when the user
presses the button.
'''

import tkinter
import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile
from scipy.interpolate import *
from numpy import *
from matplotlib.pyplot import *
class Entry(tkinter.Tk):
    location="hello"
    order="1"
    regression_type="0"
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Crystall-ball")
        self.geometry("500x500")
        


        self.entry = tkinter.Entry()
        self.entry.pack(fill=tkinter.BOTH, expand=0)
        
        button = tkinter.Button(text="Enter your dataset location", command=self.on_button_click)
        button.pack(fill=tkinter.BOTH, expand=0)

        self.entry1 = tkinter.Entry()
        self.entry1.pack(fill=tkinter.BOTH, expand=0)

        button1 = tkinter.Button(text="regression type", command=self.on_button_click1)
        button1.pack(fill=tkinter.BOTH, expand=0)

        self.entry2 = tkinter.Entry()
        self.entry2.pack(fill=tkinter.BOTH, expand=0)

        button2 = tkinter.Button(text="order in case of polynomial", command=self.on_button_click2)
        button2.pack(fill=tkinter.BOTH, expand=0)

    def on_button_click(self):
        location=self.entry.get()
        print(location)
        x=location
        
 
        df = pd.read_excel(x, sheetname='data')

        #print("Column headings:")
        #print(df.head())
        l1 = df['price'].tolist()

        l3 = df['conversion'].tolist()
        #p1=polyfit(l3,l1,1)
        #p2=polyfit(l3,l1,2)
        #p3=polyfit(l3,l1,5)

        #print(p3)

        plot(l3,l1,'o')
        #plot(l3,polyval(p1,l3),'r-')
        #plot(l3,polyval(p2,l3),'b--')
        #plot(l3,polyval(p3,l3),'m:')
        show()

    def on_button_click1(self):
        regression_type=self.entry1.get()
        print(regression_type)
        n=regression_type
        location=self.entry.get()
        print(location)
        x=location
        if (regression_type=="0"):
            df = pd.read_excel(x, sheetname='data')
            #print("Column headings:")
            #print(df.head())
            l1 = df['price'].tolist()
            l3 = df['conversion'].tolist()
            p1=polyfit(l3,l1,1)
            #p2=polyfit(l3,l1,2)
            #p3=polyfit(l3,l1,5)

            print(p1)

            plot(l3,l1,'o')
            #plot(l3,polyval(p1,l3),'r-')
            #plot(l3,polyval(p2,l3),'b--')
            plot(l3,polyval(p1,l3),'m:')
            show()
           
 
           

        
    def on_button_click2(self):
        location=self.entry.get()
        order=self.entry2.get()
        regression_type=self.entry1.get()
        print(location)
        x=location
        
       
 
        if (regression_type=="1"):
            df = pd.read_excel(x, sheetname='data')

            #print("Column headings:")
            #print(df.head())
            l1 = df['price'].tolist()

            l3 = df['conversion'].tolist()
            #p1=polyfit(l3,l1,1)
            #p2=polyfit(l3,l1,2)
            k=int(order)
            p3=polyfit(l3,l1,k)
            string= ','.join(map(str, p3))

            print(p3)

            plot(l3,l1,'o')
            #plot(l3,polyval(p1,l3),'r-')
            #plot(l3,polyval(p2,l3),'b--')
            plot(l3,polyval(p3,l3),'m:')
            show()
            lfit="%s(%s;%s"%(regression_type,order,string)
            print(lfit)

if __name__ == "__main__":
    application = Entry()
    application.mainloop()


