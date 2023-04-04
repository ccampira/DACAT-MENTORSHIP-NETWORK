import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from classes import BookHotel
from os import path
from time import strftime
import json
import csv


f = open('mentors.json')
mentors_accounts = json.load(f)
f.close()

f1 = open('mentees.json')
mentees_accounts = json.load(f1)
f1.close()


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Dwayne Johnson's Mentor Profile")
        self.geometry("800x550")
        rock_frame = Frame(self, bg='white', width=800, height=600)
        rock_frame.grid(row=0, column=0)

        buttonRock1 = tkinter.Button(rock_frame, image=theRock)
        buttonRock1.grid(row=1, column=0, pady=30, padx=5)
        rock_label1 = Label(rock_frame, text=f'Dwayne Johnson', font=('Bodoni MT', 20),
                           bg='white')
        rock_label1.grid(row=2, column=0, pady=10, padx=5)
        rock_label2 = Label(rock_frame, text=f'Major: Computer Information Systems', font=('Bodoni MT', 20),
                           bg='white')
        rock_label2.grid(row=3, column=0, pady=10, padx=5)
        rock_label3 = Label(rock_frame, text=f'Hi My names Dwayne, a current professional in the industry of software development\n'
                                             f'I am eager to mentor and teach incoming ASU professionals or Alumni\n'
                                             f'I have over 10 years of experience in development and would love to share\n'
                                             f'what I have learned over the past 10 years with you!', font=('Bodoni MT', 16),
                           bg='white')
        rock_label3.grid(row=4, column=0, pady=30, padx=20)


        # label = Label(self, text="Hi My names Dwayne, a current professional in the industry")

