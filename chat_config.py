from tkinter import *
from tkinter import ttk
from threading import *
import socketio 
import json

class Chat():
    
    sio = socketio.Client()
    def __init__(self,current_user) -> None:
        self.master = Tk()
        self.messageVar = StringVar(self.master)
        self.sio.connect('http://localhost:3000')
        print('SOCKET_ID : ', self.sio.sid)
        self.sio.emit('register', {'username':current_user})
        print(f'Sender {current_user}')
        self.master.wm_title("Message Client")
        self.master.withdraw()
        self.master.deiconify()
        self.master.geometry('600x450')
        self.master.resizable(0,0)

        labelframeMessages = LabelFrame(self.master, text="All messages")  
        labelframeMessages.pack(fill="both", expand="yes") 

        self.messagesList = Listbox(labelframeMessages)
        self.messagesList.pack(expand=True,fill=BOTH)

        m_file = open('mentors.json')
        mentees_accounts = json.load(m_file)
        m_file.close()

        usernames = []
        for user in mentees_accounts.keys():
                usernames.append(user)
        print(usernames)
        self.selectedUser = StringVar()
        labelframeSelect = LabelFrame(self.master,text='Select a Person to chat with')
        labelframeSelect.pack(expand="yes")
        self.select = ttk.Combobox(labelframeSelect,textvariable=self.selectedUser)
        self.select.pack(expand=True,ipady=5,ipadx=230)
        self.select['values'] = tuple(usernames)
        self.select.current(0)
        self.select.bind('<<ComboboxSelected>>',self.get_socket_id)

        labelframeInput = LabelFrame(self.master, text="Enter message")  
        labelframeInput.pack(fill="both", expand="yes") 
        text = Entry(labelframeInput,textvariable=self.messageVar)


        labelframeSend= LabelFrame(self.master, text="Send Message")  
        labelframeSend.pack(fill="both", expand="yes") 

        self.final_message_reciverVar = StringVar()

        btn = Button(labelframeSend,text="Send Message",command=lambda:self.sendPrivateMessage(self.final_message_reciverVar,self.messageVar))
        cncl = Button(labelframeSend,text="Cancel",command=self.master.destroy)
        text.pack(expand=True,ipady=50,ipadx=230)
        btn.pack()
        cncl.pack()
        self.master.mainloop()

    def get_socket_id(self,evt):
        f = open('mentors.json')
        mentors_accounts = json.load(f)
        f.close()
        selected_user = self.select.get()
        print(f'selected user {selected_user}')
        for mentor in mentors_accounts.keys():
            if mentor == selected_user:
                socketid = mentors_accounts[selected_user]['SOCKET_ID']
                print(socketid)
                self.final_message_reciverVar.set(socketid)
                break

        

    def sendPrivateMessage(self,to,message):
        self.sio.emit('group_posted', {
                    'to':to.get(),
                    'message':message.get()
                })
        self.messagesList.insert(self.messagesList.size()+1,'YOU : '+message.get())
        self.messageVar.set("")

    @sio.on('newconnection')
    def connect():
        print('new user connected')

    @sio.event
    def message(self,data):
        print('I received a message!')
        self.messagesList.insert(0,"Hey there")

    @sio.on('group_posted')
    def on_message(self,data):
        print(data)
        self.messagesList.insert(self.messagesList.size()+1,'RECEIVED : '+data)
        print('I received a message!')

    @sio.on('connection')
    def on_user_joined(self):
        print('user joined')