from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from classes import BookHotel
from os import path
import time
import json
import csv


f = open('mentors.json')
mentors_accounts = json.load(f)
f.close()

f1 = open('mentees.json')
mentees_accounts = json.load(f1)
f1.close()


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
            box1.grid_forget()
            mentee_message_label.config(text=" ")
            mentee_welcomepg.grid()
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
    # bg_label.grid_forget()
    box.grid_forget()
    mentor_loginpg.grid()
    mentor_loginpg.columnconfigure(0, weight=1)
    box2.grid(row=0, column=0)


def choose_mentee():
    # bg_label.grid_forget()
    box.grid_forget()
    mentee_loginpg.grid()
    mentee_loginpg.columnconfigure(0, weight=1)
    box1.grid(row=0, column=0)


def back_mentee():
    mentee_loginpg.grid_forget()
    box1.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box.grid(row=0, column=0)
    mentee_message_label.config(text=" ")


def back_mentor():
    mentor_loginpg.grid_forget()
    box2.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box.grid(row=0, column=0)
    mentor_message_label.config(text=" ")


def create_mentee_account():
    mentee_loginpg.grid_forget()
    box1.grid_forget()
    # page_two.grid_forget()
    # page_three.grid_forget()
    mentee_account_page.grid()
    mentee_account_page.columnconfigure(0, weight=3)
    # bg_labelACC.grid(rowspan=4, columnspan=1)
    create_box.grid(row=0, column=0)


def create_mentor_account():
    mentor_loginpg.grid_forget()
    box2.grid_forget()
    # page_two.grid_forget()
    # page_three.grid_forget()
    mentor_account_page.grid()
    mentor_account_page.columnconfigure(0, weight=3)
    # bg_labelACC.grid(rowspan=4, columnspan=1)
    # create_box.grid(row=0, column=0)


def mentee_back_to_login():
    mentee_account_page.grid_forget()
    mentee_loginpg.grid()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box1.grid(row=0, column=0)


def mentor_back_to_login():
    mentor_account_page.grid_forget()
    mentor_loginpg.grid()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    box2.grid(row=0, column=0)

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


################################################# INTRO PAGE

box = Frame(window, bg='white', width=400, height=200)
box.grid(row=0, columnspan=4)
# box.grid_propagate(False)

title_label = Label(box, text='Mentor Program', width=20, font=('Open Sans', 24, 'bold'), fg='black', bg= 'white')
title_label.grid(columnspan=4, row=1, column=0)

choose_label = Label(box, text='Choose your Role', width=20, font=('Open Sans', 20, 'bold'), fg='black', bg= 'white')
choose_label.grid(columnspan=4, row=2, column=0, pady=10)

mentee_button = Button(box, font=("Roboto", 12), text='Mentee', width=10, command=choose_mentee, relief=FLAT, bg='#135fca',
                       fg='white')
mentee_button.grid(row=3, column=0, pady=10, columnspan=4)

mentor_button = Button(box, font=("Roboto", 12), text='Mentor', width=10, command=choose_mentor, relief=FLAT, bg='#ffa440',
                       fg='white')
mentor_button.grid(row=4, column=0, pady=10, columnspan=4)






####################################################################### MENTEE PAGES

# Configure variables
mentee_username = StringVar()
mentee_password = StringVar()


# CONTACT PAGE
mentee_loginpg = Frame(window, width=1280, height=800)

# FRAME WITH USERNAME & PASSWORD
box1 = Frame(mentee_loginpg, bg='white', width=500, height=500)
box1.grid(row=0, columnspan=3)

# LOGO IMAGE
# logo = Image.open('thecat.png')
# new_width = 300
# new_height = 225
# img = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
# img.save('thecat.png')
# logo = ImageTk.PhotoImage(img)
# logo_label = Label(box1, image=logo)
# logo_label.grid(row=0, column=0, columnspan=4)

# LOG IN TO YOUR ACCOUNT MESSAGE
mentee_label = Label(box1, text='Mentee\n Login to your Account', font=('Open Sans', 20, 'bold'), fg='black', bg= 'white')
mentee_label.grid(columnspan=4, row=1, column=0)

