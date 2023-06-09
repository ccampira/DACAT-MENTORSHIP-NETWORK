import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from classes import BookHotel
from os import path
from time import strftime
import json
import csv
from tkinter import filedialog
from tkinter.filedialog import askopenfile

from chat_config import Chat
import socketio

global mentees_accounts


f = open('mentors.json')
mentors_accounts = json.load(f)
f.close()

f1 = open('mentees.json')
mentees_accounts = json.load(f1)
f1.close()

f2 = open('menteeslogin.json')
mentees_login = json.load(f2)
f2.close()

try:
    socket_connection = socketio.Client()
    socket_connection.connect('http://localhost:3000')
except:
    print('Could not connect to socket ')


def upload_file():
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    profile = Image.open(filename)
    profile_pic = profile.resize((150, 150))  # new width & height
    profile_pic.save('profile_pic.jpg')
    view = ImageTk.PhotoImage(profile_pic)
    e1= Label(create_box)
    e1.grid(row=12, column=1)
    e1.image = view
    e1['image'] = view


    buttonavatar = tkinter.Button(mentor_list_box, image=view, width=200, height=200)
    buttonavatar.bind("<Button>", lambda e: NewWindow5(mentor_list_box))
    buttonavatar.grid(row=3, column=2)
    avatar_label = Label(mentor_list_box, text=mentor_q1_entry.get(), font=('Bodoni MT', 12),
                         bg='white')
    avatar_label.grid(row=4, column=2)
############################ mentor page - mentee list
def load_json_from_file():
    global mentees

    with open('mentees.json', "r") as file_handler:
        mentees_accounts = json.load(file_handler)

    print(mentees_accounts)


def save_json_to_file():
    global mentees
    with open("mentees.json", "w") as file_handler:
        json.dump(mentees_accounts, file_handler, indent=4)


def clear_mentee_list():
    for item in mentee_list.get_children():
        mentee_list.delete(item)


def load_list_with_json():
    global mentees

    clear_mentee_list()

    rowIndex = 1
    for key in mentees_accounts:
        username = key["username"]
        name = key["name"]
        email = key["email"]
        cellphone = key["cellphone"]

        mentee_list.insert('', index='end', iid=rowIndex, text="",
                           values=(username, name, email, cellphone))
        rowIndex = rowIndex + 1


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Dwayne Johnson's Mentor Profile")
        self.geometry("800x550")
        rock_frame = Frame(self, bg='white', width=800, height=550, borderwidth=2, relief=RAISED)
        rock_frame.grid(row=0, column=0)
        rock_frame.grid_propagate(False)

        buttonRock1 = tkinter.Button(rock_frame, image=theRock)
        buttonRock1.grid(row=1, column=0, pady=30, padx=5)
        rock_label1 = Label(rock_frame, text=f'Dwayne Johnson', font=('Bodoni MT', 20),
                           bg='white')
        rock_label1.grid(row=2, column=0, pady=10, padx=5)
        rock_label2 = Label(rock_frame, text=f'Major: Computer Information Systems', font=('Bodoni MT', 20),
                           bg='white')
        rock_label2.grid(row=3, column=0, pady=10, padx=5)
        rock_label3 = Label(rock_frame, text=f'Hi My names Dwayne, a current professional in the industry of info systems\n'
                                             f'I want to mentor someone interested in data science or analytics\n'
                                             f'I have 4 years of experience in both and want to give a motivated\n'
                                             f'individual advice on how to be successful in your early career.', font=('Bodoni MT', 16),
                           bg='white')
        rock_label3.grid(row=4, column=0, pady=30, padx=20)
        rock_label4 = Label(rock_frame, text=f'Phone Number: #480-123-5678\n'
                                             f'E-mail: DJohnson@gmail.com', font=('Bodoni MT', 11),
                            bg='white')
        rock_label4.grid(row=1, column=0, pady=5, padx=5, sticky=W)


        # label = Label(self, text="Hi My names Dwayne, a current professional in the industry")