class NewWindow1(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Mark Walhberg's Mentor Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Mark, a current professional in the industry")
        label.grid()

class NewWindow2(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Mark Zuckerberg Mentor's Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Mark, a current professional in the industry")
        label.grid()

class NewWindow3(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Natalie Portman's Mentor Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Natalie, a current professional in the industry")
        label.grid()

class NewWindow4(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Bill Gates' Mentor Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Bill, a current professional in the industry")
        label.grid()


class NewWindow5(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Mentor Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Jake, a current professional in the industry")
        label.grid()

def show_time():
    time = strftime("%H:%M:%S")
    date = strftime('%Y/%m/%d')
    set_text = f"{time} \n {date}"
    date_time.configure(text=set_text, font=("Calibri", 15, "bold"), bg="black", fg="white")
    date_time.after(100, show_time)
def mentor_login():
    try:
        result = any(mentor_password_entry.get() in d.values() for d in mentors_accounts.values())
        if mentor_username_entry.get() not in mentors_accounts or result is False:
            mentor_message_label.config(
                text=f'{mentor_username_entry.get()} is not in our system. Please create an account or try again.')
        else:
            # bg_label.grid_forget()
            box1.grid_forget()
            mentor_message_label.config(text=" ")
            mentor_welcomepg.grid()
    except AttributeError:
        mentor_message_label.config(text=f'{mentor_username_entry.get()}, your password is incorrect. Please try again.')


def mentee_login():
    try:
        result = any(mentee_password_entry.get() in d.values() for d in mentees_accounts.values())
        if mentee_username_entry.get() not in mentees_accounts or result is False:
            mentee_message_label.config(
                text=f'{mentee_username_entry.get()} is not in our system. Please create an account or try again.')
        else:
            # bg_label.grid_forget()
            mentee_login_page.grid_forget()
            mentee_message_label.config(text=" ")
            mentee_welcomepg.grid()
            # sidebarFrame.grid(row=0, column=0, columnspan=1, sticky=N)
            editProfile_button.grid(row=0, column=0,pady=8, sticky=N)
            logout_button.grid(row=0, column=0, pady=8, sticky=NE)
            date_time.grid(row=0, column=0, pady=10,padx=8, sticky=NW)
            show_time()

    except AttributeError:
        mentee_message_label.config(text=f'{mentee_username_entry.get()}, your password is incorrect. Please try again.')


def add_new_mentor():

    mentor_newusername = mentor_newusername_textbox.get()
    mentor_newpassword = mentor_newpassword_textbox.get()
    mentor_email = mentor_email_textbox.get()

    mentors_accounts[mentor_newusername] = dict()
    mentors_accounts['Username'] = mentor_newusername
    mentors_accounts[mentor_newusername]['Password'] = mentor_newpassword
    mentors_accounts[mentor_newusername]['Email'] = mentor_email

    with open('mentors.json', 'w', newline='') as f:
        json.dump(mentors_accounts, f)

    mentor_create_label.config(text=f'Thank you {mentor_newusername}, your Mentor account has been created!')
    buttonavatar = tkinter.Button(mentor_list_box, image=ava)
    buttonavatar.bind("<Button>", lambda e: NewWindow5(mentor_list_box))
    buttonavatar.grid(row=3, column=0, sticky=E)
    avatar_label = Label(mentor_list_box, text=f'Computer Information Systems', font=('Bodoni MT', 12),
                         bg='white')
    avatar_label.grid(row=4, column=0, sticky=E)


def add_new_mentee():

    mentee_newusername = mentee_newusername_textbox.get()
    mentee_newpassword = mentee_newpassword_textbox.get()
    mentee_email = mentee_email_textbox.get()

    mentees_accounts[mentee_newusername] = dict()
    mentees_accounts['Username'] = mentee_newusername
    mentees_accounts[mentee_newusername]['Password'] = mentee_newpassword
    mentees_accounts[mentee_newusername]['Email'] = mentee_email

    with open('mentees.json', 'w', newline='') as f1:
        json.dump(mentees_accounts, f1)

    mentee_create_label.config(text=f'Thank you {mentee_newusername}, your Mentee account has been created!')


def choose_mentor():
    intro_page.grid_forget()
    box.grid_forget()
    mentor_login_page.grid()
    mentor_login_page.columnconfigure(0, weight=1)
    box2.grid(row=0, column=0)


def choose_mentee():
    intro_page.grid_forget()
    box.grid_forget()
    mentee_login_page.grid()
    mentee_login_page.columnconfigure(0, weight=1)
    box1.grid(row=0, column=0)


def back_mentee():
    mentee_login_page.grid_forget()
    box1.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    intro_page.grid()
    box.grid(row=0, column=0)
    mentee_message_label.config(text=" ")


def back_mentor():
    mentor_login_page.grid_forget()
    box2.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    intro_page.grid()
    box.grid(row=0, column=0)
    mentor_message_label.config(text=" ")


def create_mentee_account():
    mentee_login_page.grid_forget()
    box1.grid_forget()
    # page_two.grid_forget()
    # page_three.grid_forget()
    mentee_account_page.grid()
    mentee_account_page.columnconfigure(0, weight=3)
    # bg_labelACC.grid(rowspan=4, columnspan=1)
    create_box.grid(row=0, column=0)


def create_mentor_account():
    mentor_login_page.grid_forget()
    box2.grid_forget()
    # page_two.grid_forget()
    # page_three.grid_forget()
    mentor_account_page.grid()
    mentor_account_page.columnconfigure(0, weight=3)
    # bg_labelACC.grid(rowspan=4, columnspan=1)
    # create_box.grid(row=0, column=0)


def mentee_back_to_login():
    mentee_account_page.grid_forget()
    mentee_login_page.grid()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box1.grid(row=0, column=0)


def mentor_back_to_login():
    mentor_account_page.grid_forget()
    mentor_login_page.grid()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box2.grid(row=0, column=0)

def select_button_click():
    mentee_welcomepg.grid_forget()
 #    page_three.grid()
 #    page_three.columnconfigure(0, weight=3)

# def logout():
    # page_three.grid_forget()
    # final_page.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    # box1.grid(row=0, column=0)


# def final():
    # page_three.grid_forget()
    # final_page.grid()
    # final_page.columnconfigure(0, weight=3)

def close():
    window.destroy()


# def next_button_click():
    # page_two.grid_forget()
    # page_three.grid()
    # page_three.columnconfigure(0, weight=3)




window = Tk()
window.geometry('1280x800')
window.title('DA CAT')
window.config(bg='#f0f0f0')
window.resizable(1, 0)

menubar = Menu(window)  # add a menu to window object/instance

filemenu = Menu(menubar)  # add File menu and commands
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
filemenu.add_command(label='Exit', command=window.quit)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

window.columnconfigure(0, weight=1)

# background Image
# bg_img = Image.open('wallpaper.jpg')
# new_width = 1280
# new_height = 800
# wallpaper = bg_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
# wallpaper.save('wallpaper.jpg')
# bg = ImageTk.PhotoImage(wallpaper)
# bg_label = Label(window, image=bg)
# bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)

######################################################################################################################


############################################################################################################ INTRO PAGE
intro_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
intro_page.grid()
# intro Image
intro_img = Image.open('whiteBackground.jpg')
new_width = 1280
new_height = 800
wallpaper = intro_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
wallpaper.save('whiteBackground.jpg')
bg = ImageTk.PhotoImage(wallpaper)
bg_label = Label(intro_page, image=bg)
bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)

box = Frame(intro_page, bg='white', width=400, height=200)
box.grid(row=0, columnspan=4)
# box.grid_propagate(False)

title_label = Label(box, text='Mentor Program', width=20, font=('Bodoni MT', 24, 'bold'), fg='black', bg='#fbfbfb')
title_label.grid(columnspan=4, row=1, column=0)

choose_label = Label(box, text='Choose your Role', width=20, font=('Bodoni MT', 20, 'bold'), fg='black', bg= 'white')
choose_label.grid(columnspan=4, row=2, column=0, pady=10)

mentee_button = Button(box, font=("Bodoni MT", 12), text='MENTEE', width=10, command=choose_mentee, relief=FLAT, bg='black',
                       fg='white')
mentee_button.grid(row=3, column=0, pady=10, columnspan=4)

mentor_button = Button(box, font=("Bodoni MT", 12), text='MENTOR', width=10, command=choose_mentor, relief=FLAT, bg='black',
                       fg='white')
mentor_button.grid(row=4, column=0, pady=10, columnspan=4)
###################################################################################################### INTRO PAGE ENDS





######################################################################################################## MENTEE PAGES

# Configure variables
mentee_username = StringVar()
mentee_password = StringVar()


# Mentee Login PAGE
mentee_login_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
# mentee_login_page.grid()
mentee_login_img = Image.open('whiteBackground.jpg')
new_width2 = 1280
new_height2 = 800
wallpaper2 = mentee_login_img.resize((new_width2, new_height2), Image.Resampling.LANCZOS)
wallpaper2.save('whiteBackground.jpg')
bg2 = ImageTk.PhotoImage(wallpaper2)
bg_label2 = Label(mentee_login_page, image=bg2)
bg_label2.grid(row=0, column=0, rowspan=2, columnspan=1)

# FRAME WITH USERNAME & PASSWORD
box1 = Frame(mentee_login_page, bg='#fbfbfb', width=500, height=500)
box1.grid(row=0, columnspan=3)


# LOG IN TO YOUR ACCOUNT MESSAGE
mentee_label = Label(box1, text='Mentee\n Login to your Account', font=('Bodoni MT', 20, 'bold'), fg='black', bg='#fbfbfb')
mentee_label.grid(columnspan=4, row=1, column=0)

# Login_label = Label(box1, text='Login to your Account', width=40, font=('Open Sans', 14), fg='black', bg= 'white')
# Login_label.grid(row=2)

mentee_message_label = Label(box1, justify=CENTER, font=('Bodoni MT', 10), bg='#fbfbfb', wraplength=210)
mentee_message_label.grid(columnspan=3, row=2, column=0)

# label for username and password
mentee_username_label = Label(box1, text='Username', fg='black', font=('Calibri', 12, 'bold'), bg='#fbfbfb')
mentee_username_label.grid(columnspan=1, row=3, column=0, pady=20)
mentee_password_label = Label(box1, font=('Calibri', 12, 'bold'), text='Password', bg='white')
mentee_password_label.grid(columnspan=1, row=4, column=0)

# # BOX 1, USER & PASSWORD ENTRY BOXES
mentee_username_entry = Entry(box1, textvariable=mentee_username, justify=LEFT, width=20, font=('Bodoni MT', 11), bg='#fbfbfb')
mentee_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentee_password_entry = Entry(box1, textvariable=mentee_password, justify=LEFT, width=20, font=('Bodoni MT', 11), show="*", bg='#fbfbfb')
mentee_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentee_login_button = Button(box1, command=mentee_login, font=('Bodoni MT', 12), text='Log In',
                        relief=FLAT, bg='#135fca', fg='white', width=10)
mentee_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

#contact button
back_button = Button(box1, font=('Bodoni MT', 12), text='Back',
                        fg='black', width=8, command=back_mentee, relief="groove")
back_button.grid(row=7,column=0, pady=10, padx=10)

#create account button
newMentee_button = Button(box1, command=create_mentee_account, font=('Bodoni MT', 12), text='New Mentee',
                        fg='black', relief="groove")
newMentee_button.grid(row=7, column=1, sticky=E, pady=10, padx=10)


################################################################################### CREATE MENTEE ACCOUNT PAGE

mentee_account_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
# mentee_account_page.grid()
mentee_account_img = Image.open('whiteBackground.jpg')
new_width3 = 1280
new_height3 = 800
wallpaper3 = mentee_account_img.resize((new_width3, new_height3), Image.Resampling.LANCZOS)
wallpaper3.save('whiteBackground.jpg')
bg3 = ImageTk.PhotoImage(wallpaper3)
bg_label3 = Label(mentee_account_page, image=bg3)
bg_label3.grid(row=0, column=0, rowspan=2, columnspan=1)

# frame
create_box = Frame(mentee_account_page, bg='#fbfbfb', width=600, height=630, relief=FLAT)
create_box.grid(row=0, column=0, columnspan=3, pady=3)
create_box.grid_propagate(False)
create_box.columnconfigure(0, weight=1)
create_box.columnconfigure(1, weight=1)
create_box.columnconfigure(2, weight=1)

Login_label = Label(create_box, text='Create Your Mentee Account', width=40, font=('Bodoni MT', 20), fg='black', bg='#fbfbfb')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb', fg='black')
newusername_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newusername_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_newusername_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb', fg='black')
newpassword_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_newpassword_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb', fg='black')
email_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_email_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_email_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)

mentee_q1_label = Label(create_box, text='\nWhat are you looking for in a mentor?', justify=CENTER, font=('Bodoni MT', 12),
                        bg='#fbfbfb', fg='black')
mentee_q1_label.grid(row=4, column=0, pady=5, padx=100, columnspan=3)


blank_label = Label(create_box, text='\n\n\n ', width=60, bg='#fbfbfb', font=('Calibri', 12), fg='black')
blank_label.grid(row=5, column=0, pady=30, columnspan=3)

mentee_q1_entry = Text(create_box, font=('Calibri', 12), height=30)
mentee_q1_entry.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)
# mentee_q1_entry.grid(row=5, column=0, pady=5, columnspan=3, padx=30)


create_button = Button(create_box, font=('Bodoni MT', 12), text='Create', width=10, command=add_new_mentee, relief=FLAT,
                       bg='#135fca', fg='white')
create_button.grid(column=0, row=7, pady=30, columnspan=3)

mentee_create_label = Label(create_box, text=' ', width=60, bg='#fbfbfb', font=('Bodoni MT', 12), fg='black')
mentee_create_label.grid(row=8, column=0, pady=30, columnspan=3)

home_button = Button(create_box, command=mentee_back_to_login, font=('Bodoni MT', 12), text='Back to Login',
                       fg='black', relief="groove")
home_button.grid(row=9, column=0, columnspan=3)


############################################################### MENTEE WELCOME
mentee_welcomepg = Frame(window, width=1280, height=800, borderwidth=1)

mentor_selection_img = Image.open('whiteBackground.jpg')
new_width6 = 1280
new_height6 = 800
wallpaper6 = mentor_selection_img.resize((new_width6, new_height6), Image.Resampling.LANCZOS)
wallpaper6.save('whiteBackground.jpg')
bg6 = ImageTk.PhotoImage(wallpaper6)
bg_label6 = Label(mentee_welcomepg, image=bg6)
bg_label6.grid(row=0, column=0, rowspan=2, columnspan=1)

mentor_list_box = Frame(mentee_welcomepg, bg='white', width=450, height=300, borderwidth=2, relief=RAISED)
mentor_list_box.grid(row=0, column=0)

rock = Image.open('rock.jpg')
new_width4 = 200
new_height4 = 200
rock2 = rock.resize((new_width4, new_height4), Image.Resampling.LANCZOS)
rock2.save('rock.jpg')
theRock = ImageTk.PhotoImage(rock)

wahlberg = Image.open('mark.jpg')
new_width5 = 200
new_height5 = 200
wahlberg2 = wahlberg.resize((new_width5, new_height5), Image.Resampling.LANCZOS)
wahlberg2.save('mark.jpg')
mwahlberg = ImageTk.PhotoImage(wahlberg2)

zuck = Image.open('markZuck.jpg')
new_width6 = 200
new_height6 = 200
zuck2 = zuck.resize((new_width6, new_height6), Image.Resampling.LANCZOS)
zuck2.save('markZuck.jpg')
zuckerberg = ImageTk.PhotoImage(zuck2)

nat = Image.open('nat.jpg')
new_width7 = 200
new_height7 = 200
nat2 = nat.resize((new_width7, new_height7), Image.Resampling.LANCZOS)
nat2.save('nat.jpg')
portman = ImageTk.PhotoImage(nat2)

bill = Image.open('bill.jpg')
new_width8 = 200
new_height8 = 200
bill2 = bill.resize((new_width8, new_height8), Image.Resampling.LANCZOS)
bill2.save('bill.jpg')
gates = ImageTk.PhotoImage(bill2)

avatar = Image.open('avatar.jpeg')
new_width9 = 200
new_height9 = 200
avatar2 = avatar.resize((new_width9, new_height9), Image.Resampling.LANCZOS)
avatar2.save('avatar.jpeg')
ava = ImageTk.PhotoImage(avatar2)

description = "The Rock"
var = StringVar(window, "1")

welcome_label = Label(mentor_list_box, text=f'Welcome to DACAT Mentorship Network.', font=('Bodoni MT', 40),
                      bg='white')
welcome_label.grid(row=0, column=0,sticky=W)

buttonRock = tkinter.Button(mentor_list_box, image=theRock)
buttonRock.bind("<Button>", lambda e: NewWindow(mentor_list_box))
buttonRock.grid(row=1, column=0, sticky=W)
rock_label = Label(mentor_list_box, text=f'Major: Computer Information Systems', font=('Bodoni MT', 12),
                      bg='white')
rock_label.grid(row=2, column=0, sticky=W)

buttonZuck = tkinter.Button(mentor_list_box, image=zuckerberg)
buttonZuck.bind("<Button>", lambda e: NewWindow2(mentor_list_box))
buttonZuck.grid(row=1, column=0)
zuck_label = Label(mentor_list_box, text=f'Major: Computer Science & Management', font=('Bodoni MT', 12),
                      bg='white')
zuck_label.grid(row=2, column=0)

buttonNat = tkinter.Button(mentor_list_box, image=portman)
buttonNat.bind("<Button>", lambda e: NewWindow3(mentor_list_box))
buttonNat.grid(row=1, column=0, sticky=E)
nat_label = Label(mentor_list_box, text=f'Major: Finance & Data Analytics', font=('Bodoni MT', 12),
                      bg='white')
nat_label.grid(row=2, column=0, sticky=E)

buttonwalhberg = tkinter.Button(mentor_list_box, image=mwahlberg)
buttonwalhberg.bind("<Button>", lambda e: NewWindow1(mentor_list_box))
buttonwalhberg.grid(row=3, column=0, sticky=W)
walhberg_label = Label(mentor_list_box, text=f'Software Development & Communications', font=('Bodoni MT', 12),
                      bg='white')
walhberg_label.grid(row=4, column=0, sticky=W)

buttonbill = tkinter.Button(mentor_list_box, image=gates)
buttonbill.bind("<Button>", lambda e: NewWindow4(mentor_list_box))
buttonbill.grid(row=3, column=0)
bill_label = Label(mentor_list_box, text=f'Computer Information Systems', font=('Bodoni MT', 12),
                      bg='white')
bill_label.grid(row=4, column=0)






editProfile_button = Button(window, font=('Bodoni MT', 17), text='Edit User Profile',
                       fg='black')
logout_button = Button(window, font=('Bodoni MT', 17), text='Log Out',
                       fg='black')
date_time = Label(window)

# page1text = tkinter.Label(window, text="This is page 1")
# page2text = tkinter.Label(window, text="this is page 2")
# buttonRock.pack()
# page1text.pack()


# r1 = Radiobutton(box3, text=description, variable=var, value='rock', image=physical, font=('Impact', 40))
# r1.grid(row=3, column=0, sticky=W)
# rock_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='ROCK')
# rock_lbl.grid(row=4, column=0, sticky=W, padx=70)
# r2 = Radiobutton(box3, text='walhberg', variable=var, value='walhberg', image=accounting, font=('Impact', 40))
# r2.grid(row=3, column=0, sticky=W, padx=250)
# walhberg_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='WALHBERG')
# walhberg_lbl.grid(row=4, column=0, sticky=W, padx=70)
# r3 = Radiobutton(box3, text='zuck', variable=var, value='zuck', image=compsci, font=('Impact', 40))
# r3.grid(row=3, column=0, sticky=W, padx=500)
# zuck_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text='ZUCK')
# zuck_lbl.grid(row=4, column=0, sticky=W, padx=70)
# r4 = Radiobutton(box3, text=description, variable=var, value='nat', image=science, font=('Impact', 40))
# r4.grid(row=3, column=0, sticky=W, padx=750)
# nat_lbl = Label(box3, justify=CENTER, font=('Impact', 30), bg='white', text=description)
# nat_lbl.grid(row=4, column=0, sticky=W, padx=70)



# select button
select_button = Button(mentor_list_box, command=select_button_click, font=('Bodoni MT', 20), text='Select',
                       relief=GROOVE, bg='black', fg='white')
select_button.grid(row=5, column=0, columnspan=3)
###################################################################################################### MENTEE PAGES END


########################################################################################################### MENTOR PAGES
# Configure variables
mentor_username = StringVar()
mentor_password = StringVar()


# Mentor Login Page
mentor_login_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
# mentor_login_page.grid()
mentor_login_img = Image.open('whiteBackground.jpg')
new_width4 = 1280
new_height4 = 800
wallpaper4 = mentor_login_img.resize((new_width4, new_height4), Image.Resampling.LANCZOS)
wallpaper4.save('whiteBackground.jpg')
bg4 = ImageTk.PhotoImage(wallpaper4)
bg_label4 = Label(mentor_login_page, image=bg4)
bg_label4.grid(row=0, column=0, rowspan=2, columnspan=1)


# FRAME WITH USERNAME & PASSWORD
box2 = Frame(mentor_login_page, bg='white', width=500, height=500)
box2.grid(row=0, columnspan=5)

# LOG IN TO YOUR ACCOUNT MESSAGE
mentor_label = Label(box2, text='Mentor\n Login to your Account', font=('Bodoni MT', 20, 'bold'), fg='black', bg= 'white')
mentor_label.grid(columnspan=4, row=1, column=0)

# Login_label = Label(box2, text='Login to your Account', width=40, font=('Open Sans', 14), fg='black', bg= 'white')
# Login_label.grid(row=2)

mentor_message_label = Label(box2, justify=CENTER, font=('Bodoni MT', 10), bg='white', wraplength=210)
mentor_message_label.grid(columnspan=3, row=2, column=0)

# label for username and password
mentor_username_label = Label(box2, text='Username', fg='black', font=('Calibri', 12), bg='white')
mentor_username_label.grid(columnspan=1, row=3, column=0, pady=20)
mentor_password_label = Label(box2, font=('Calibri', 12), text='Password', bg='white')
mentor_password_label.grid(columnspan=1, row=4, column=0)

# # BOX 1, USER & PASSWORD ENTRY BOXES
mentor_username_entry = Entry(box2, textvariable=mentor_username, justify=LEFT, width=20, font=('Calibri', 11))
mentor_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentor_password_entry = Entry(box2, textvariable=mentor_password, justify=LEFT, width=20, font=('Calibri', 11), show="*")
mentor_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentor_login_button = Button(box2, command=mentor_login, font=('Bodoni MT', 12), text='Log In',
                        relief=FLAT, bg='#ffa440', fg='white', width=10)
mentor_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

#contact button
back_button = Button(box2, font=('Bodoni MT', 12), text='Back',
                        fg='black', width=8, command=back_mentor, relief="groove")
back_button.grid(row=7,column=0, pady=10, padx=10)

#create account button
newMentor_button = Button(box2, command=create_mentor_account, font=('Bodoni MT', 12), text='New Mentor',
                        fg='black', relief="groove")
newMentor_button.grid(row=7, column=1, sticky=E, pady=10, padx=10)

#################################################################################### CREATE MENTOR ACCOUNT PAGE
mentor_account_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
# mentor_account_page.grid()
mentor_account_img = Image.open('whiteBackground.jpg')
new_width5 = 1280
new_height5 = 800
wallpaper5 = mentor_account_img.resize((new_width5, new_height5), Image.Resampling.LANCZOS)
wallpaper5.save('whiteBackground.jpg')
bg5 = ImageTk.PhotoImage(wallpaper5)
bg_label5 = Label(mentor_account_page, image=bg5)
bg_label5.grid(row=0, column=0, rowspan=2, columnspan=1)

# frame
create_box = Frame(mentor_account_page, bg='white', width=600, height=630, relief=FLAT)
create_box.grid(row=0, column=0, columnspan=3, pady=3)
create_box.grid_propagate(False)
create_box.columnconfigure(0, weight=1)
create_box.columnconfigure(1, weight=1)
create_box.columnconfigure(2, weight=1)

Login_label = Label(create_box, text='Create Your Mentor Account', width=40, font=('Bodoni MT', 20), fg='black', bg= 'white')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Calibri', 12), bg='white', fg='black')
newusername_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newusername_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_newusername_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Calibri', 12), bg='white', fg='black')
newpassword_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_newpassword_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Calibri', 12), bg='white', fg='black')
email_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_email_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_email_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)


mentor_q1_label = Label(create_box, text='\nWhat can you provide as a mentor?', justify=CENTER, font=('Bodoni MT', 12),
                        bg='white', fg='black')
mentor_q1_label.grid(row=4, column=0, pady=5, padx=100, columnspan=3)


blank_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Calibri', 12), fg='black')
blank_label.grid(row=5, column=0, pady=30, columnspan=3)

mentee_q1_entry = Text(create_box, font=('Arial', 12), height=30)
mentee_q1_entry.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)
# mentee_q1_entry.grid(row=5, column=0, pady=5, columnspan=3, padx=30)

