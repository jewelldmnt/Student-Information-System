from tkinter import *
from pathlib import Path
from Options import AddStudent as add, ViewStudent as view, \
    SearchStudent as search, UpdateStudent as update, DeleteStudent as delete


# Frame for admin menu page
class AdminMenu(Frame):
    # constants
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    current_btn, current_img = None, None


    # admin menu class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # temporary space taker for the panel
        temp = Frame(self, width=293)
        temp.pack(side="left")

        # initialize options container and frames in it
        self.container = Frame(self)
        self.container.pack(side="left", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        self.create_frames()

        # creating the whole canvas of the frame
        self.canvas = Canvas(self, bg = "#093545", height = 720, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # creating the bottom image for design
        self.curvy = PhotoImage(file=self.relative_to_assets("curvy.png"))
        self.canvas.create_image(640.0, 664.0, image=self.curvy)

        # creating panel menu
        self.canvas.create_rectangle(0.0, 0.0, 293.0, 720.0, fill="#214D5E", outline="")

        # creating delete students button
        self.imgDelete = PhotoImage(file=self.relative_to_assets("btnDelete.png"))
        btnDelete = Button(self.canvas, image=self.imgDelete, borderwidth=0, highlightthickness=0, command=lambda: self.show_option("DeleteStudent", btnDelete, self.imgDelete), relief="flat")
        btnDelete.place(x=41.0, y=439.0, width=212.0, height=46.0)

        # creating update students button
        self.imgUpdate = PhotoImage(file=self.relative_to_assets("btnUpdate.png"))
        btnUpdate = Button(self.canvas, image=self.imgUpdate, borderwidth=0, highlightthickness=0, command=lambda: self.show_option("UpdateStudent", btnUpdate, self.imgUpdate), relief="flat")
        btnUpdate.place(x=41.0, y=375.0, width=212.0, height=46.0)

        # creating search students button
        self.imgSearch = PhotoImage(file=self.relative_to_assets("btnSearch.png"))
        btnSearch = Button(self.canvas, image=self.imgSearch, borderwidth=0, highlightthickness=0, command=lambda: self.show_option("SearchStudent", btnSearch, self.imgSearch), relief="flat")
        btnSearch.place(x=41.0, y=311.0, width=212.0, height=46.0)

        # creating view students button
        self.imgView = PhotoImage(file=self.relative_to_assets("btnView.png"))
        btnView = Button(self.canvas, image=self.imgView, borderwidth=0, highlightthickness=0, command=lambda: self.show_option("ViewStudent", btnView, self.imgView), relief="flat")
        btnView.place(x=41.0, y=247.0, width=212.0, height=46.0)

        # creating add students button
        self.imgAdd = PhotoImage(file=self.relative_to_assets("btnAdd.png"))
        btnAdd = Button(self.canvas, image=self.imgAdd, borderwidth=0, highlightthickness=0, command=lambda: self.show_option("AddStudent", btnAdd, self.imgAdd), relief="flat")
        btnAdd.place(x=41.0, y=182.0, width=212.0, height=46.0)

        # creating menu label
        self.canvas.create_text(116.0, 139.0, anchor="nw", text="MENU",  fill="#FFFFFF", font=("LexendDeca Regular", 20 * -1))

        # creating quit button
        self.imgLogout = PhotoImage(file=self.relative_to_assets("btnLogout.png"))
        btnLogout = Button(self.canvas, image=self.imgLogout, borderwidth=0, highlightthickness=0, command=lambda: self.to_home_page(controller), relief="flat")
        btnLogout.place(x=41.0, y=665.0, width=90.0, height=27.0)

        # creating SIS label
        self.canvas.create_text(355.0, 35.0, anchor="nw", text="Student Management System",  fill="#FFFFFF", font=("LexendDeca Regular", 36 * -1))

        # creating students image bottom right
        self.imgStudents = PhotoImage(file=self.relative_to_assets("imgStudents.png"))
        self.canvas.create_image(1085.0, 509.0, image=self.imgStudents)


    # --------------- Methods --------------- #

    # creating frames for all options and rooting them in the main container
    def create_frames(self):
        optionsList = [add.AddStudent, view.ViewStudent, search.SearchStudent, update.UpdateStudent, delete.DeleteStudent]
        for f in optionsList:
            frame_name = f.__name__
            frame = f(self.container)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[frame_name] = frame


    # returning back to homepage
    def to_home_page(self, controller):
        self.reset_button_state()
        self.hide_pages_widgets()
        self.canvas.tk.call("raise", self.canvas._w)
        controller.show_frame("HomePage")


    # showing the called frame on top of everything
    def show_option(self, frame_name, button, image):
        # output the table as soon view student page was called
        if frame_name == "ViewStudent":
            view.ViewStudent.view_information(self.frames["ViewStudent"])

        self.hide_pages_widgets()
        
        # for showing the called page
        self.button_clicked(frame_name, button, image)
        self.container.tkraise()
        self.frames[frame_name].tkraise()


    # hiding the other pages widgets
    def hide_pages_widgets(self):
        for page in ["AddStudent", "SearchStudent", "DeleteStudent", "UpdateStudent"]:
            frame = self.frames[page]
            frame.response.place_forget()

            if page == "UpdateStudent":
                frame.entrySearch.delete(0, END)

            if page != "AddStudent":
                frame.hide_frame()


    # change button appearance when clicked
    def button_clicked(self, fname, new_btn, new_img):
        # assign the current image and button
        self.reset_button_state()
        self.current_img = new_img
        self.current_btn = new_btn

        # change the button image corresponding to the button clicked
        if fname == "AddStudent":
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnAddCv.png"))
        elif fname == "ViewStudent":
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnViewCv.png"))
        elif fname == "SearchStudent":
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnSearchCv.png"))
        elif fname == "UpdateStudent":
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnUpdateCv.png"))
        elif fname == "DeleteStudent":
            self.clicked_img = PhotoImage(file=self.relative_to_assets("btnDeleteCv.png"))
        self.current_btn.configure(image=self.clicked_img)


    # reset the current button image
    def reset_button_state(self):
        if self.current_btn != None and self.current_img != None:
            self.current_btn.configure(image=self.current_img)
        

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
