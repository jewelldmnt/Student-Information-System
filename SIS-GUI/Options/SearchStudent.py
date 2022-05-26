from tkinter import *
from pathlib import Path
from Database import search


class SearchStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    
    
    # search student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        canvas = Canvas(self, bg="#093545", height=720, width=987, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        canvas.create_image(347.0, 664.0, image=self.curvy)

        # creating the search student label
        canvas.create_text(330.0, 40.0, text="SEARCH STUDENT", anchor="nw", fill="#FFFFFF", font=("LexendDeca Bold", 36 * -1, "underline"))

        # creating search bar label
        canvas.create_text(310.0, 126.0, text="Enter the student number to search", anchor="nw", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating search bar entry
        self.imgSearch1 = PhotoImage(file=self.relative_to_assets("entry_search.png"))
        canvas.create_image(431.0, 169.5, image=self.imgSearch1)
        self.entrySearch = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entrySearch.place(x=291.0, y=150.0, width=240.0, height=43.0)

        # creating search icon image
        self.iconSearch = PhotoImage(file=self.relative_to_assets("imgSearch.png"))
        canvas.create_image(555.0, 173.0, image=self.iconSearch)

        # creating search button
        self.imgSearch2 = PhotoImage(file=self.relative_to_assets("btnSearch.png"))
        btnSearch = Button(self, image=self.imgSearch2, borderwidth=0, highlightthickness=0, command=self.student_search, relief="flat")
        btnSearch.place(x=590.0, y=152.0, width=94.0, height=38.0)

        # creating error message label
        self.response = Label(canvas, text="Student number not found.", anchor="nw", bg="#093545", fg="#F04C41", font=("LexendDeca Regular", 14 * -1))

        # ----------------------------- creation of table part ------------------------------------------------ #

        # creating frame for the student info
        self.frame = Frame(canvas, width=835, height=347, bg="#093545")

        # creating success message label
        self.successMsg = Label(self.frame, text="Student information found!", anchor="nw", bg="#093545", fg="#20DF7F", font=("LexendDeca Regular", 16 * -1))
        self.successMsg.place(x=320, y=280)

        # creating student information label
        lblInfo = Label(self.frame, anchor="nw", text="STUDENT INFORMATION", bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 18 * -1))
        lblInfo.place(x=295, y=15)

        # creating the table image
        self.imgTable = PhotoImage(file=self.relative_to_assets("imgTable.png"))
        Label(self.frame, image=self.imgTable, width=835, height=210, bd=0, highlightthickness=0, relief="ridge").place(x=0, y=51)

        # creating the student number placeholder label
        lblStNo = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1, "bold"))
        lblStNo.place(x=143, y=58)

        # creating the last name placeholder label
        lblLN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblLN.place(x=166, y=93)

        # creating the first name placeholder label
        lblFN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblFN.place(x=166, y=126)

        # creating the middle name placeholder label
        lblMN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblMN.place(x=166, y=164)

        # creating the email placeholder label
        lblEmail = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblEmail.place(x=166, y=199)

        # creating the contact placeholder label
        lblContact = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblContact.place(x=166, y=233)

        # store list of all labels
        self.labels = [lblStNo, lblLN, lblFN, lblMN, lblEmail, lblContact]


    # --------------- Methods --------------- #

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)


    # searching for student
    def student_search(self):
        if search.student_found(self.entrySearch.get()):
            self.response.place_forget()
            self.frame.place(x=78, y=227)
            search.show_results(self)
        else:
            self.response.place(x=345.0, y=202.0)
            self.frame.place_forget()
        self.entrySearch.delete(0, END)


    # hide frame
    def hide_frame(self):
        self.frame.place_forget()