create_button = Button(create_box, font=("Bodoni MT", 12), text='Create', width=10, command=add_new_mentor, relief=FLAT,
                       bg='#ffa440', fg='white')
create_button.grid(column=0, row=7, pady=30, columnspan=3)

mentor_create_label = Label(create_box, text=' ', width=60, bg='white', font=('Calibri', 12), fg='black')
mentor_create_label.grid(row=8, column=0, pady=30, columnspan=3)

home_button = Button(create_box, command=mentor_back_to_login, font=('Bodoni MT', 12), text='Back to Login',
                       fg='black', relief="groove")
home_button.grid(row=9, column=0, columnspan=3)

################################################### MENTOR WELCOME
mentor_welcomepg = Frame(window, bg='black', width=1920, height=1080)

# # Background IMAGE
# bg2_img = Image.open('wallpaper2.jpg')
# new_width2 = 1280
# new_height2 = 800
# wallpaper2 = bg2_img.resize((new_width2, new_height2), Image.Resampling.LANCZOS)
# wallpaper2.save('wallpaper2.jpg')
# bg2 = ImageTk.PhotoImage(wallpaper2)
# bg_label2 = Label(page_two, image=bg2)
# bg_label2.grid(rowspan=4, columnspan=1)
# bg_label2.grid_propagate(False)


