# hard code new mentor
"jake": {"Password": "jake1", "Email": "jake@asu.edu"}

#images
avatar = Image.open('avatar.jpeg')
new_width8 = 200
new_height8 = 200
avatar2 = avatar.resize((new_width9, new_height9), Image.Resampling.LANCZOS)
avatar2.save('avatar.jpeg')
ava = ImageTk.PhotoImage(avatar2)

#under mentor create account
buttonavatar = tkinter.Button(mentor_list_box, image=ava)
buttonavatar.bind("<Button>", lambda e: NewWindow5(mentor_list_box))
buttonavatar.grid(row=3, column=0)
avatar_label = Label(mentor_list_box, text=f'Computer Information Systems', font=('Bodoni MT', 12),
                     bg='white')
avatar_label.grid(row=4, column=0)

#class
class NewWindow5(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Mentor Profile")
        self.geometry("1280x800")
        label = Label(self, text="Hi My names Jake, a current professional in the industry")
        label.grid()