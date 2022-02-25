from tkinter import *

def miles_to_km():
    miles=float(entry_miles.get())
    km=miles*1.609
    label_km_result.config(text=f"{km}")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=250,height=150)
window.config(padx=20,pady=20)

entry_miles=Entry(width=7)
entry_miles.grid(column=1,row=0)
entry_miles.config()


button_calculate=Button(text="Calculate",command=miles_to_km)
button_calculate.grid(row=2,column=1)

label_miles=Label(text="Miles")
label_miles.grid(column=2,row=0)

label_equal=Label(text="is equal to")
label_equal.grid(column=0,row=1)
label_equal.config(pady=20)

label_km_result=Label(text="0")
label_km_result.grid(column=1,row=1)

label_km=Label(text="Km")
label_km.grid(column=2,row=1)











window.mainloop()