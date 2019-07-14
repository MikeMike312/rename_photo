#! \Users\user\~ ANY DIRECTRY
# -*- coding: utf-8 -*
import sys
import os, os.path
#import tkinter as tk

p = input('Enter your name[3 digit](Ex. MZK): ')
n = int(input('Enter Digit (Ex. 3): '))
e = input('Enter Event Name(Party 20190501): ')

'''
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
'''
#push button
def rena():
    temp = 0
    #di = resource_path(".")
    #files = os.listdir(di)
    files = os.listdir(".")
    files.sort(key=os.path.getmtime,reverse=False)
    for i,name in enumerate(files):
        if name.endswith("jpg"):
            temp = temp + 1
            #p = textPre.get()
            d = str(i)
            #n = int(textDigit.get())
            d_zero = d.zfill(n)
            #e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".jpg")
        if name.endswith("JPG"):
            temp = temp + 1
            #p = textPre.get()
            d = str(i)
            #n = int(textDigit.get())
            d_zero = d.zfill(n)
            #e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".JPG")
        if name.endswith("JPEG"):
            temp = temp + 1
            #p = textPre.get()
            d = str(i)
            #n = int(textDigit.get())
            d_zero = d.zfill(n)
            #e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".JPEG")
        if name.endswith("jpeg"):
            temp = temp + 1
            #p = textPre.get()
            d = str(i)
            #n = int(textDigit.get())
            d_zero = d.zfill(n)
            #e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".jpeg")
        if name.endswith("png"):
            temp = temp + 1
            #p = textPre.get()
            d = str(i)
            #n = int(textDigit.get())
            d_zero = d.zfill(n)
            #e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".png")
rena()
'''
#window
win = tk.Tk()
win.title("Rename!")

win.geometry("500x250")

labelPre = tk.Label(win, text=u'Prefix?[3 digit]:')
labelPre.pack()

textPre = tk.Entry(win)
textPre.insert(tk.END, 'MZK')
textPre.pack()

labelDigit= tk.Label(win, text=u'Digit Number?:')
labelDigit.pack()

textDigit = tk.Entry(win)
textDigit.insert(tk.END, '3')
textDigit.pack()

labelEve = tk.Label(win, text=u'Event Name?:')
labelEve.pack()

textEve = tk.Entry(win)
textEve.insert(tk.END, 'chEvent')
textEve.pack()

#labelResult = tk.label(win, text=u'---')
#labelResult.pack()

renaButton = tk.Button(win, text=u'Rename in this Directry!!')
renaButton["command"] = rena
renaButton.pack()

win.mainloop()
'''