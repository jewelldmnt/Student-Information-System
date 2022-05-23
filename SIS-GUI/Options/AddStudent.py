from tkinter import *
from pathlib import Path
from database import add


class AddStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # add student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        canvas = Canvas(self, bg="#093545", height=720, width=987, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating response label
        self.response = Label(canvas, text="", anchor="nw", bg="#093545", font=("LexendDeca Regular", 16 * -1))
        self.response.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(347.0, 664.0, image=self.curvy)

        # creating add student label
        canvas.create_text(395.0, 35.0, anchor="nw", text="Add student", fill="#FFFFFF", font=("LexendDeca Light", 36 * -1))

        # creating student number label
        canvas.create_text(437.0, 166.0, anchor="nw", text="Student Number", fill="#FFFFFF", font=("LexendDeca Light", 14 * -1))

        # creating student number entry
        self.imgStuNum = PhotoImage(file=self.relative_to_assets("entry_StuNum.png"))
        canvas.create_image(492.0, 208.5, image=self.imgStuNum)
        self.entry_StuNum = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_StuNum.place(x=352.0, y=186.0, width=280.0, height=43.0)

        # creating last name label
        canvas.create_text(136.0, 285.0, anchor="nw", text="Last name", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating last name entry
        self.imgLastN = PhotoImage(file=self.relative_to_assets("entry_LastN.png"))
        canvas.create_image(172.0, 327.5, image=self.imgLastN)
        self.entry_LastN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_LastN.place(x=32.0, y=305.0, width=280.0, height=43.0)

        # creating first name label
        canvas.create_text(456.0, 285.0, anchor="nw", text="First name", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating first name entry
        self.imgFirstN = PhotoImage(file=self.relative_to_assets("entry_FirstN.png"))
        canvas.create_image(492.0, 327.5, image=self.imgFirstN)
        self.entry_FirstN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_FirstN.place(x=352.0, y=305.0, width=280.0, height=43.0)

        # creating middle name label
        canvas.create_text(767.0, 285.0, anchor="nw", text="Middle name", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating middle name entry
        self.imgMiddleN = PhotoImage(file=self.relative_to_assets("entry_MiddleN.png"))
        canvas.create_image(811.0, 327.5, image=self.imgMiddleN)
        self.entry_MiddleN = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_MiddleN.place(x=671.0, y=305.0, width=280.0, height=43.0)

        # creating email address label
        canvas.create_text(444.0, 404.0, anchor="nw", text="Email Address", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating email entry
        self.imgEmail = PhotoImage(file=self.relative_to_assets("entry_Email.png"))
        canvas.create_image(492.0, 446.5, image=self.imgEmail)
        self.entry_Email = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_Email.place(x=352.0, y=424, width=280.0, height=43.0)

        # creating contact number label
        canvas.create_text(436.0, 506.0, anchor="nw", text="Contact Number", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating contact number entry
        self.imgContNum = PhotoImage(file=self.relative_to_assets("entry_ContNum.png"))
        canvas.create_image(492.0, 548.5, image=self.imgContNum)
        self.entry_ContNum = Entry(self, bd=0, bg="#224957", highlightthickness=0)
        self.entry_ContNum.place(x=352.0, y=526.0, width=280.0, height=43.0)

        # creating submit button
        self.imgSubmit = PhotoImage(file=self.relative_to_assets("btnSubmit.png"))
        btnSubmit = Button(self, image=self.imgSubmit, borderwidth=0, highlightthickness=0,
                           command=lambda: self.to_add_student(), relief="flat")
        btnSubmit.place(x=391.0, y=620.0, width=212.0, height=46.0)

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def to_add_student(self):
        # creating a list of all entries of the user
        student_data = [self.entry_StuNum.get(), self.entry_LastN.get(), self.entry_FirstN.get(),
                        self.entry_MiddleN.get(), self.entry_Email.get(), self.entry_ContNum.get()]
        entry_count = 0
        for values in student_data:
            entry_count = (entry_count + 1 if values != "" else entry_count)
        self.clear_entries()

        # if all entries are filled
        if entry_count == 6:
            add.add(student_data)
            self.response.configure(text="Data successfully saved!", fg="#52EFA0")
            self.response.place_configure(x=402, y=107)

        # if not all entries are filled
        else:
            self.response.configure(text="Insufficient data!", fg="#F04C42")
            self.response.place_configure(x=430, y=107)

    def clear_entries(self):
        self.entry_StuNum.delete(0, END)
        self.entry_LastN.delete(0, END)
        self.entry_FirstN.delete(0, END)
        self.entry_MiddleN.delete(0, END)
        self.entry_Email.delete(0, END)
        self.entry_ContNum.delete(0, END)
