# import required files
import os
import csv
from tkinter import *

# student information file
student_database = 'students.csv'

def display_students(parent):
    global student_database

    # display student information
    with open(student_database, "r") as file:
        # y values to align and print properly
        reader = csv.reader(file)
        y_stn = 6
        y_data = 37

        # loop all rows and display it
        for ind, row in enumerate(reader):
            # print the table image
            Label(parent.table_frame, image=parent.imgTable).grid(row=ind)
            for index, data in enumerate(row):
                # if student number, different placement
                if index == 0:
                    Label(parent.table_frame, text=data, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 13 * -1)).place(x=120, y=y_stn)
                else:
                    Label(parent.table_frame, text=data, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 13 * -1)).place(x=160, y=y_data)
                    y_data += 30
            # increment the y value to align in the bottom
            y_stn += 184
            y_data += 34

# get number of students
def number_of_students():
    global student_database

    # check if file exists 
    if not os.path.isfile(student_database):
        return 0

    with open(student_database, "r") as file:
        return len(file.readlines())

