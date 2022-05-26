from tkinter import *
from pathlib import Path
from Database import update, search


class UpdateStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    current_btn, current_img = None, None


    # update student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        self.canvas = Canvas(self, bg="#093545", height=720, width=987, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        self.canvas.create_image(347.0, 664.0, image=self.curvy)

        # creating the update student label
        self.canvas.create_text(205.0, 40.0, text="UPDATE STUDENT INFORMATION", anchor="nw", fill="#FFFFFF", font=("LexendDeca Bold", 36 * -1, "underline"))

        # creating search bar label
        self.canvas.create_text(310.0, 106.0, text="Enter the student number to search", anchor="nw", fill="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating search bar entry
        self.imgSearch1 = PhotoImage(file=self.relative_to_assets("entry_search.png"))
        self.canvas.create_image(431.0, 149.5, image=self.imgSearch1)
        self.entrySearch = Entry(self, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))
        self.entrySearch.place(x=291.0, y=130.0, width=240.0, height=43.0)

        # creating search icon image
        self.iconSearch = PhotoImage(file=self.relative_to_assets("imgSearch.png"))
        self.canvas.create_image(555.0, 153.0, image=self.iconSearch)

        # creating search button
        self.imgSearch3 = PhotoImage(file=self.relative_to_assets("btnSearch.png"))
        btnSearch = Button(self, image=self.imgSearch3, borderwidth=0, highlightthickness=0, command=self.search_student, relief="flat")
        btnSearch.place(x=590.0, y=132.0, width=94.0, height=38.0)

        # creating error message label
        self.response = Label(self.canvas, text="Student number not found.", anchor="nw", bg="#093545", fg="#F04C41",
                              font=("LexendDeca Regular", 14 * -1))

        # creating student information label
        self.lblInfo = Label(self.canvas, anchor="nw", text="STUDENT INFORMATION", bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 18 * -1))

        # ----------------------------- creation of table part ------------------------------------------------ #

        # creating frame for the student info
        self.frame = Frame(self.canvas, width=835, height=387, bg="#093545")

        # creating success message label
        self.successMsg = Label(self.frame, text="Student information successfully updated!", anchor="nw",
                                bg="#093545", fg="#20DF7F", font=("LexendDeca Regular", 16 * -1))

        # creating the table image
        self.imgTable = PhotoImage(file=self.relative_to_assets("imgTable.png"))
        Label(self.frame, image=self.imgTable, width=835, height=210, bd=0, highlightthickness=0, relief="ridge").place(x=0, y=1)

        # creating the student number placeholder label
        lblStNo = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1, "bold"))
        lblStNo.place(x=143, y=8)

        # creating the last name placeholder label
        lblLN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblLN.place(x=166, y=43)

        # creating the first name placeholder label
        lblFN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblFN.place(x=166, y=76)

        # creating the middle name placeholder label
        lblMN = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblMN.place(x=166, y=114)

        # creating the email placeholder label
        lblEmail = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblEmail.place(x=166, y=149)

        # creating the contact placeholder label
        lblContact = Label(self.frame, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 16 * -1))
        lblContact.place(x=166, y=183)

        # store list of all labels
        self.labels = [lblStNo, lblLN, lblFN, lblMN, lblEmail, lblContact]

        # -------------------------- creation of updating info part -------------------------------------------- #

        # creating select the field you want to modify label
        Label(self.frame, text="Select the field that you want to modify:",
              bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 16 * -1)).place(x=0, y=220)

        # creating last name button
        self.imgLastN = PhotoImage(file=self.relative_to_assets("btnLastN.png"))
        btnLastN = Button(self.frame, image=self.imgLastN, borderwidth=0, highlightthickness=0, command=lambda: self.show_change_into(1, btnLastN, self.imgLastN), relief="flat")
        btnLastN.place(x=35.0, y=250.0, width=127.0, height=38.0)

        # creating first name button
        self.imgFirstN = PhotoImage(file=self.relative_to_assets("btnFirstN.png"))
        btnFirstN = Button(self.frame, image=self.imgFirstN, borderwidth=0, highlightthickness=0, command=lambda: self.show_change_into(2, btnFirstN, self.imgFirstN), relief="flat")
        btnFirstN.place(x=180.0, y=250.0, width=127.0, height=38.0)

        # creating middle name button
        self.imgMiddleN = PhotoImage(file=self.relative_to_assets("btnMiddleN.png"))
        btnMiddleN = Button(self.frame, image=self.imgMiddleN, borderwidth=0, highlightthickness=0, command=lambda: self.show_change_into(3, btnMiddleN, self.imgMiddleN), relief="flat")
        btnMiddleN.place(x=324.0, y=250.0, width=152.0, height=38.0)

        # creating email address button
        self.imgEmail = PhotoImage(file=self.relative_to_assets("btnEmail.png"))
        btnEmail = Button(self.frame, image=self.imgEmail, borderwidth=0, highlightthickness=0, command=lambda: self.show_change_into(4, btnEmail, self.imgEmail), relief="flat")
        btnEmail.place(x=493.0, y=250.0, width=164.0, height=38.0)

        # creating contact number button
        self.imgContactN = PhotoImage(file=self.relative_to_assets("btnContactN.png"))
        btnContactN = Button(self.frame, image=self.imgContactN, borderwidth=0, highlightthickness=0, command=lambda: self.show_change_into(5, btnContactN, self.imgContactN), relief="flat")
        btnContactN.place(x=674.0, y=250.0, width=137.0, height=38.0)

        # creating change into label
        self.lblChangeInto = Label(self.frame, text="Change into: ", anchor="nw", bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating change into entry
        self.new_info = StringVar()
        self.new_info.trace("w", self.show_confirmation_part)
        self.imgChangeInto = PhotoImage(file=self.relative_to_assets("entry_ChangeInto.png"))
        self.imgChIn = Label(self.frame, image=self.imgChangeInto, bg="#093545")
        self.entryChangeInto = Entry(self.frame, textvariable=self.new_info, bd=0, bg="#224957", highlightthickness=0, fg="silver", insertbackground="silver", font=("LexendDeca Regular", 14 * -1))

        # -------------------------- creation of confirmation part -------------------------------------------- #

        # creating confirmation label
        self.lblConfirm = Label(self.frame, text="Are you sure this information is correct?", bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 14 * -1))
        self.lblConfirm2 = Label(self.frame, text="By choosing yes, the previously saved data would be overwritten.", bg="#093545", fg="#FFFFFF", font=("LexendDeca Regular", 14 * -1))

        # creating yes button
        self.imgYes = PhotoImage(file=self.relative_to_assets("btnYes.png"))
        self.btnYes = Button(self.frame, image=self.imgYes, borderwidth=0, highlightthickness=0, command=self.update_student, relief="flat")

        # creating no button
        self.imgNo = PhotoImage(file=self.relative_to_assets("btnNo.png"))
        self.btnNo = Button(self.frame, image=self.imgNo, borderwidth=0, highlightthickness=0, command=self.enter_again, relief="flat")


    # --------------- Methods --------------- #

    # search student
    def search_student(self):
        if search.student_found(self.entrySearch.get()):
            self.response.place_forget()
            self.frame.place(x=78, y=227)
            self.lblInfo.place(x=385, y=200)
            search.show_results(self)
        else:
            self.response.place(x=345.0, y=180.0)
            self.frame.place_forget()
            self.lblInfo.place_forget()


    # update student
    def update_student(self):
        update.update_student(self.info_index, self.new_info.get())
        self.entryChangeInto.delete(0, END)
        self.hide_frame()
        self.search_student()


    # user clicked no, go back to changing what info again
    def enter_again(self):
        self.entryChangeInto.delete(0, END)
        self.hide_frame()
        self.search_student()


    # show ChangeInto buttons and entry box
    def show_change_into(self, index, button, image):
        self.info_index = index
        self.button_clicked(button, image)
        self.new_info.set(value="")

        # placing the change info label
        self.lblChangeInto.place(x=20, y=305)
        
        # placing the change info entry
        self.imgChIn.place(x=117, y=296)
        self.entryChangeInto.place(x=129.0, y=300.0, width=688.0, height=36.0)


    # show confirmation part if there is a text
    def show_confirmation_part(self, *args):
        new_info = self.new_info.get()

        # placing confirmation part
        if new_info != "":
            self.lblConfirm.place(x=378, y=345)
            self.lblConfirm2.place(x=221, y=365)
            self.btnYes.place(x=656.0, y=350.0, width=84.0, height=30.0)
            self.btnNo.place(x=753.0, y=350.0, width=84.0, height=30.0)
        # hide the confirmation part
        else:
            self.lblConfirm.place_forget()
            self.lblConfirm2.place_forget()
            self.btnYes.place_forget()
            self.btnNo.place_forget()


    # change button appearance when clicked
    def button_clicked(self, new_btn, new_img):
        self.reset_button_state()
        self.current_btn = new_btn
        self.current_img = new_img
        button_index = self.info_index

        if button_index == 1:
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnLastNCv.png"))
        elif button_index == 2:
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnFirstNCv.png"))
        elif button_index == 3:
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnMiddleNCv.png"))
        elif button_index == 4:
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnEmailCv.png"))
        elif button_index == 5:
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnContactNCv.png"))
        self.current_btn.configure(image=self.clicked_img)


    # reset the current button image
    def reset_button_state(self):
        if self.current_btn != None and self.current_img != None:
            self.current_btn.configure(image=self.current_img)


    # hide frame
    def hide_frame(self):
        self.reset_button_state()
        self.lblInfo.place_forget()
        self.frame.place_forget()
        self.lblChangeInto.place_forget()
        self.imgChIn.place_forget()
        self.entryChangeInto.place_forget()
        self.lblConfirm.place_forget()
        self.lblConfirm2.place_forget()
        self.btnYes.place_forget()
        self.btnNo.place_forget()


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
