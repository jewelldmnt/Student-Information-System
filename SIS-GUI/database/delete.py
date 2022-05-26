# DATABASE TO DELETE STUDENTS
from Database import search

# no return statement, just command
def delete_student():
    student_database = 'students.csv'
    data_list = []

    # read file and store it in a list
    with open(student_database, "r") as file:
        data_list = file.readlines()

    # rewrite the file without the skipped student
    with open(student_database, "w") as file:
        for line in data_list:
            if not line.startswith(search.student_info[0]):
                file.write(f"{line.strip()}\n")
