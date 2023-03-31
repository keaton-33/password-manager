import tkinter
import tkinter.messagebox
import generator
import pyperclip
import json

WHITE = "#ffffff"


# new_data being passed in is a tuple containing (website, username, password)
def save(new_data):
    data_dict = {
        new_data[0]: {
            "username": new_data[1],
            "password": new_data[2]
        }
    }

    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            # Creates a new file and saves the data
            json.dump(new_data, file, indent=4)
    else:
        # Updating old data with new data
        data.update(data_dict)
        with open("data.json", "w") as file:
            # Saving updated data
            json.dump(data, file, indent=4)


def find_password(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            tkinter.messagebox.showinfo(title=website,
                                        message=f"Username: {data[website]['username']}\nPassword: {data[website]['password']}")
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="ERROR", message="No data file found")
    except KeyError:
        tkinter.messagebox.showinfo(title="Not Found", message="No details for the website exists")
    else:
        pyperclip.copy(data[website]['password'])


def add_button_clicked(*event):
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        tkinter.messagebox.showwarning(title="Empty Field", message="Please do not leave any fields blank")
    else:
        password_confirmed = tkinter.messagebox.askokcancel(title=website, message=f"Username: {username} \nPassword: {password} \n\nPress OK to save")
        if password_confirmed:
            save((website, username, password))
            website_input.delete(0, 'end')
            username_input.delete(0, 'end')
            username_input.insert(0, "waltonkeaton@gmail.com")
            password_input.delete(0, 'end')


def generate_button_clicked():
    generated_password = generator.generate()
    password_input.delete(0, 'end')
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


def search_button_clicked():
    website = str(website_input.get())

    if len(website) == 0:
        tkinter.messagebox.showerror(title="Empty Field", message="Please type a password to search into the Website field")
    else:
        find_password(website)



window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.bind('<Return>', add_button_clicked)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_pic = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=0, row=0, columnspan=3)

# WEBSITE SECTION #
website_label = tkinter.Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1, stick="e")

website_input = tkinter.Entry(width=25)
website_input.grid(column=1, row=1, sticky="w")
website_input.focus()

# USERNAME SECTION #
username_label = tkinter.Label(text="Email/Username:", font=("Arial", 10, "normal"))
username_label.grid(column=0, row=2, sticky="e")

username_input = tkinter.Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(0, "waltonkeaton@gmail.com")

# PASSWORD SECTION #
password_label = tkinter.Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3, sticky="e")

password_input = tkinter.Entry(width=25)
password_input.grid(column=1, row=3, sticky="w")

# BUTTONS #
generate_button = tkinter.Button(text="Generate", width=7, command=generate_button_clicked)
generate_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=29, command=add_button_clicked)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = tkinter.Button(text="Search", width=7, command=search_button_clicked)
search_button.grid(column=2, row=1, sticky="w")

window.mainloop()
