from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox

#Welcome screen or lobby
#this is the place where user is redirected after login
def wlcm_screen():
    wlcm_scrn = Tk()
    wlcm_scrn.title("The Lezends")
    wlcm_scrn.geometry("511x531")


    file=open(username1, "r")
    lines = file.readlines()
    nme = lines[2]
    
    Label(wlcm_scrn, text="Welcome "+nme, width=329, height=3, font=("agency fb", 20), fg="white",bg="black").pack()
    Label(wlcm_scrn, text="\n").pack()
    Label(wlcm_scrn, text="Thank you for being a part of \"The Lezends\"", font=("@yu gothic lite", "13")).pack()
    Label(wlcm_scrn, text="\"The Lezends\" is a hand crafted application\n for educational purposes.",font=("@yu gothic lite", "13")).pack()
    Label(wlcm_scrn,text="This application is a platform in which users\n of any age, any gender can learn \nanything at any time!",font=("@yu gothic lite", "13")).pack()
    Label(wlcm_scrn,text="Here we have \nSuper calculators for any sums,\nLIY(Learn it yourself),\nblogs and \nforums in which you can ask any question! ",font=("@yu gothic lite", "13")).pack()
    Label(wlcm_scrn, text="Come and join us and explore the app!", font=("@yu gothic lite", "13")).pack()

    Label(wlcm_scrn, text=" ").pack()
 
    Button(wlcm_scrn, text = "Jump In!", font = ("bradley hand itc", "20"), bg = "black", fg = "orange").pack()

#coding to verify credentials
def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            response = messagebox.showinfo("Authentication ", "Login Success!")
            if response == "ok":
                screen2.destroy()
                screen.destroy()
                list_of_files = file1.readlines()
                wlcm_screen()
        else:
            messagebox.showerror("Authentication Error!", "Invaild password!")

    else:
        messagebox.showerror("Authentication Error!", "Username not found!")

#GUI for register screen
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("511x300")

    global username, password, username_entry, password_entry
    global name_user, name_entry
    global value


    username = StringVar()
    password = StringVar()
    name_user = StringVar()
    role_user = StringVar()

    Label(screen1, text="Please enter details below", font=("lucida sans unicode", 16)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Name: ", font=("lucida sans unicode", 12)).pack()
    name_entry = Entry(screen1, textvariable=name_user).pack()
    Label(screen1, text="Username: ", font=("lucida sans unicode", 12)).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Remember that your username is not mail address", font=("calibri", 8)).pack()
    Label(screen1, text="Password: ", font=("lucida sans unicode", 12)).pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
   
    Label(screen1, text = "Choose your Role")

    Button(screen1, text="Register", font=("agency fb", 16), width=9, borderwidth=4, command=register_user).pack()



#coding for registering user
def register_user():
    username_info = username.get()
    password_info = password.get()
    name_info = name_user.get()

    listfiles = os.listdir()
    if username_info in listfiles:
        messagebox.showerror("Registration", "Username Already Exists")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(name_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo("Registration", "Registration Successful!")
        screen1.destroy()
        login()


#GUI for login
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x250")
    Label(screen2, text="Please enter details below to login", font=("HP Simplified", 14)).pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ", font=("felix titling", 10)).pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ", font=("felix titling", 10)).pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

#GUI for the mainscreen
screen = Tk()
screen.title("The Lezends")
screen.geometry("333x459")
Label(screen, text=" ").pack()
Label(screen, text="The Lezends app", width=329, height=3, font=("airways personal use only", 25), fg="white",
      bg="black").pack()
Label(screen, text=" ").pack()
Label(screen, text=" ").pack()
Label(screen, text=" ").pack()
Label(screen, text="Please Login or Register to continue", font=("agency fb", 17)).pack()
Label(screen, text=" ").pack()
Label(screen, text=" ").pack()
Button(screen, text="Login", font=("agency fb", 16), width=11, borderwidth=4, command=login).pack()
Label(screen, text="|", font=("calibri", 8)).pack()
Label(screen, text="or", font=("calibri", 8)).pack()
Label(screen, text="|", font=("calibri", 8)).pack()
Button(screen, text="Register", font=("agency fb", 16), width=13, borderwidth=4, command=register).pack()

screen.mainloop()
