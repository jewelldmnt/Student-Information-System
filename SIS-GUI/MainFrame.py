# importing the required libraries/modules
from tkinter import *
from HomePage import HomePage as hp
from SignUpPage import SignUpPage as sup
from SignInPage import SignInPage as sip
from StudentMenu import StudentMenu as sm
from AdminMenu import AdminMenu as am


# class for the main frame
class MainFrame(Tk):
    # init method of the class MainFrame
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)

        # creating a container for all
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creating a dictionary of page objects and id for menu
        self.frames = {}
        self.id = None

        # looping in every page/class and creating an object of it
        # then storing the class name as the key 
        # and the object of it as the value 
        for f in {hp.HomePage, sup.SignUpPage, sip.SignInPage, sm.StudentMenu, am.AdminMenu}:
            page_name = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = frame

        self.show_frame("HomePage")

    # showing the current frame above everything
    def show_frame(self, page_name, id=None):
        self.id = id
        frame = self.frames[page_name]
        frame.tkraise()


# initialize main window app
window = MainFrame()
window.geometry("1280x720")
window.resizable(0, 0)
window.mainloop()
