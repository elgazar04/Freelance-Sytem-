import hashlib
import os
from os import path


#ترتيب الكود بيكون كالأتي
#1: while loop
#2: signup()
#3: login()
#4: corporation page
#5: freelancer page


def signup():
    status = input("Hi, are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("./users/usernames.txt", "a")as f:
                    f.write(username + "\n")
                    f.close()
                os.mkdir("./users/" + username)
                with open("./users/" + username + "/" + username + ".txt", "w")as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again. \n")
    elif status == "c": # هنا لو المستخدم شركة هيكتب c
        username = input("Enter corporation username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("./users/corp_credentials.txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again.\n")


def login():
    attempts = 4
    global f_username 
    status = input("Are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        while attempts >= 0:
            f_username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            if os.path.isdir("./users/" + f_username):
                with open("./users/" + f_username + "/" + f_username + ".txt", "r") as f:
                    stored_f_username, stored_password = f.read().split("\n")
                f.close()
                if f_username == stored_f_username and auth_hash == stored_password:
                    print("Logged in Successfully!")
                    freelancer_page()
                    break
                else:
                    print("Login failed!, you have ", attempts, " attempts to try again\n")
                    attempts = attempts - 1
            else:
                print("There is no username like that! please signup!")
                signup()
        if(attempts<0):
            print("you can't login, try creating account")
            signup()

    elif status == "c":
        while attempts >=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()

            auth_hash = hashlib.md5(auth).hexdigest()
            with open("./users/corp_credentials.txt", "r") as f:
                stored_corp_username, stored_corp_password = f.read().split("\n")
            f.close()
            if username == stored_corp_username and auth_hash == stored_corp_password:
                print("Logged in Successfully!")
                corp_page()
                break
            else:
                print("Login failed!, you have ",attempts," attempts to try again\n")
                attempts=attempts-1
            if attempts < 0:
                cr_account = input(print("you can't login, would try creating an account?"))
                if cr_account == "y":
                    signup()
                else:
                    break

def corp_page():
    with open("./users/corp_credentials.txt", "r") as f:
        if not os.path.isfile("./jobs/jobs.txt"):
            with open("./jobs/jobs.txt", "w")as v:
                v.close()
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?")
        if corp_chosen == "l":
            num = int(input("Enter number of jobs: "))
            i = 1
            j = 1
            while (i<= num and j <= num):
                print("job",i, ":")
                title = input("Enter job title: \n")
                id = input("Enter job id: \n")
                required_skills =input ("Enter required skills: \n")
                job_describ =input("Enter job description: ")
                with open("./jobs/jobs.txt", "r")as f:
                    xlines = len(f.readlines())
                    f.close()
                if xlines == 0:
                    f = open("./jobs/jobs.txt","w")
                    f.write(title +"\n")
                else:
                    f = open("./jobs/jobs.txt", "a")
                    f.write(title + "\n") 

                if not os.path.isdir("./jobs/" + title):
                    os.mkdir("./jobs/" + title)
                    file_Name = "./jobs/" + title + "/" + title + ".txt"
                    x = open(file_Name, "w")
                    x.write("Title: " + title + "\n")
                    x.write("id: " + id + "\n")
                    x.write("Required skills: " + required_skills + "\n")
                    x.write("Job describtion: " + job_describ)
                    j = j + 1
                    i = i + 1

                else:

                    file_Name = "./jobs/" + title + "/" + title + ".txt"
                    x = open(file_Name, "w")
                    x.write("Title: " + title + "\n")
                    x.write("id: " + id + "\n")
                    x.write("Required skills: " + required_skills + "\n")
                    x.write("Job describtion: " + job_describ)
                    j = j + 1
                    i = i + 1


        elif corp_chosen == "v":
            with open("./users/usernames.txt", "r")as f:
                usernames = f.readlines()
                how_many_usernames = len(f.readlines())
                f.close()
            print("Hi, these applicants have applied to a job: \n")
            print(*usernames, sep =", ")
            username_chosen = input("Which one do you want to see their application?")
            user_job_applied = "./users/" + username_chosen + "/" + username_chosen + "_job_applied.txt"
            user_description = "./users/" + username_chosen + "/" + username_chosen + "_description.txt"
            username_job_status = "./users/" + username_chosen + "/" + username_chosen + "_job_status.txt"
            if os.path.isfile(user_job_applied):
                with open(user_job_applied, "r")as f:
                    job_applied = f.read()
                    f.close()
                with open(user_description, "r")as f:
                    applicant_description = f.read()
                    f.close()
                print(username_chosen + " has applied to " + job_applied)

                print(username_chosen + "'s bio is: " + "\n" +applicant_description + "\n")
                job_status_1 = input("Wanna accept this application? (y/n): ")
                if job_status_1 == "y":
                    job_status = "Accepted"
                    with open(username_job_status, "w") as f:
                        f.write(job_status)
                        f.close()
                else:
                    job_status = "Not Accepted"
                    with open(username_job_status, "w") as f:
                        f.write(job_status)
                        f.close()
            else:
                print("user has not applied for a job")



def freelancer_page():
    zero = 0
    global stored_f_username
    counter = 1
    check_job = 0
    lines = 0
    limit = 0

    with open("./users/" + f_username + "/" + f_username + ".txt", "r") as f:
        stored_f_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_f_username
        print("Hi " + username + " there are some jobs available. Do you want to see them?\n")
        viewjobs = input("(y)es, or (n)o\n")
        if viewjobs == "y":
            with open("./jobs/jobs.txt", "r") as f:
                for line in open("./jobs/jobs.txt").readlines():
                    limit+=1
                job1 = f.read().splitlines()
                f.close()
            while lines <= limit-1:
                print(counter, ": ", job1[lines],"\n")
                lines = lines + 1
                counter = counter + 1
            check_job = int(input("Choose a job to see its description, skills needed, and furthermore.\n(Please enter the job's number)\n"))
            job_num = check_job - 1
            if check_job <= limit:
                job_name = job1[job_num]
                job_file_name = "./jobs/" + job_name + "/" + job_name + ".txt"
                with open(job_file_name, "r")as f:
                    job_title = f.read().split("\n")
                    job_id = f.read().split("\n")
                    job_req_skills = f.read().split("\n")
                    job_description = f.read()
                    f.close()
                print(job_title[0] +"\n" + job_title[1] + "\n" + job_title[2] + "\n" + job_title[3])
            else:
                print("Please enter a valid number")
        else:
            pass
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n")
        while job_apply == "j":
            applicant_description = input("Please inter your bio, skills, and social numbers: " + "\n")
            applicant_description_file = "./users/" + username + "/" + username + "_description.txt"
            with open(applicant_description_file, "w")as f:
                f.write(applicant_description + "\n")
                f.close()
            i = int(input("Please enter job's number " + "\n"))
            i_real = i-1
            job_applied_username = "./users/" + username + "/" + username + "_job_applied.txt"
            with open("./jobs/jobs.txt", "r")as f:
                job_applied_name = f.readlines()[i_real]
                f.close()
            with open(job_applied_username, "w")as f:
                f.write(job_applied_name + "\n")
                f.close()
            print("Job request sent successfully !")
            break
        while job_apply == "s":
            user_job_status = "./users/" + username + "/" + username +"_job_status.txt"
            with open(user_job_status, "r") as f:
                job_status = f.read()
                f.close()
            print("you " + "have been " + job_status + " to your job!" + "\n")
            break


while 1:
    if not os.path.isdir("users"):
        os.mkdir("users")
    if not os.path.isdir("jobs"):
        os.mkdir("jobs")

    print("\n---------- Login System ----------\n")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:

        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
