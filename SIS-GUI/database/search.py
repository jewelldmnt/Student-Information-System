import os
import csv

student_info = None

# return true or false weather the student is found
def search(student_number):
    global student_info
    student_database = 'students.csv'

    if os.path.exists(student_database) and os.path.getsize(student_database) > 0:
        with open(student_database, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if student_number == row[0]:
                    student_info = row
                    return True
    return False

def show_results(parent):
    global student_info
    for label, info in zip(parent.labels, student_info):
        label.configure(text=info)