class NewWindow1(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Mark Walhberg's Mentor Profile")
        self.geometry("800x550")
        walhberg_frame = Frame(self, bg='white', width=800, height=550, borderwidth=2, relief=RAISED)
        walhberg_frame.grid(row=0, column=0)
        walhberg_frame.grid_propagate(False)

        buttonwalhberg1 = tkinter.Button(walhberg_frame, image=mwahlberg)
        buttonwalhberg1.grid(row=1, column=0, pady=30, padx=5)
        walhberg_label1 = Label(walhberg_frame, text=f'Mark Walhberg', font=('Bodoni MT', 20),
                           bg='white')
        walhberg_label1.grid(row=2, column=0, pady=10, padx=5)
        walhberg_label2 = Label(walhberg_frame, text=f'Major: Software Development & Communications', font=('Bodoni MT', 20),
                           bg='white')
        walhberg_label2.grid(row=3, column=0, pady=10, padx=5)
        walhberg_label3 = Label(walhberg_frame, text=f'Hi My names Mark, a current professional in the industry of software development\n'
                                             f'I am eager to mentor and teach incoming ASU professionals or Alumni\n'
                                             f'I have over 10 years of experience in development and would love to share\n'
                                             f'what I have learned over the past 10 years with you!', font=('Bodoni MT', 16),
                           bg='white')
        walhberg_label3.grid(row=4, column=0, pady=30, padx=20)
        walhberg_label4 = Label(walhberg_frame, text=f'Phone Number: #480-321-5678\n'
                                             f'E-mail: MWalhberg@gmail.com', font=('Bodoni MT', 11),
                            bg='white')
        walhberg_label4.grid(row=1, column=0, pady=5, padx=5, sticky=W)

class NewWindow2(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Mark Zuckerberg Mentor's Profile")
        self.geometry("800x550")
        zuck_frame = Frame(self, bg='white', width=800, height=550, borderwidth=2, relief=RAISED)
        zuck_frame.grid(row=0, column=0)
        zuck_frame.grid_propagate(False)

        buttonzuck1 = tkinter.Button(zuck_frame, image=zuckerberg)
        buttonzuck1.grid(row=1, column=0, pady=30, padx=5)
        zuck_label1 = Label(zuck_frame, text=f'Mark Zuckerberg', font=('Bodoni MT', 20),
                           bg='white')
        zuck_label1.grid(row=2, column=0, pady=10, padx=5)
        zuck_label2 = Label(zuck_frame, text=f'Major: Computer Science & Management', font=('Bodoni MT', 20),
                           bg='white')
        zuck_label2.grid(row=3, column=0, pady=10, padx=5)
        zuck_label3 = Label(zuck_frame, text=f'Hi My names Mark, a current professional in the computer science industry\n'
                                             f'I would love to teach someone who is likes to code and learn new software\n'
                                             f'I have over 35 years of experience in computer science and want\n'
                                             f'to give insight on how to succeed and improve in the industry', font=('Bodoni MT', 16),
                           bg='white')
        zuck_label3.grid(row=4, column=0, pady=30, padx=20)
        zuck_label4 = Label(zuck_frame, text=f'Phone Number: #480-777-5678\n'
                                             f'E-mail: MZuck@gmail.com', font=('Bodoni MT', 11),
                            bg='white')
        zuck_label4.grid(row=1, column=0, pady=5, padx=5, sticky=W)

class NewWindow3(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Natalie Portman's Mentor Profile")
        self.geometry("800x550")
        nat_frame = Frame(self, bg='white', width=800, height=550, borderwidth=2, relief=RAISED)
        nat_frame.grid(row=0, column=0)
        nat_frame.grid_propagate(False)

        buttonnat1 = tkinter.Button(nat_frame, image=portman)
        buttonnat1.grid(row=1, column=0, pady=30, padx=5)
        nat_label1 = Label(nat_frame, text=f'Natalie Portman', font=('Bodoni MT', 20),
                           bg='white')
        nat_label1.grid(row=2, column=0, pady=10, padx=5)
        nat_label2 = Label(nat_frame, text=f'Major: Finance & Data Analytics', font=('Bodoni MT', 20),
                           bg='white')
        nat_label2.grid(row=3, column=0, pady=10, padx=5)
        nat_label3 = Label(nat_frame, text=f'Hi My names Natalie, a current professional in the industry finance & analytics\n'
                                             f'I am looking to mentor someone who is interested in fin tech\n'
                                             f'I have over 5 years of experience in fin tech and would love to share\n'
                                             f'my experiences and how to excel your career', font=('Bodoni MT', 16),
                           bg='white')
        nat_label3.grid(row=4, column=0, pady=30, padx=20)
        nat_label4 = Label(nat_frame, text=f'Phone Number: #480-666-5678\n'
                                             f'E-mail: NPortman@gmail.com', font=('Bodoni MT', 12),
                            bg='white')
        nat_label4.grid(row=1, column=0, pady=5, padx=5, sticky=W)

class NewWindow4(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Bill Gates' Mentor Profile")
        self.geometry("800x550")
        bill_frame = Frame(self, bg='white', width=800, height=550, borderwidth=2,  relief=RAISED)
        bill_frame.grid(row=0, column=0)
        bill_frame.grid_propagate(False)

        buttonbill1 = tkinter.Button(bill_frame, image=gates)
        buttonbill1.grid(row=1, column=0, pady=30, padx=5)
        bill_label1 = Label(bill_frame, text=f'Bill Gates', font=('Bodoni MT', 20),
                           bg='white')
        bill_label1.grid(row=2, column=0, pady=10, padx=5)
        bill_label2 = Label(bill_frame, text=f'Major: Business Data Analytics', font=('Bodoni MT', 20),
                           bg='white')
        bill_label2.grid(row=3, column=0, pady=10, padx=5)
        bill_label3 = Label(bill_frame, text=f'Hi My names Bill, a current professional in the industry of data analytics\n'
                                             f'I look forward to mentoring someone new every year!\n'
                                             f'I have 20 years of experience in analytics and would love to share\n'
                                             f'what I have learned over the past 20 years with someone motivated!', font=('Bodoni MT', 16),
                           bg='white')
        bill_label3.grid(row=4, column=0, pady=30, padx=20)
        bill_label4 = Label(bill_frame, text=f'Phone Number: #480-444-5678\n'
                                             f'E-mail: BGates@gmail.com', font=('Bodoni MT', 10),
                            bg='white')
        bill_label4.grid(row=1, column=0, pady=5, padx=5, sticky=W)


class NewWindow5(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title(f"{mentor_name_textbox.get()}'s Mentor Profile")
        self.geometry("800x550")
        new_frame1 = Frame(self, bg='white', width=800, height=550, borderwidth=2, relief=RAISED)
        new_frame1.grid(row=0, column=0, columnspan=3)

        buttonava = tkinter.Button(new_frame1, image=ava)
        buttonava.grid(row=1, column=0, pady=30, padx=5)

        new_label1 = Label(new_frame1, text=mentor_name_textbox.get(), font=('Bodoni MT', 20),
                           bg='white')
        new_label1.grid(row=2, column=0, pady=10, padx=5)

        label = Label(self, text=mentor_q1_entry.get(), font=('Bodoni MT', 16),
                           bg='white')
        label.grid(row=4, column=0, pady=30, padx=20)

        label2 = Label(self, text=mentor_q2_entry.get(), font=('Bodoni MT', 16),
                           bg='white')
        label2.grid(row=5, column=0, pady=30, padx=20)

        label3 = Label(self, text=f'E-mail: {mentor_email_textbox.get()}', font=('Bodoni MT', 10),
                            bg='white')
        label3.grid(row=1, column=0, pady=5, padx=5, sticky=W)



def show_time():
    time = strftime("%H:%M:%S")
    date = strftime('%Y/%m/%d')
    set_text = f"{time} \n {date}"
    date_time.configure(text=set_text, font=("Calibri", 15, "bold"), bg="black", fg="white")
    date_time.after(100, show_time)


def mentor_login():
    global mentees
    print(mentees_accounts)
    try:
        result = any(mentor_password_entry.get() in d.values() for d in mentors_accounts.values())
        if mentor_username_entry.get() not in mentors_accounts or result is False:
            mentor_message_label.config(
                text=f'Unable to login. Please create an account or try again.')
        else:
            # bg_label.grid_forget()
            mentor_login_page.grid_forget()
            mentor_message_label.config(text=" ")
            mentor_welcomepg.grid()
            editProfile_button.grid(row=0, column=0, pady=2, sticky=N)
            mentor_logout_button.grid(row=0, column=0, pady=8, sticky=NE)
            date_time.grid(row=0, column=0, pady=10, padx=8, sticky=NW)
            show_time()
            load_list_with_json()
            global current_user
            current_user = mentor_username_entry.get()
            print('mentor socket id', socket_connection.sid)
            mentors_accounts[mentor_username_entry.get()]['SOCKET_ID'] = socket_connection.sid
            with open('mentors.json', 'w', newline='') as f:
                json.dump(mentors_accounts, f)
    except AttributeError:
        mentor_message_label.config(
            text=f'{mentor_username_entry.get()}, your password is incorrect. Please try again.')


def mentee_login():
    try:
        result = any(mentee_password_entry.get() in d.values() for d in mentees_login.values())
        if mentee_username_entry.get() not in mentees_login or result is False:
            mentee_message_label.config(
                text=f'Unable to login. Please create an account or try again.')
        else:
            # bg_label.grid_forget()
            # mentee_email.set(mentees_accounts[mentee_username_entry.get()]["Email"])
            mentee_login_page.grid_forget()
            mentee_message_label.config(text=" ")
            mentee_welcomepg.grid()
            # sidebarFrame.grid(row=0, column=0, columnspan=1, sticky=N)
            editProfile_button.grid(row=0, column=0, pady=2, sticky=N)
            mentee_logout_button.grid(row=0, column=0, pady=8, sticky=NE)
            date_time.grid(row=0, column=0, pady=10, padx=8, sticky=NW)
            show_time()
            global current_user
            current_user = mentee_username_entry.get()
            print('mentee socket id', socket_connection.sid)
            user_socket = socket_connection.sid
            mentees_accounts[1]['SOCKET_ID'] = socket_connection.sid
            with open('mentees.json', 'w', newline='') as f:
                json.dump(mentees_accounts, f)

    except AttributeError:
        mentee_message_label.config(
            text=f'{mentee_username_entry.get()}, your password is incorrect. Please try again.')


def add_new_mentor():
    mentor_newusername = mentor_newusername_textbox.get()
    mentor_newpassword = mentor_newpassword_textbox.get()
    mentor_email = mentor_email_textbox.get()
    mentor_name = mentor_name_textbox.get()

    mentors_accounts[mentor_newusername] = dict()
    mentors_accounts[mentor_newusername]['Password'] = mentor_newpassword
    mentors_accounts[mentor_newusername]['Email'] = mentor_email
    mentors_accounts[mentor_newusername]['Name'] = mentor_name

    with open('mentors.json', 'w', newline='') as f:
        json.dump(mentors_accounts, f)

    mentor_create_label.config(text=f'Thank you {mentor_newusername}, your account has been created!')


def add_new_mentee():
    mentee_fullname = mentee_fullname_textbox.get()
    mentee_newusername = mentee_newusername_textbox.get()
    mentee_newpassword = mentee_newpassword_textbox.get()
    mentee_email = mentee_email_textbox.get()
    mentee_phone = mentee_phone_textbox.get()

    mentees_login[mentee_newusername] = dict()
    mentees_login[mentee_newusername]['Password'] = mentee_newpassword
    mentees_login[mentee_newusername]['Email'] = mentee_email

    mentees_accounts.append({'username': mentee_newusername, 'name': mentee_fullname, 'email': mentee_email, 'cellphone': mentee_phone})
    # mentees_accounts[mentee_newusername] = dict()
    # mentees_accounts[mentee_newusername]['name'] = mentee_fullname
    # mentees_accounts[mentee_newusername]['email'] = mentee_email
    # mentees_accounts[mentee_newusername]['cellphone'] = mentee_phone

    with open('menteeslogin.json', 'w', newline='') as f2:
        json.dump(mentees_login, f2)

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


def mentee_logout():
    mentee_welcomepg.grid_forget()
    mentee_login_page.grid()
    mentee_login_page.columnconfigure(0, weight=1)
    box1.grid(row=0, column=0)
    editProfile_button.grid_forget()
    mentee_logout_button.grid_forget()
    date_time.grid_forget()
    mentee_username_entry.delete(0, END)
    mentee_password_entry.delete(0, END)
    user_profile_frame.grid_forget()
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    # box1.grid(row=0, column=0)
    socket_connection.disconnect()


def mentor_logout():
    mentor_welcomepg.grid_forget()
    mentor_login_page.grid()
    mentor_login_page.columnconfigure(0, weight=1)
    box2.grid(row=0, column=0)
    editProfile_button.grid_forget()
    mentor_logout_button.grid_forget()
    date_time.grid_forget()
    mentor_username_entry.delete(0, END)
    mentor_password_entry.delete(0, END)
    # bg_label.grid(row=0, column=0, rowspan=2, columnspan=1)
    # box1.grid(row=0, column=0)
    socket_connection.disconnect()


# def final():
# page_three.grid_forget()
# final_page.grid()
# final_page.columnconfigure(0, weight=3)

def sendMessage():
    chat = Chat(current_user, 'mentee')


def sendMessageToMentee():
    chat = Chat(current_user, 'mentor')

def close():
    window.destroy()


def editProfilePage():
    mentee_welcomepg.grid_forget()
    box.grid_forget()
    user_profile_frame.grid()
    user_profile_frame.columnconfigure(0, weight=1)
    box2.grid(row=0, column=0)


def overwrite_user_info():
    with open('menteeslogin.json', 'r') as f:
        data = json.load(f)
    with open('mentees.json', 'r') as x:
        update = json.load(x)
    data[mentee_username.get()]["Password"] = password_entry.get()
    data[name_entry.get()] = data.pop(mentee_username.get())
    index = next((index for (index, d) in enumerate(update) if d["username"] == mentee_username.get()), None)
    update[int(index)]['username'] = name_entry.get()
    mentee_username.set(name_entry.get())
    mentee_password.set(password_entry.get())
    with open('menteeslogin.json', 'w') as f:
        json.dump(data, f)
    with open('mentees.json', 'w') as x:
        json.dump(update, x)
    edit_success_label.config(
                text=("Success! You have edited your account information!\n\n Please restart the app for changes to be saved"))

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

choose_label = Label(box, text='Choose your Role', width=20, font=('Bodoni MT', 20, 'bold'), fg='black', bg='white')
choose_label.grid(columnspan=4, row=2, column=0, pady=10)

mentee_button = Button(box, font=("Bodoni MT", 12), text='MENTEE', width=10, command=choose_mentee, relief=FLAT,
                       bg='black',
                       fg='white')
mentee_button.grid(row=3, column=0, pady=10, columnspan=4)

mentor_button = Button(box, font=("Bodoni MT", 12), text='MENTOR', width=10, command=choose_mentor, relief=FLAT,
                       bg='black',
                       fg='white')
mentor_button.grid(row=4, column=0, pady=10, columnspan=4)
###################################################################################################### INTRO PAGE ENDS


######################################################################################################## MENTEE PAGES

# Configure variables
mentee_username = StringVar()
mentee_password = StringVar()
mentee_email = StringVar()
mentor_description = StringVar()
mentor_description2 = StringVar()

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
mentee_label = Label(box1, text='Mentee\n Login to your Account', font=('Bodoni MT', 20, 'bold'), fg='black',
                     bg='#fbfbfb')
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
mentee_username_entry = Entry(box1, textvariable=mentee_username, justify=LEFT, width=20, font=('Calibri', 11),
                              bg='#fbfbfb')
mentee_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentee_password_entry = Entry(box1, textvariable=mentee_password, justify=LEFT, width=20, font=('Calibri', 11),
                              show="*", bg='#fbfbfb')
mentee_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentee_login_button = Button(box1, command=mentee_login, font=('Bodoni MT', 12), text='Log In',
                             relief=FLAT, bg='#135fca', fg='white', width=10)
mentee_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

# contact button
back_button = Button(box1, font=('Bodoni MT', 12), text='Back',
                     fg='black', width=8, command=back_mentee, relief="groove")
back_button.grid(row=7, column=0, pady=10, padx=10)

# create account button
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

Login_label = Label(create_box, text='Create Your Mentee Account', width=40, font=('Bodoni MT', 20), fg='black',
                    bg='#fbfbfb')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

fullname_label = Label(create_box, text='Enter Full Name: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb',
                          fg='black')
fullname_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_fullname_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_fullname_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb',
                          fg='black')
newusername_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newusername_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_newusername_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb',
                          fg='black')
newpassword_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_newpassword_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb', fg='black')
email_label.grid(row=4, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_email_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_email_textbox.grid(row=4, column=1, pady=1, padx=100, sticky=W, columnspan=2)

phone_label = Label(create_box, text='Enter Cell: ', justify=CENTER, font=('Calibri', 12), bg='#fbfbfb', fg='black')
phone_label.grid(row=5, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentee_phone_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentee_phone_textbox.grid(row=5, column=1, pady=1, padx=100, sticky=W, columnspan=2)

# mentee_q1_label = Label(create_box, text='\nWhat are you looking for in a mentor?', justify=CENTER,
#                         font=('Bodoni MT', 12),
#                         bg='#fbfbfb', fg='black')
# mentee_q1_label.grid(row=4, column=0, pady=5, padx=100, columnspan=3)
#
# blank_label = Label(create_box, text='\n\n\n ', width=60, bg='#fbfbfb', font=('Calibri', 12), fg='black')
# blank_label.grid(row=5, column=0, pady=30, columnspan=3)
#
# mentee_q1_entry = Text(create_box, font=('Calibri', 12), height=30)
# mentee_q1_entry.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)
# mentee_q1_entry.grid(row=5, column=0, pady=5, columnspan=3, padx=30)


create_button = Button(create_box, font=('Bodoni MT', 12), text='Create', width=10, command=add_new_mentee, relief="groove",
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

mentor_list_box = Frame(mentee_welcomepg, bg='white', width=1000, height=600, borderwidth=2, relief=RAISED)
mentor_list_box.grid(row=0, column=0, columnspan=3)
# mentor_list_box.grid_propagate(False)

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

welcome_label = Label(mentor_list_box, text=f'DACAT MENTORSHIP\nClick on each mentor to explore what they have to offer...', font=('Bodoni MT', 25),
                      bg='white')
welcome_label.grid(row=0, column=0, columnspan=3)

buttonRock = tkinter.Button(mentor_list_box, image=theRock)
buttonRock.bind("<Button>", lambda e: NewWindow(mentor_list_box))
buttonRock.grid(row=1, column=0)
rock_label = Label(mentor_list_box, text=f'Computer Information Systems', font=('Bodoni MT', 12),
                   bg='white')
rock_label.grid(row=2, column=0)

buttonZuck = tkinter.Button(mentor_list_box, image=zuckerberg)
buttonZuck.bind("<Button>", lambda e: NewWindow2(mentor_list_box))
buttonZuck.grid(row=1, column=1)
zuck_label = Label(mentor_list_box, text=f'Computer Science & Management', font=('Bodoni MT', 12),
                   bg='white')
zuck_label.grid(row=2, column=1)

buttonNat = tkinter.Button(mentor_list_box, image=portman)
buttonNat.bind("<Button>", lambda e: NewWindow3(mentor_list_box))
buttonNat.grid(row=1, column=2)
nat_label = Label(mentor_list_box, text=f'Finance & Data Analytics', font=('Bodoni MT', 12),
                  bg='white')
nat_label.grid(row=2, column=2)

buttonwalhberg = tkinter.Button(mentor_list_box, image=mwahlberg)
buttonwalhberg.bind("<Button>", lambda e: NewWindow1(mentor_list_box))
buttonwalhberg.grid(row=3, column=0)
walhberg_label = Label(mentor_list_box, text=f'Software Development & Communications', font=('Bodoni MT', 10),
                       bg='white')
walhberg_label.grid(row=4, column=0)

buttonbill = tkinter.Button(mentor_list_box, image=gates)
buttonbill.bind("<Button>", lambda e: NewWindow4(mentor_list_box))
buttonbill.grid(row=3, column=1)
bill_label = Label(mentor_list_box, text=f'Computer Information Systems', font=('Bodoni MT', 12),
                   bg='white')
bill_label.grid(row=4, column=1)

editProfile_button = Button(window, font=('Bodoni MT', 17), text='Edit User Profile',
                            fg='black')
mentee_logout_button = Button(window, font=('Bodoni MT', 17), text='Log Out',
                              fg='black', command=mentee_logout)
date_time = Label(window)


############################################################################################################ EDIT PROFILE PAGE




user_profile_frame = Frame(window, bg='white', width=1280, height=800, borderwidth=1)


current_name_label = tkinter.Label(user_profile_frame, text="Current Username",bg='white')
current_name_label.grid(row=0, column=0)
# current_email_label = tkinter.Label(user_profile_frame, text="Current Email",bg='white')
# current_email_label.grid(row=0, column=1)
current_password_label = tkinter.Label(user_profile_frame, text="Current Password",bg='white')
current_password_label.grid(row=0, column=2)


name_label = tkinter.Label(user_profile_frame, text="New Username",bg='white')
name_label.grid(row=3, column=0)
# email_label = tkinter.Label(user_profile_frame, text="New Email",bg='white')
# email_label.grid(row=3, column=1)
password_label = tkinter.Label(user_profile_frame, text="New Password",bg='white')
password_label.grid(row=3, column=2)


name_entry = tkinter.Entry(user_profile_frame)
# email_entry = tkinter.Entry(user_profile_frame)
password_entry = tkinter.Entry(user_profile_frame)

currentName_entry = tkinter.Entry(user_profile_frame, textvariable=(mentee_username), state='readonly')
currentName_entry.grid(row=2, column=0)
currentPassword_entry = tkinter.Entry(user_profile_frame, textvariable=(mentee_password), state='readonly')
currentName_entry.grid(row=2, column=1)
# currentEmail_entry = tkinter.Entry(user_profile_frame, textvariable=(mentee_email), state='readonly')
# currentName_entry.grid(row=2, column=2)

edit_success_label = Label(user_profile_frame, font=('Bodoni MT', 12),bg='white', wraplength=210)
edit_success_label.grid(columnspan=3, row=7, column=0)



name_entry.grid(row=4, column=0)
# email_entry.grid(row=4, column=1)
password_entry.grid(row=4, column=2)

currentName_entry.grid(row=2, column=0)
# currentEmail_entry.grid(row=2, column=1)
currentPassword_entry.grid(row=2, column=2)


edit_button = Button(user_profile_frame,command=overwrite_user_info, font=('Bodoni MT', 12), text='Edit Profile',
                       fg='black', relief="groove")
edit_button.grid(row=5, column=0, columnspan=3)



editProfile_button = Button(window,command=editProfilePage, font=('Bodoni MT', 12), text='Edit User Profile',
                       fg='black')
logout_button = Button(window, font=('Bodoni MT', 20), text='Log Out',
                       fg='black')
date_time = Label(window)

# editProfile_button.grid(row=0, column=0,pady=8, sticky=N)
# mentee_logout_button.grid(row=0, column=0, pady=8, sticky=NE)
# date_time.grid(row=0, column=0, pady=10,padx=8, sticky=NW)

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
# select_button = Button(mentor_list_box, command=select_button_click, font=('Bodoni MT', 20), text='Select',
#                        relief=GROOVE, bg='black', fg='white')
# select_button.grid(row=5, column=0, columnspan=3)

send_message_button = Button(mentor_list_box, font=('Bodoni MT', 17), text='Send Message',
                             fg='black', relief=GROOVE, command=sendMessage)
send_message_button.grid(row=6, column=0, columnspan=4, pady=5)

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
mentor_label = Label(box2, text='Mentor\n Login to your Account', font=('Bodoni MT', 20, 'bold'), fg='black',
                     bg='white')
mentor_label.grid(columnspan=4, row=1, column=0)

# Login_label = Label(box2, text='Login to your Account', width=40, font=('Open Sans', 14), fg='black', bg= 'white')
# Login_label.grid(row=2)

mentor_message_label = Label(box2, justify=CENTER, font=('Bodoni MT', 10), bg='white', wraplength=210)
mentor_message_label.grid(columnspan=3, row=2, column=0)

# label for username and password
mentor_username_label = Label(box2, text='Username', fg='black', font=('Calibri', 12, 'bold'), bg='#fbfbfb')
mentor_username_label.grid(columnspan=1, row=3, column=0, pady=20)
mentor_password_label = Label(box2, font=('Calibri', 12, 'bold'), text='Password', bg='white')
mentor_password_label.grid(columnspan=1, row=4, column=0)

# # BOX 1, USER & PASSWORD ENTRY BOXES
mentor_username_entry = Entry(box2, textvariable=mentor_username, justify=LEFT, width=20, font=('Calibri', 11))
mentor_username_entry.grid(row=3, column=1, pady=20, padx=10, sticky=W)
mentor_password_entry = Entry(box2, textvariable=mentor_password, justify=LEFT, width=20, font=('Calibri', 11),
                              show="*")
mentor_password_entry.grid(row=4, column=1, padx=10, sticky=W)

# Login button
mentor_login_button = Button(box2, command=mentor_login, font=('Bodoni MT', 12), text='Log In',
                             relief=FLAT, bg='#ffa440', fg='white', width=10)
mentor_login_button.grid(row=5, column=0, columnspan=3, pady=30, sticky=N)

# contact button
back_button = Button(box2, font=('Bodoni MT', 12), text='Back',
                     fg='black', width=8, command=back_mentor, relief="groove")
back_button.grid(row=7, column=0, pady=10, padx=10)

# create account button
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

Login_label = Label(create_box, text='Create Your Mentor Account', width=40, font=('Bodoni MT', 20), fg='black',
                    bg='white')
Login_label.grid(columnspan=3, row=0, column=0, pady=20)

mentor_name_label = Label(create_box, text='Enter Full Name: ', justify=CENTER, font=('Calibri', 12), bg='white',
                          fg='black')
mentor_name_label.grid(row=1, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_name_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_name_textbox.grid(row=1, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newusername_label = Label(create_box, text='Enter Username: ', justify=CENTER, font=('Calibri', 12), bg='white',
                          fg='black')
newusername_label.grid(row=2, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newusername_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_newusername_textbox.grid(row=2, column=1, pady=1, padx=100, sticky=W, columnspan=2)

newpassword_label = Label(create_box, text='Enter Password: ', justify=CENTER, font=('Calibri', 12), bg='white',
                          fg='black')
newpassword_label.grid(row=3, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_newpassword_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_newpassword_textbox.grid(row=3, column=1, pady=1, padx=100, sticky=W, columnspan=2)

email_label = Label(create_box, text='Enter Email: ', justify=CENTER, font=('Calibri', 12), bg='white', fg='black')
email_label.grid(row=4, column=0, pady=5, padx=100, sticky=W, columnspan=2)
mentor_email_textbox = Entry(create_box, justify=LEFT, font=('Calibri', 12))
mentor_email_textbox.grid(row=4, column=1, pady=1, padx=100, sticky=W, columnspan=2)

mentor_q1_label = Label(create_box, text='\nPlease enter your major:', justify=CENTER,
                        font=('Bodoni MT', 12),
                        bg='white', fg='black')
mentor_q1_label.grid(row=5, column=0, pady=2, padx=50, columnspan=3)

# blank_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Calibri', 12), fg='black')
# blank_label.grid(row=6, column=0, pady=30, columnspan=3)

mentor_q1_entry = Entry(create_box, font=('Arial', 12), width=60, textvariable=mentor_description)
# mentee_q1_entry.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.4)
mentor_q1_entry.grid(row=7, column=0, pady=2, padx=50, columnspan=3)

mentor_q2_label = Label(create_box, text='Please provide a brief description for yourself:', justify=CENTER,
                        font=('Bodoni MT', 12),
                        bg='white', fg='black')
mentor_q2_label.grid(row=8, column=0, pady=2, padx=50, columnspan=3)
# blank2_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Calibri', 12), fg='black')
# blank2_label.grid(row=9, column=0, pady=30, columnspan=2)


mentor_q2_entry = Entry(create_box, font=('Arial', 12), width=60, textvariable=mentor_description2)
# mentor_q2_entry.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.6)
mentor_q2_entry.grid(row=9, column=0, pady=2, padx=50, columnspan=3)

upload_button = Button(create_box, text='Upload Profile Picture',
   width=20,command = lambda:upload_file())
upload_button.grid(row=10,column=1)

create_button = Button(create_box, font=("Bodoni MT", 12), text='Create', width=10, command=add_new_mentor, relief="groove",
                       bg='#ffa440', fg='white')
create_button.grid(column=0, row=0, pady=30, columnspan=3, sticky=E)

mentor_create_label = Label(create_box, text=' ', width=45, bg='white', font=('Calibri', 12), fg='black')
mentor_create_label.grid(row=11, column=0, pady=30, columnspan=3)

home_button = Button(create_box, command=mentor_back_to_login, font=('Bodoni MT', 12), text='Back to Login',
                       fg='black', relief="groove")
home_button.grid(row=0, column=0, columnspan=3, sticky=W)

# blank_label = Label(create_box, text='\n\n\n ', width=60, bg='white', font=('Calibri', 12), fg='black')
# blank_label.grid(row=5, column=0, pady=30, columnspan=3)
#

#
# create_button = Button(create_box, font=("Bodoni MT", 12), text='Create', width=10, command=add_new_mentor, relief=FLAT,
#                        bg='#ffa440', fg='white')
# create_button.grid(column=0, row=7, pady=30, columnspan=3)
#
# mentor_create_label = Label(create_box, text=' ', width=60, bg='white', font=('Calibri', 12), fg='black')
# mentor_create_label.grid(row=8, column=0, pady=30, columnspan=3)
#
# home_button = Button(create_box, command=mentor_back_to_login, font=('Bodoni MT', 12), text='Back to Login',
#                      fg='black', relief="groove")
# home_button.grid(row=9, column=0, columnspan=3)

################################################### MENTOR WELCOME
mentor_welcomepg = Frame(window, width=1920, height=1080)

mentor_logout_button = Button(window, font=('Bodoni MT', 17), text='Log Out',
                              fg='black', command=mentor_logout)

mentee_list_box = Frame(mentor_welcomepg, bg='white', relief=FLAT, width=600, height=630)
mentee_list_box.grid(row=1, column=0, rowspan=5, columnspan=4, pady=100)

mentee_list = ttk.Treeview(mentee_list_box, columns=(1, 2, 3, 4), show='headings', height='16')
mentee_list.grid(row=0, column=0, rowspan=16, columnspan=4)

mentee_list.heading(1, text='Username', anchor='center')
mentee_list.heading(2, text='Full Name', anchor='center')
mentee_list.heading(3, text='Email', anchor='center')
mentee_list.heading(4, text='Number', anchor='center')

mentee_list.column('#1', anchor='w', width=140, stretch=True)
mentee_list.column('#2', anchor='w', width=140, stretch=False)
mentee_list.column('#3', anchor='w', width=140, stretch=False)
mentee_list.column('#4', anchor='w', width=140, stretch=False)

send_message_buttonm = Button(mentee_list_box, font=('Bodoni MT', 17), text='Send Message',
                              fg='black', relief=GROOVE, command=sendMessageToMentee)
send_message_buttonm.grid(row=15, column=0, columnspan=4)



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
