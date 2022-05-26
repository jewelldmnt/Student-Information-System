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

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#093545", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating response label
        self.response = Label(canvas, text="", anchor="nw", bg="#093545", font=("LexendDeca Regular", 16 * -1))
        self.response.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating sign in label
        canvas.create_text(541.0, 174.0, anchor="nw", text="Sign in", fill="#FFFFFF", font=("LexendDeca Regular", 64 * -1))

        # creating starting label
        canvas.create_text(485.0, 260.0, anchor="nw", text="Sign in to start managing student information", fill="#FFFFFF", font=("LexendDeca Regular", 16 * -1))

        # creating email label
        canvas.create_text(490.0, 321.0, anchor="nw", text="Email", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.imgEntry1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        canvas.create_image(640.0, 363.5, image=self.imgEntry1)
        self.entry1 = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry1.place(x=500.0, y=341.0, width=280.0, height=43.0)

        # creating password label
        canvas.create_text(490.0, 398.0, anchor="nw", text="Password", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating password entry
        self.imgEntry2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(640.0, 440.5, image=self.imgEntry2)
        self.entry2 = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entry2.place(x=500.0, y=418.0, width=280.0, height=43.0)

        # creating login button
        self.imgLogin = PhotoImage(file=self.relative_to_assets("btnLogin.png"))
        btnLogin = Button(self, image=self.imgLogin, borderwidth=0, highlightthickness=0, command=lambda: self.to_menu(controller), relief="flat")
        btnLogin.place(x=491.0, y=486.0, width=300.0, height=45.0)

        # creating label do you have an account
        canvas.create_text(490.0, 554.0, anchor="nw", text="Don't have an account?", fill="#FFFFFF", font=("Montserrat Medium", 14 * -1))

        # creating sign up button
        self.imgSignUp = PhotoImage(file=self.relative_to_assets("btnSignUp.png"))
        btnSignUp = Button(self, image=self.imgSignUp, borderwidth=0, highlightthickness=0, command=lambda: self.to_signup(controller), relief="flat")
        btnSignUp.place(x=731.0, y=551.0, width=63.0, height=25.0)


    # transition to the sign up page
    def to_signup(self, controller):
        self.clear_text()
        self.response.place_forget()
        controller.show_frame("SignUpPage", controller.id)


    # transition to the right menu
    def to_menu(self, controller):
        email = self.entry1.get()
        password = self.entry2.get()
        self.clear_text()

        # for students
        if controller.id == "student":
            filename = "Student_Credentials.txt"
            sign_in = account.login(filename, email, password)

            # Logged in successfully
            if sign_in == 1:
                self.response.place_forget()
                controller.show_frame("StudentMenu")
            # Account does not exist!
            elif sign_in == 2:
                self.response.configure(text="Account does not exist!", fg="#F04C42")
                self.response.place_configure(x=560, y=286)
            # Incorrect email or password!
            else:
                self.response.configure(text="Incorrect password!", fg="#E7A90A")
                self.response.place_configure(x=577, y=286)

        # for admin
        else:
            filename = "Admin_Credentials.txt"
            sign_in = account.login(filename, email, password)

            # Logged in successfully
            if sign_in == 1:
                self.response.place_forget()
                controller.show_frame("AdminMenu")
            # Account does not exist!
            elif sign_in == 2:
                self.response.configure(text="Account does not exist!", fg="#F04C42")
                self.response.place_configure(x=560, y=286)
            # Incorrect email or password!
            else:
                self.response.configure(text="Incorrect password!", fg="#E7A90A")
                self.response.place_configure(x=577, y=286)


    # clearing entry inputs
    def clear_text(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)