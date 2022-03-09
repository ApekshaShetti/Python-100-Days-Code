from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    l = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    s = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    letters = random.randint(8,10)
    symbols = random.randint(2,4)
    numbers = random.randint(2,4)

    password_letters = [random.choice(l) for _ in range(letters)]
    password_symbols=[random.choice(s) for _ in range(symbols)]
    password_numbers=[random.choice(n) for _ in range(numbers)]

    password_list= password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message=f"Please don't leave any fields empty!")
    else:
        # messagebox.showinfo(title="Title",message="Message")
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nDo you want to save it?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    
    




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"apekshashetti1012@gmail.com")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry=Entry(width=20)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()