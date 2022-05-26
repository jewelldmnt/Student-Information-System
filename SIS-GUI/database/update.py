from Database import search

# no return value, just pure command
def update_student(info_index, new_info):
    student_database = 'students.csv'
    # change student info with the new info
    search.student_info[info_index] = new_info
    # list of rows in the students database file
    data_list = []

    # read all line in a file and store it in a list 
    with open(student_database, "r", newline="") as file:
        data_list = file.readlines()

    # rewriting of student database file
    with open(student_database, "w", newline="") as file:
        # write the new student info if it matches with the current row
        for line in data_list:
            if line.startswith(search.student_info[0]):
                file.write(",".join(data for data in search.student_info) + "\n")
            else:
                file.write(f"{line.strip()}\n")