#! \Users\user\
# -*- coding: utf-8 -*

import os, os.path
import tkinter as tk

#push button
def rena():
    files = os.listdir(".")
    files.sort(key=os.path.getmtime,reverse=False)
    for i,name in enumerate(files):
        if name.endswith("jpg"):
            p = textPre.get()
            d = str(i)
            n = int(textDigit.get())
            d_zero = d.zfill(n)
            e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".jpg")
        if name.endswith("jpeg"):
            p = textPre.get()
            d = str(i)
            n = int(textDigit.get())
            d_zero = d.zfill(n)
            e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".jpeg")
        if name.endswith("png"):
            p = textPre.get()
            d = str(i)
            n = int(textDigit.get())
            d_zero = d.zfill(n)
            e = textEve.get()
            os.rename(name,p+d_zero+"_"+e+".png")
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