import tkinter
from tkinter import *
from tkinter import messagebox
import pyperclip
import json



import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_numbers)]

    password_list =password_letters + password_symbols +password_numbers



    random.shuffle(password_list)

    password= "" .join(password_list)



    print(f"Your password is: {password}")
    pwd_entry.insert(0, password)
    pyperclip.copy(password)




window =tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)


canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.grid(column=1,row=1)

# Load the image
lock_img = PhotoImage(file="logo.png")

# Add the image to the canvas
canvas.create_image(100, 100, image=lock_img)





def find_password():
    try:
        with open('data.json', 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("File is empty")
            data = json.loads(content)
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified file is not available.")
        #create new file
        with open('data.json', 'w') as file:
            json.dump({}, file)
        messagebox.showinfo("File Created", "A new data.json file has been created.")
    else:
        site = web_entry.get()

        if site in data:
            password_info =data[site]
            messagebox.showinfo(f"{site}",
                                f" The Password for {site} is : {password_info['password']}")

        else:
            messagebox.showerror("Error", "No password found for the specified site.")



web_label =Label(text="Website:")
web_label.grid(column=0,row=2)
web_entry=Entry(width=18,highlightthickness=0)
web_entry.grid(column=1,row=2)



search_button=Button(text="Search", highlightthickness=0,width=13,bg="white", command=find_password)
search_button.grid(column=2,row=2)



def get_data():
    website = web_entry.get()
    username = name_entry.get()
    password = pwd_entry.get()
    new_data =\
        {website:
            {
        "email" : username,
        "password" : password,
    }
               }

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Opps", message=f"You have left some fields empty, PLease fill all blanks ")

    else:
        try:

                #read old data
            with open('data.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
                #updating old data with the new
            data.update(new_data)


            with open("data.json", "w") as file:
            #saving updated data
                json.dump(data, file, indent=4)
        finally:

            web_entry.delete(0, END)
            name_entry.delete(0, END)
            pwd_entry.delete(0, END)
            name_entry.insert(0, "nellymakenakarithi@gmail.com")



name_label =Label(text="Email/Username:",pady=20,padx=10)
name_label.grid(column=0,row=3)
name_entry=Entry(width=35,highlightthickness=0)
name_entry.grid(column=1,row=3,columnspan=2)
name_entry.insert(0, "nellymakenakarithi@gmail.com")

pwd_label =Label(text="Password:",padx=10,pady=20)
pwd_label.grid(column=0,row=4)
pwd_entry=Entry(width=18,highlightthickness=0, )
pwd_entry.grid(column=1,row=4)


gen_button=Button(text="Generate Password", highlightthickness=0,width=13,bg="white",command=generate_password)
gen_button.grid(column=2,row=4)

add_button=Button(text="Add", highlightthickness=0,width=36,bg="white",command=get_data)
add_button.grid(column=1,row=5,columnspan=2)






















window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #