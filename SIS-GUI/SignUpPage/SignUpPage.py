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

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating response label
        self.response = Label(canvas, text="", anchor="nw", bg="#093545", font=("LexendDeca Regular", 16 * -1))
        self.response.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign up label
        canvas.create_text(530.0, 93.0, anchor="nw", text="Sign up", fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 181.0, anchor="nw", text="Sign up to start managing student information", fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(491.0, 240.0, anchor="nw", text="Email", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        canvas.create_image(641.0, 282.5, image=self.imgEntry1)
        self.entry1 = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry1.place(x=501.0, y=260.0, width=280.0, height=43.0)

        # creating password label
        canvas.create_text(491.0, 317.0, anchor="nw", text="Password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(641.0, 359.5, image=self.imgEntry2)
        self.entry2 = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry2.place(x=501.0, y=337.0, width=280.0, height=43.0)

        # creating confirm password label
        canvas.create_text(491.0, 394.0, anchor="nw", text="Confirm password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating confirm password entry
        self.imgEntry3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        canvas.create_image(641.0, 436.5, image=self.imgEntry3)
        self.entry3 = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry3.place(x=501.0, y=414.0, width=280.0, height=43.0)

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
        self.clear_text()
        self.response.place_forget()
        controller.show_frame("SignInPage", controller.id)


    # creating an account
    def create(self, controller):
        email = self.entry1.get()
        pwd = self.entry2.get()
        confirm_pwd = self.entry3.get()
        self.clear_text()

        # if there is insufficient data 
        if "" in (email, pwd, confirm_pwd):
            self.response.configure(text="Insufficient Data!", fg="#F04C42")
            self.response.place_configure(x=585, y=207)
            return

        # for student
        if controller.id == "student":
            filename = "Student_Credentials.txt"
            sign_up = account.signup(filename, email, pwd, confirm_pwd)

            # You have registered successfully!
            if sign_up == 1:
                self.response.configure(text="You have registered successfully!", fg="#52EFA0")
                self.response.place_configure(x=525, y=207)
            # Password is not same as above!
            elif sign_up == 2:
                self.response.configure(text="Password is not same as above!", fg="#F04C42")
                self.response.place_configure(x=530, y=207)
            # The email is already exist!
            else:
                self.response.configure(text="The email is already exist!", fg="#E7A90A")
                self.response.place_configure(x=550, y=207)

        # for admin
        else:
            filename = "Admin_Credentials.txt"
            sign_up = account.signup(filename, email, pwd, confirm_pwd)

            # You have registered successfully!
            if sign_up == 1:
                self.response.configure(text="You have registered successfully!", fg="#52EFA0")
                self.response.place_configure(x=525, y=207)
            # Password is not same as above!
            elif sign_up == 2:
                self.response.configure(text="Password is not same as above!", fg="#F04C42")
                self.response.place_configure(x=530, y=207)
            # The email is already exist!
            else:
                self.response.configure(text="The email is already exist!", fg="#E7A90A")
                self.response.place_configure(x=550, y=207)


    # clearing entry inputs
    def clear_text(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
