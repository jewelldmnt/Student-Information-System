import os
import csv


# return true or false weather the student is found
def student_information(student_number):
    student_database = 'students.csv'
    student_information = []

    with open(student_database, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if student_number == row[0]:
                for i in range(6):
                    student_information.append(row[i])
                break  # to exit for-loop in line 10 if student is already found

        return student_information
