from tkinter import *
from pathlib import Path
import account


# Frame for sign in page
class SignInPage(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    # sign in page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # error image with red border
        self.imgError = PhotoImage(file=self.relative_to_assets("imgErrorEntry.png"))
        self.count = 0

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign in label
        canvas.create_text(540.0, 127.0, anchor="nw", text="Sign in", fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 213.0, anchor="nw", text="Sign in to start managing student information", fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(490.0, 249.0, anchor="nw", text="Email", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.email = StringVar()
        self.email.trace("w", self.reset_bg1_border)
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entryBg1 = Label(self, image=self.imgEntry1, bg="#093545")
        self.entryBg1.place(x=490, y=267.0)
        self.entry1 = Entry(self, textvariable=self.email, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry1.place(x=500.0, y=270.0, width=280.0, height=43.0)

        # creating email response message
        self.emailResponse = Label(canvas, anchor="nw", bg="#093545", fg="#F04C42", font=("LexendDeca Regular", 11 * -1))
        self.emailResponse.place(x=495, y=315)

        # creating password label
        canvas.create_text(490.0, 344.0, anchor="nw", text="Password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.pwd = StringVar()
        self.pwd.trace("w", self.reset_bg2_border)
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entryBg2 = Label(self, image=self.imgEntry1, bg="#093545")
        self.entryBg2.place(x=490, y=361.0)
        self.entry2 = Entry(self, textvariable=self.pwd, show="*", bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry2.place(x=500.0, y=364.0, width=245.0, height=43.0)

        # creating show or hide password button
        self.imgHide = PhotoImage(file=self.relative_to_assets("btnHide.png"))
        self.imgView = PhotoImage(file=self.relative_to_assets("btnView.png"))
        self.btnShowHide = Button(self, image=self.imgView, borderwidth=0, highlightthickness=0, command=self.show_or_hide_pass, relief="flat")
        self.btnShowHide.place(x=760, y=377, width=20, height=20)

        # creating password response message
        self.pwdResponse = Label(canvas, anchor="nw", bg="#093545", fg="#F04C42", font=("LexendDeca Regular", 11 * -1))
        self.pwdResponse.place(x=495, y=410)

        # creating login button
        self.imgLogin = PhotoImage(file=self.relative_to_assets("btnLogin.png"))
        btnLogin = Button(self, image=self.imgLogin, borderwidth=0, highlightthickness=0, command=lambda: self.to_menu(controller), relief="flat")
        btnLogin.place(x=490.0, y=442.0, width=300.0, height=45.0)

        # creating label do you have an account
        canvas.create_text(490.0, 510.0, anchor="nw", text="Don't have an account?", fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign up button
        self.imgSignUp = PhotoImage(file=self.relative_to_assets("btnSignUp.png"))
        btnSignUp = Button(self, image=self.imgSignUp, borderwidth=0, highlightthickness=0, command=lambda: self.to_signup(controller), relief="flat")
        btnSignUp.place(x=730.0, y=507.0, width=63.0, height=25.0)


    # transition to the sign up page
    def to_signup(self, controller):
        self.reset_all()
        controller.show_frame("SignUpPage", controller.id)


    # transition to the right menu
    def to_menu(self, controller):
        email = self.entry1.get()
        pwd = self.entry2.get()
        self.clear_text()

        # if email and password is both empty
        if email == pwd == "":
            self.emailResponse["text"] = self.pwdResponse["text"] = "This field is required"
            self.entryBg1["image"] = self.entryBg2["image"] = self.imgError
            return 

        # if email is empty
        if email == "":
            self.emailResponse["text"] = "This field is required"
            self.entryBg1["image"] = self.imgError
            return

        # if password is empty
        if pwd == "":
            self.pwdResponse["text"] = "This field is required"
            self.entryBg2["image"] = self.imgError
            return

        # for students
        if controller.id == "student":
            self.sign_in("Student_Credentials.txt", email, pwd, controller)
        # for admin
        else:
            self.sign_in("Admin_Credentials.txt", email, pwd, controller)

    
    # sign in process
    def sign_in(self, filename, email, pwd, controller):
        _id = controller.id
        sign_in_id = account.login(filename, email, pwd)

        # The account does not exist.
        if sign_in_id == 1:
            self.emailResponse["text"] = "The account does not exist"
            self.entryBg1["image"] = self.imgError
        # The password is incorrect.
        elif sign_in_id == 2:
            self.pwdResponse["text"] = "The password is incorrect"
            self.entryBg2["image"] = self.imgError
        # Logged in successfully
        else:
            controller.show_frame("StudentMenu" if _id == "student" else "AdminMenu")


    # show or hide password
    def show_or_hide_pass(self):
        if self.count % 2 == 0:
            self.btnShowHide["image"] = self.imgHide
            self.entry2.config(show="")
        else:
            self.btnShowHide["image"] = self.imgView
            self.entry2.config(show="*")

        self.count = 1 if self.count == 0 else 0


    # clearing entry inputs
    def clear_text(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)


    # reset entry background 1 border
    def reset_bg1_border(self, *args):
        self.entryBg1.configure(image=self.imgEntry1)
        self.emailResponse.configure(text="")


    # reset entry background 2 border
    def reset_bg2_border(self, *args):
        self.entryBg2.configure(image=self.imgEntry1)
        self.pwdResponse.configure(text="")


    # reset the entry backgrounds and entry responses
    def reset_all(self):
        self.clear_text()
        self.reset_bg1_border()
        self.reset_bg2_border()


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)