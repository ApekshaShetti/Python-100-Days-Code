from tkinter import *

def buttonClicked():
    print("I got clicked")
    new_text=entry.get()
    label.config(text=new_text)

window=Tk()
window.title("Conversion")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)     

# Label
label=Label(text="I am label",font=("Arial",24,"bold"))
label["text"]="New Text"
label.config(text="New Text")
# label.pack()
# label.place(x=170,y=0)
label.grid(column=0,row=0)

# Button
button=Button(text="Click Me!",command=buttonClicked)
# button.pack()
button.grid(column=1,row=1)

button2=Button(text="Click Me Again!")
button2.grid(column=2,row=0)

# Entry
entry=Entry(width=10)
print(entry.get())
# entry.pack()
entry.grid(column=3,row=3)





window.mainloop()