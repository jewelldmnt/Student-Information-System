from tkinter import *
from tkinter import ttk
from pathlib import Path
from Database import view


class ViewStudent(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    # view student init method
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # creating this frame canvas
        self.canvas = Canvas(self, bg="#093545", height=720, width=987, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        self.canvas.create_image(347.0, 664.0, image=self.curvy)

        # creating the view student label
        self.canvas.create_text(385.0, 40.0, text="VIEW STUDENT", anchor="nw", fill="#FFFFFF", font=("LexendDeca Bold", 36 * -1, "underline"))

        # creating list of student information label
        self.canvas.create_text(395.0, 106.0, text="LIST OF STUDENT INFORMATION", anchor="nw", fill="#FFFFFF", font=("LexendDeca Bold", 16 * -1))

        # creating total number label
        self.lblTotal = Label(self.canvas, bg="#27595E", anchor="nw", fg="#FFFFFF", font=("LexendDeca Bold", 16 * -1))
        self.lblTotal.place(x=605.0, y=683.0)
        

    # creation of the table of student information
    def view_information(self):
        total_students = view.number_of_students()

        # creating the main frame
        self.main_frame = Frame(self.canvas, width=835, height=538, bg="#0B4D65")
        self.main_frame.place(x=75, y=133)

        # creating the canvas for the scrollbar
        self.in_canvas = Canvas(self.main_frame, width=835, height=538, bg="#0B4D65", highlightthickness=0.5, highlightbackground="black")
        self.in_canvas.pack(side=LEFT, fill=BOTH, expand=True, ipadx=2)

        # making the scrollbar of the canvas
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.in_canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        # configuring the canvas scrollbar properties
        self.in_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.in_canvas.bind("<Configure>", lambda e: self.in_canvas.configure(scrollregion=self.in_canvas.bbox("all")))

        # making a window inside a canvas in the main frame
        self.table_frame = Frame(self.in_canvas, width=835, height=538, bg="#0B4D65")
        self.in_canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        # creating no students label
        self.lblNone = Label(self.table_frame, anchor="nw", bg="#0B4D65", fg="#FFFFFF", font=("LexendDeca Regular", 30 * -1))

        # displaying student information through loop
        self.imgTable = PhotoImage(file=self.relative_to_assets("imgTable1.png"))

        if total_students == 0:
            self.lblNone.configure(text="NO STUDENT FOUND")
            self.lblNone.place(x=261, y=250)
        else:
            view.display_students(self)
            self.lblNone.configure(text="")
            self.lblNone.place_forget()

        # display total number of students
        self.lblTotal.configure(text=f"TOTAL NUMBER OF STUDENTS: {total_students}")


    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)