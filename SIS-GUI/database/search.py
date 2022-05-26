import os
import csv

student_info = []

# return true or false weather the student is found
def student_found(student_number):
    global student_info
    student_database = 'students.csv'

    # if file exists
    if os.path.isfile(student_database):
        with open(student_database, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if student_number == row[0]:
                    student_info = row
                    return True

    # student not found
    return False

# display the student result
def show_results(parent):
    global student_info
    for label, info in zip(parent.labels, student_info):
        label.configure(text=info)