############################################################################################################ PAGE 3
# page_three = Frame(window, bg='black', width=1280, height=800, borderwidth=2)
#
# # Background IMAGE
# bg5_img = Image.open('wallpaper3.jpg')
# new_width5 = 1280
# new_height5 = 800
# wallpaper5 = bg2_img.resize((new_width5, new_height5), Image.Resampling.LANCZOS)
# wallpaper5.save('wallpaper3.jpg')
# bg5 = ImageTk.PhotoImage(wallpaper5)
# bg_label5 = Label(page_three, image=bg5)
# bg_label5.grid(rowspan=4, columnspan=1)
# bg_label5.grid_propagate(False)


# Next button
# next_button = Button(box3, command=next_button_click, font=('Impact', 20), text='Next',
#                        relief=GROOVE, bg='black', fg='white')
# next_button.grid(row=9, column=0, columnspan=3)
#
#
# # frame
# box0 = Frame(box10, bg='#354d8b', width=600, height=110,
#              borderwidth=5)
# box0.grid(row=4, column=0, columnspan=3, pady=3)
# box0.grid_propagate(False)
# box0.columnconfigure(0, weight=1)
# box0.columnconfigure(1, weight=1)
# box0.columnconfigure(2, weight=1)


######################## FINAL CONFIRMATION PAGE
# final_page =  Frame(window, bg='black', width=1920, height=1080, borderwidth=1)
#
# # Background IMAGE
# # bgFINAL_img = Image.open('wallpaperFINAL.jpg')
# # new_widthFINAL = 1280
# # new_heightFINAL = 800
# # wallpaperFINAL = bgACC_img.resize((new_widthFINAL, new_heightFINAL), Image.Resampling.LANCZOS)
# # wallpaperFINAL.save('wallpaperFINAL.jpg')
# # bgFINAL = ImageTk.PhotoImage(wallpaperFINAL)
# # bg_labelFINAL = Label(final_page, image=bgFINAL)
# # bg_labelFINAL.grid(rowspan=4, columnspan=1)
# # bg_labelFINAL.grid_propagate(False)
#
# # frame
# final_box = Frame(final_page, bg='#354d8b', width=600, height=430,
#                    borderwidth=2, relief=RAISED)
# final_box.grid(row=0, column=0, columnspan=3, pady=3)
# final_box.grid_propagate(False)
# final_box.columnconfigure(0, weight=1)
# final_box.columnconfigure(1, weight=1)
# final_box.columnconfigure(2, weight=1)
#
# final_label = Label(final_box, text="Thank you for booking with DACAT", justify=CENTER, font=('Impact', 16),
#                    bg='#354d8b', fg='white')
# final_label.grid(row=0, column=0, columnspan=3, pady=10)
#
#
# confirmation_button = Button(final_box, font=("Arial", 12), text='Log Out', width=15, command=logout)
# confirmation_button.grid(column=0, row=2, pady=2, padx=0, columnspan=3)

window.config(menu=menubar)
window.mainloop()