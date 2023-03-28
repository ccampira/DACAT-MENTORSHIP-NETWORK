from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from classes import BookHotel
from os import path
import time
import json
import csv


def login_mentee():
    intro_page.grid_forget()


def login_mentor():
    intro_page.grid_forget()
    # box1.grid_forget()
    # page_two.grid_forget()
    # page_three.grid_forget()
    # contact_page.grid()
    # contact_page.grid()
    # contact_page.columnconfigure(0, weight=2)
    # bg_label3.grid(rowspan=4, columnspan=1)
    # box2.grid(row=0, column=0)


window = Tk()
# window.state('zoomed')
window.geometry('1280x800')  # left number is width, right number is height
window.title('DA CAT')
window.config(bg='#354d8b')  # we are using rgb color
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
edit = Menu(menubar, tearoff=False)  # if tearoff = false then it will be glued to the menu bar.
# If tearoff = true then it will allow you to move it.
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

# window.attributes('-fullscreen', True)
# window.overrideredirect(True)

window.columnconfigure(0, weight=1)

####################################################################################################### INTRO PAGE
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

introFrame = Frame(intro_page, bg='white', width=450, height=300, borderwidth=1)
introFrame.grid(row=0, column=0)

introQuestion = Label(introFrame, text='Which one are you?', font=('Bodoni MT', 20), bg='#fbfbfb')
introQuestion.grid(row=0, column=0, columnspan=2)

mentee_button = Button(introFrame, font=('Bodoni MT', 20), text='Mentee',
                       relief=GROOVE, bg='black', fg='white', command=login_mentee)
mentee_button.grid(row=1, column=0)

mentor_button = Button(introFrame, font=('Bodoni MT', 20), text='Mentor',
                       relief=GROOVE, bg='black', fg='white', command=login_mentor)
mentor_button.grid(row=1, column=1)
####################################################################################################### INTRO PAGE END

####################################################################################################### MENTEE PAGE
mentee_login_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
mentee_login_page.grid()
mentee_login_img = Image.open('whiteBackground.jpg')
new_width2 = 1280
new_height2 = 800
wallpaper2 = mentee_login_img.resize((new_width2, new_height2), Image.Resampling.LANCZOS)
wallpaper2.save('whiteBackground.jpg')
bg2 = ImageTk.PhotoImage(wallpaper2)
bg_label2 = Label(mentee_login_page, image=bg2)
bg_label2.grid(row=0, column=0, rowspan=2, columnspan=1)

mentee_login_frame = Frame(mentee_login_page, bg='white', width=450, height=300, borderwidth=1)
mentee_login_frame.grid(row=0, column=0)

####################################################################################################### MENTEE PAGE END

####################################################################################################### MENTOR PAGE
mentor_login_page = Frame(window, bg='white', width=1280, height=800, borderwidth=1)
mentor_login_page.grid()
mentor_login_img = Image.open('whiteBackground.jpg')
new_width3 = 1280
new_height3 = 800
wallpaper3 = mentor_login_img.resize((new_width3, new_height3), Image.Resampling.LANCZOS)
wallpaper3.save('whiteBackground.jpg')
bg3 = ImageTk.PhotoImage(wallpaper3)
bg_label3 = Label(mentor_login_page, image=bg3)
bg_label3.grid(row=0, column=0, rowspan=2, columnspan=1)

mentor_login_frame = Frame(mentor_login_page, bg='white', width=450, height=300, borderwidth=1)
mentor_login_frame.grid(row=0, column=0)
####################################################################################################### MENTOR PAGE END
window.config(menu=menubar)
window.mainloop()
