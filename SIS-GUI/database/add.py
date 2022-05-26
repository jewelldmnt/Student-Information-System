# DATABASE TO ADD STUDENTS
import csv


def add(student_data):
    # the student database csv file
    student_database = 'students.csv'
    
    # append the student data to the database file
    with open(student_database, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
