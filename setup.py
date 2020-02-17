# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:57:57 2020

@author: Ayush Gaba
"""
import tkinter as tk
pathtospyder=''

def show_entry_fields(event=None):
    global pathtospyder
    pathtospyder = e1.get()
    w.grid(row=3,column=2)

master = tk.Tk()
master.geometry('300x75') #Setting geometry
tk.Label(master, 
         text="Path to \nspyder shortcut").grid(row=0) # Label for input msg
w = tk.Label(master, text="Path saved!")        #confirmation label
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
master.bind('<Return>',show_entry_fields)       #binding enter to submit
tk.Button(master, 
          text='Submit', command=show_entry_fields).grid(row=3, 
                                                       column=1,  
                                                       pady=4)

tk.mainloop()


pathtospyder+='\\Spyder (Anaconda3)'
print(pathtospyder)

