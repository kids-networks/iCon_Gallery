from pyscript import document
def fileopen(data) :
    with open ("data.txt") as text :
        for line in text :
            line = line.rstrip ("\n")
            line = line.rstrip (" ")
            username, password = line.split("<<")
            data[username] = password
def fileedit(nUser, nPassword) :
    with open ("data.txt", "a") as text :
        text.write("\n" + str(User) + "<<" + str(nPassword))
def login() :
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    data = {}
    fileopen(data)
    if username in data :
        if data[username] == password :
            print("Welcome back!")
        else:
            print("Scram, Hacker!")