# Login_label = Label(box1, text='Login to your Account', width=40, font=('Open Sans', 14), fg='black', bg= 'white')
# Login_label.grid(row=2)

mentee_message_label = Label(box1, justify=CENTER, font=('Open Sans', 10), bg='white', wraplength=210)
mentee_message_label.grid(columnspan=3, row=2, column=0)

# label for username and password
mentee_username_label = Label(box1, text='Username', fg='black', font=('Open Sans', 12), bg='white')
mentee_username_label.grid(columnspan=1, row=3, column=0, pady=20)
mentee_password_label = Label(box1, font=('Open Sans', 12), text='Password', bg='white')
mentee_password_label.grid(columnspan=1, row=4, column=0)

# # BOX 1, USER & PASSWORD ENTRY BOXES
mentee_username_entry = Entry(box1, textvariable=mentee_username, justify=LEFT, width=20, font=('Verdana', 11))
mentee_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentee_password_entry = Entry(box1, textvariable=mentee_password, justify=LEFT, width=20, font=('Verdana', 11), show="*")
mentee_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentee_login_button = Button(box1, command=mentee_login, font=('Roboto', 12), text='Log In',
                        relief=FLAT, bg='#135fca', fg='white', width=10)
mentee_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

#contact button
back_button = Button(box1, font=('Roboto', 12), text='Back',
                        fg='black', width=8, command=back_mentee, relief="groove")
back_button.grid(row=7,column=0, pady=10, padx=10)

#create account button
newMentee_button = Button(box1, command=create_mentee_account, font=('Roboto', 12), text='New Mentee',
                        fg='black', relief="groove")
newMentee_button.grid(row=7, column=1, sticky=E, pady=10, padx=10)


###################################################### CREATE MENTEE ACCOUNT PAGE
mentee_account_page = Frame(window, width=1280, height=800)

# frame
create_box = Frame(mentee_account_page, bg='white', width=600, height=630, relief=FLAT)
create_box.grid(row=0, column=0, columnspan=3, pady=3)
create_box.grid_propagate(False)
create_box.columnconfigure(0, weight=1)
create_box.columnconfigure(1, weight=1)
create_box.columnconfigure(2, weight=1)

Login_label = Label(create_box, text='Create Your Mentee Account', width=40, font=('Open Sans', 20), fg='black', bg= 'white')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
newusername_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newusername_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentee_newusername_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
newpassword_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentee_newpassword_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
email_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_email_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentee_email_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)

mentee_q1_label = Label(create_box, text='\nWhat are you looking for in a mentor?', justify=CENTER, font=('Arial', 12),
                        bg='white', fg='black')
mentee_q1_label.grid(row=4, column=0, pady=5, padx=100, columnspan=3)


blank_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Arial', 12), fg='black')
blank_label.grid(row=5, column=0, pady=30, columnspan=3)

mentee_q1_entry = Text(create_box, font=('Arial', 12), height=30)
mentee_q1_entry.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)
# mentee_q1_entry.grid(row=5, column=0, pady=5, columnspan=3, padx=30)


create_button = Button(create_box, font=('Roboto', 12), text='Create', width=10, command=add_new_mentee, relief=FLAT,
                       bg='#135fca', fg='white')
create_button.grid(column=0, row=7, pady=30, columnspan=3)

mentee_create_label = Label(create_box, text=' ', width=60, bg='white', font=('Arial', 12), fg='black')
mentee_create_label.grid(row=8, column=0, pady=30, columnspan=3)

home_button = Button(create_box, command=mentee_back_to_login, font=('Roboto', 12), text='Back to Login',
                       fg='black', relief="groove")
home_button.grid(row=9, column=0, columnspan=3)


############################################################### MENTEE WELCOME
mentee_welcomepg = Frame(window, width=1280, height=800)





################################################################# MENTOR PAGES
# Configure variables
mentor_username = StringVar()
mentor_password = StringVar()


# CONTACT PAGE
mentor_loginpg = Frame(window, width=1280, height=800)


