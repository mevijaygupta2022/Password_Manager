from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- Search Website ------------------------------- #
def find_password():
    website = website_entry.get().lower()
    try:
        file = open("data.json","r")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"There is no record in the File!\nPlease add first!!")
    else:
        data=json.load(file)

        if website in data:
            message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            messagebox.showinfo(title=website ,message=message)
        else:
            messagebox.showinfo(title="Error" ,message=f"No WebSite with the name {website} Found")
        file.close()



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(10, 12)
    nr_symbols = random.randint(5, 8)
    nr_numbers = random.randint(4, 6)

    password_list = []

    # Use List Comprehension
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    #
    random.shuffle(password_list)
    #
    # Use the join method

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website=website_entry.get().lower()
    email= email_entry.get().lower()
    password= password_entry.get().lower()
    # file_name = "data.txt"
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    #Validations
    if len(website) ==0 or len(password) ==0:

        messagebox.showinfo(title="Error" ,message="You should not left any field empty.")

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} "
                                     f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file_save:
                    data=json.load(data_file_save)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file_save:

                    json.dump(new_data, data_file_save, indent=4)

            else:
                with open("data.json","w") as data_file_save:
                    # data_file_save.write(f"{website}|{email}|{password}\n")
                    # # json.dump(new_data,data_file_save,indent=4)
                    # data=json.load(data_file_save)
                    # data.update(new_data)
                    json.dump(data, data_file_save, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0)
password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

#Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(0, "mevijaygupta2010@gmail.com")
password_entry = Entry(width=36)
password_entry.grid(row=4, column=1, columnspan=2)

# Buttons
search_button = Button(text="Search",width=10,command=find_password)
search_button.grid(row=1, column=4)
generate_password_button = Button(text="Generate Password",command=generate_pasword)
generate_password_button.grid(row=4, column=4,ipadx=5)
add_button = Button(text="Add", width=10,command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
