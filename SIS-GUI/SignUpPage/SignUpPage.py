from tkinter import *
from pathlib import Path
import account

# Frame for Sign up page
class SignUpPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    # SignUpPage init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # error image with red border
        self.imgError = PhotoImage(file=self.relative_to_assets("imgErrorEntry.png"))

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating response label
        self.response = Label(canvas, anchor="nw", bg="#093545", fg="#52EFA0", font=("LexendDeca Regular", 16 * -1))
        self.response.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign up label
        canvas.create_text(528.0, 78.0, anchor="nw", text="Sign up", fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 160.0, anchor="nw", text="Sign up to start managing student information", fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(490.0, 210.0, anchor="nw", text="Email", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.email = StringVar()
        self.email.trace("w", self.reset_bg1_border)
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entryBg1 = Label(self, image=self.imgEntry1, bg="#093545")
        self.entryBg1.place(x=490, y=229.0)
        self.entry1 = Entry(self, textvariable=self.email, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry1.place(x=501.0, y=232.0, width=280.0, height=43.0)

        # creating email response message
        self.emailResponse = Label(canvas, anchor="nw", bg="#093545", fg="#F04C42", font=("LexendDeca Regular", 11 * -1))
        self.emailResponse.place(x=495, y=276)

        # creating password label
        canvas.create_text(491.0, 300.0, anchor="nw", text="Password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.pwd = StringVar()
        self.pwd.trace("w", self.reset_bg2_border)
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entryBg2 = Label(self, image=self.imgEntry2, bg="#093545")
        self.entryBg2.place(x=490, y=317.0)
        self.entry2 = Entry(self, textvariable=self.pwd, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry2.place(x=501.0, y=320.0, width=280.0, height=43.0)

        # creating password response message
        self.pwdResponse = Label(canvas, anchor="nw", bg="#093545", fg="#F04C42", font=("LexendDeca Regular", 11 * -1))
        self.pwdResponse.place(x=495, y=364)

        # creating confirm password label
        canvas.create_text(491.0, 390.0, anchor="nw", text="Confirm password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating confirm password entry
        self.confirm = StringVar()
        self.confirm.trace("w", self.reset_bg3_border)
        self.imgEntry3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entryBg3 = Label(self, image=self.imgEntry3, bg="#093545")
        self.entryBg3.place(x=490, y=407.0)
        self.entry3 = Entry(self, textvariable=self.confirm, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry3.place(x=501.0, y=410.0, width=280.0, height=43.0)

        # creating confrim password response message
        self.confirmResponse = Label(canvas, anchor="nw", bg="#093545", fg="#F04C42", font=("LexendDeca Regular", 11 * -1))
        self.confirmResponse.place(x=495, y=454)

        # creating create account button
        self.imgCreate = PhotoImage(file=self.relative_to_assets("btnCreate.png"))
        btnCreate = Button(self, image=self.imgCreate, borderwidth=0, highlightthickness=0, command=lambda: self.create(controller), relief="flat")
        btnCreate.place(x=491.0, y=486.0, width=300.0, height=45.0)

        # creating label do you have an account
        canvas.create_text(491.0, 554.0, anchor="nw", text="Do you have an account?", fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign in button
        self.imgSignIn = PhotoImage(file=self.relative_to_assets("btnSignIn.png"))
        btnSignIn = Button(self, image=self.imgSignIn, borderwidth=0, highlightthickness=0, command=lambda: self.to_signin(controller), relief="flat")
        btnSignIn.place(x=737.0, y=554.0, width=59.0, height=21.0)


    # transition to the sign in page
    def to_signin(self, controller):
        self.reset_all()
        controller.show_frame("SignInPage", controller.id)


    # creating an account
    def create(self, controller):
        email, pwd, confirm_pwd = self.entry1.get(), self.entry2.get(), self.entry3.get()
        self.clear_text()

        # if email, password, and confirm password are all empty
        if email == pwd == confirm_pwd == "":
            self.emailResponse["text"] = self.pwdResponse["text"] = self.confirmResponse["text"] = "This field is required"
            self.entryBg1["image"] = self.entryBg2["image"] = self.entryBg3["image"] = self.imgError
            return

        # if email only is empty
        if email == "":
            self.emailResponse["text"] = "This field is required"
            self.entryBg1["image"] = self.imgError
            return

        # both password and confirm password are empty
        if pwd == confirm_pwd == "":
            self.pwdResponse["text"] = self.confirmResponse["text"] = "This field is required"
            self.entryBg2["image"] = self.entryBg3["image"] = self.imgError
            return

        # for student
        if controller.id == "student":
            self.sign_up("Student_Credentials.txt", email, pwd, confirm_pwd)
        # for admin
        else:
            self.sign_up("Admin_Credentials.txt", email, pwd, confirm_pwd)


    # sign up process
    def sign_up(self, filename, email, pwd, confirm_pwd):
        sign_up_id = account.signup(filename, email, pwd, confirm_pwd)

        # The email already exist.
        if sign_up_id == 1:
            self.emailResponse["text"] = "The email already exist."
            self.entryBg1["image"] = self.imgError
        # The password confirmation does not match.
        elif sign_up_id == 2:
            self.confirmResponse["text"] = "The password confirmation does not match."
            self.entryBg2["image"] = self.entryBg3["image"] = self.imgError

        # You have registered successfully!
        else:
            self.response["text"] = "You have registered successfully!"
            self.response.place_configure(x=525, y=180)


    # clearing entry inputs
    def clear_text(self):
        self.response.place_forget()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)


    # reset entry background 1 border
    def reset_bg1_border(self, *args):
        self.entryBg1.configure(image=self.imgEntry1)
        self.emailResponse.configure(text="")


    # reset entry background 2 border
    def reset_bg2_border(self, *args):
        self.entryBg2.configure(image=self.imgEntry1)
        self.pwdResponse.configure(text="")


    # reset entry background 3 border
    def reset_bg3_border(self, *args):
        self.entryBg3.configure(image=self.imgEntry1)
        self.confirmResponse.configure(text="")


    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_text()
        self.reset_bg1_border()
        self.reset_bg2_border()
        self.reset_bg3_border()


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)