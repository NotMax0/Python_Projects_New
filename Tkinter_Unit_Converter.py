import tkinter
from tkinter import *

root = Tk()
root.geometry("500x550")
root.title("Metric Calculator")

photo = PhotoImage(file='calculator.png')
root.wm_iconphoto(False, photo)

frame = LabelFrame(
    root,
    text='Meter to/from Foot',
    bg='#f0f0f0',
    font=("Lucida Console", 10)

)
frame.pack(expand=True, fill=BOTH)

def clickme():
    if x.get() == 0:
        try:
            cal = float(e.get()) * 3.28084
        except ValueError:
            myLabel.config(text="Unappropriate  input...\nInput must be a Number")
        myLabel.config(text="%s meter >> %.2f foot" %(e.get(), cal))
    else:
        try:
            cal = float(e.get()) * 0.3048
        except ValueError:
            myLabel.config(text="Unappropriate  input...\nInput must be a Number")
        myLabel.config(text="%s foot >> %.2f meter" %(e.get(), cal))

myLabel1 = tkinter.Label(frame, text="Converter...")
myLabel1.pack()

e = tkinter.Entry(frame, width=30, borderwidth=10, relief=tkinter.FLAT)
e.pack()
e.insert(0, "Num")

x = IntVar()
to_foot = Radiobutton(frame, text="to Foot", variable=x, value=0)
to_foot.pack()
to_meter = Radiobutton(frame, text="to Meter", variable=x, value=1)
to_meter.pack()

myButton = Button(frame, text="Calculate", command=clickme, padx=5, pady=5)
myButton.pack()

myLabel = Label(frame, font=("Helvetica", 12, "bold"), fg="#666",
                       borderwidth=15, relief=tkinter.FLAT)
myLabel.pack()

frame.mainloop()
