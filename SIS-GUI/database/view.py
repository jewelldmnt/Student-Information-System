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
        reader = csv.reader(file)
        no_of_students = number_of_students()
        # values for right inside padding inside the table
        one_st, two_st = 170, 40 
        # y values to place the output properly
        y_stn = (one_st + 6) if no_of_students == 1 else (two_st + 6) if no_of_students == 2 else 6
        y_data = (one_st + 37) if no_of_students == 1 else (two_st + 37) if no_of_students == 2 else 37 
        ipady = one_st if no_of_students == 1 else two_st if no_of_students == 2 else 0

        # loop all rows and display it
        for ind, row in enumerate(reader):
            # print the table image
            Label(parent.table_frame, bg="#0B4D65", image=parent.imgTable).grid(row=ind, ipady=ipady)
            for index, data in enumerate(row):
                # if student number, different placement
                if index == 0:
                    Label(parent.table_frame, text=data, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 13 * -1)).place(x=120, y=y_stn)
                else:
                    Label(parent.table_frame, text=data, bg="#8DC8DE", fg="#000000", font=("LexendDeca Regular", 13 * -1)).place(x=160, y=y_data)
                    y_data += 30
            # increment the y value to align in the bottom
            y_stn += (2*two_st + 184) if no_of_students == 2 else 184
            y_data += (2*two_st + 34) if no_of_students == 2 else 34


# get number of students
def number_of_students():
    global student_database

    # check if file exists 
    if not os.path.isfile(student_database):
        return 0

    with open(student_database, "r") as file:
        return len(file.readlines())

