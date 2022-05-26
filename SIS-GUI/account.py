# THIS IS THE ACCOUNT DATA BASE
import hashlib
import os

# database management for sign up
def signup(filename, email, pwd, confirm_pwd):
    file = open(filename, "a")
    file = open(filename, "r")

    # password and confirm password doesn't match
    if pwd != confirm_pwd:
        return 2

    # The email already exist!
    for line in file:
        if email in line.split(", "):
            return 3

    # You have registered successfully!
    enc = confirm_pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    file = open(filename, "a")
    file.write(f"{email}, {hash1}\n")
    file.close()
    return 1

# database management for login
def login(filename, email, pwd):
    file = open(filename, "a")
    file = open(filename, "r")
    
    # if file is not empty
    if os.path.getsize(filename) > 0:
        # encoding the password 
        auth = pwd.encode()
        auth_hash = hashlib.md5(auth).hexdigest()

        # making a dictionary of email as key and password as value
        data = {}
        for line in file:
            em, pw = line.split(", ")
            data[em] = pw.strip()

        # check if email is in the list of emails
        if email in data.keys():
            # login successful
            if auth_hash == data[email]:
                return 1
            # incorrect email or password
            else:
                return 3
    
    # if file is empty then account does not exist
    file.close()
    return 2
