import tkinter as tk

import tkinter                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):
    path="hello"
    regression_type=0
    order=1

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="enter the path of your data-set", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        self.entry = tkinter.Entry()
        self.entry.pack(fill=tkinter.BOTH, expand=0)

        button1 = tk.Button(self, text="load",
                            command=self.on_button_click )
        button1.pack()
        # button2.pack()
    def on_button_click(self):
        location=self.entry.get()
        self.controller = controller
        print(location)
        x=location
        controller.show_frame("PageOne")
 
        df = pd.read_excel(x, sheetname='data')

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
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
       


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()