# FRAME WITH USERNAME & PASSWORD
box2 = Frame(mentor_loginpg, bg='white', width=500, height=500)
box2.grid(row=0, columnspan=5)

# LOG IN TO YOUR ACCOUNT MESSAGE
mentor_label = Label(box2, text='Mentor\n Login to your Account', font=('Open Sans', 20, 'bold'), fg='black', bg= 'white')
mentor_label.grid(columnspan=4, row=1, column=0)

# Login_label = Label(box2, text='Login to your Account', width=40, font=('Open Sans', 14), fg='black', bg= 'white')
# Login_label.grid(row=2)

mentor_message_label = Label(box2, justify=CENTER, font=('Open Sans', 10), bg='white', wraplength=210)
mentor_message_label.grid(columnspan=3, row=2, column=0)

# label for username and password
mentor_username_label = Label(box2, text='Username', fg='black', font=('Lato', 12), bg='white')
mentor_username_label.grid(columnspan=1, row=3, column=0, pady=20)
mentor_password_label = Label(box2, font=('Open Sans', 12), text='Password', bg='white')
mentor_password_label.grid(columnspan=1, row=4, column=0)

# # BOX 1, USER & PASSWORD ENTRY BOXES
mentor_username_entry = Entry(box2, textvariable=mentor_username, justify=LEFT, width=20, font=('Verdana', 11))
mentor_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentor_password_entry = Entry(box2, textvariable=mentor_password, justify=LEFT, width=20, font=('Verdana', 11), show="*")
mentor_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentor_login_button = Button(box2, command=mentor_login, font=('Roboto', 12), text='Log In',
                        relief=FLAT, bg='#ffa440', fg='white', width=10)
mentor_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

#contact button
back_button = Button(box2, font=('Roboto', 12), text='Back',
                        fg='black', width=8, command=back_mentor, relief="groove")
back_button.grid(row=7,column=0, pady=10, padx=10)

#create account button
newMentor_button = Button(box2, command=create_mentor_account, font=('Roboto', 12), text='New Mentor',
                        fg='black', relief="groove")
newMentor_button.grid(row=7, column=1, sticky=E, pady=10, padx=10)

###################################################### CREATE MENTOR ACCOUNT PAGE
mentor_account_page = Frame(window, width=1920, height=1080)

# frame
create_box = Frame(mentor_account_page, bg='white', width=600, height=630, relief=FLAT)
create_box.grid(row=0, column=0, columnspan=3, pady=3)
create_box.grid_propagate(False)
create_box.columnconfigure(0, weight=1)
create_box.columnconfigure(1, weight=1)
create_box.columnconfigure(2, weight=1)

Login_label = Label(create_box, text='Create Your Mentor Account', width=40, font=('Open Sans', 20), fg='black', bg= 'white')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
newusername_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newusername_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentor_newusername_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
newpassword_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentor_newpassword_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Arial', 12), bg='white', fg='black')
email_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_email_textbox = Entry(create_box, justify=LEFT, font=('Arial', 12))
mentor_email_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)


mentor_q1_label = Label(create_box, text='\nWhat can you provide as a mentor?', justify=CENTER, font=('Arial', 12),
                        bg='white', fg='black')
mentor_q1_label.grid(row=4, column=0, pady=5, padx=100, columnspan=3)


blank_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Arial', 12), fg='black')
blank_label.grid(row=5, column=0, pady=30, columnspan=3)

mentee_q1_entry = Text(create_box, font=('Arial', 12), height=30)
mentee_q1_entry.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)
# mentee_q1_entry.grid(row=5, column=0, pady=5, columnspan=3, padx=30)

create_button = Button(create_box, font=("Roboto", 12), text='Create', width=10, command=add_new_mentor, relief=FLAT,
                       bg='#ffa440', fg='white')
create_button.grid(column=0, row=7, pady=30, columnspan=3)

mentor_create_label = Label(create_box, text=' ', width=60, bg='white', font=('Arial', 12), fg='black')
mentor_create_label.grid(row=8, column=0, pady=30, columnspan=3)

home_button = Button(create_box, command=mentor_back_to_login, font=('Roboto', 12), text='Back to Login',
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
