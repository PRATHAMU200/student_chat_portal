import datetime
import os
path = os.path.dirname(os.path.realpath(__file__))

newpath= path+"\\posts\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
#filename = newpath+ user+".txt"
#filename = newpath+ group+".txt"
def make_a_message(grp):
    global filename
    global no_of_post
    global group
    group = grp
    db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")
    cur = db.cursor()
    filename = newpath+ group+".txt"
    post = ""
    while post != "quit":
        see_my_all_post()
        post=input("press quit to quit , enter post: ")
        f = open(filename,"a+" )
        d = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        f.writelines(d+": by "+user+"--> "+post+"\n")
        f.close()
    a = 0
    db.commit()

def see_my_all_post():
    f = open(filename,"r" )
    a=f.read()
    print(a)
    f.close()

def see_groups():
    all_files = os.listdir(newpath)
    print(all_files)


def make_new_group(name):
    filename = newpath+ name+".txt"
    f = open(filename,"a+")
    f.write("group has been made by"+user+"\n")
    f.close()

dic = {1:0,2:0,3:0,4:0}
def Poll():
    global dic
    print("1. make a poll")
    print("2. answer polls")
    print("3. show poll result")
    n = int(input("enter:"))
    d = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    if n == 1:
        d = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        title = input("enter title of poll in one word only")
        description = input("enter description of poll")
#        a = int(input("enter number of options available"))
        print("you have to put 4 options for poll")
        a=4
        filename = newpath+"poll_"+title+".txt"
        f = open(filename,"a+")
        f.writelines(d+": by "+user+"--> "+"------POLL-----"+"\n")
        f.writelines("Tittle: "+title+"\n")
        f.writelines("Description:"+description+"\n")
        for i in range (0,a):
            k = str(i+1)
            option = input("enter option")
            f.writelines(k+".)"+option+"\n")
        f.close()
    elif n == 2:
        all_files = os.listdir(newpath)
        for i in all_files:
            if i[:4] == "poll":
                print(i,end="\n")

        a = input("enter name of poll you want to access without .txt")
        filename = newpath+a+".txt"
        f = open(filename,"r")
        c=f.read()
        print(c)
        f1 = open(newpath+user+"pol_review.dat","a+")
        k = f1.read()
        print(k)
        if a not in k:
            choose = int(input("enter option that you want to tick in this poll"))
            f1.write(a)
            
            t = dic[choose]
            
            dic[choose]=t+1
                
                             
        else:
            print("you have already given this poll")


    elif n == 3:
        print("result of poll")
        for i in range(0,4):
            j=str(i+1)
            q=str(dic[i+1])
            print(j+"---->"+q+" vote")
            
        
        
        
            
            
    
    













#-------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------



import mysql.connector as sql
from getpass import getpass
    
variable = 0
def start():
    global variable
    global user
    db = sql.connect(host = "localhost", user = "root", passwd = "google")
    cur = db.cursor()

    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY , username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),no_of_post int(254) DEFAULT 0,no_of_reply INT(254) DEFAULT 0,no_of_likes INT(254) DEFAULT 0)")
                                                                                                                   

        except sql.errors.ProgrammingError :

            pass      

    finally :

        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY , username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),no_of_post int(254) DEFAULT 0,no_of_reply INT(254) DEFAULT 0,no_of_likes INT(254) DEFAULT 0)")
            cur.execute("insert into members(username , password , dob) values('admin', 'admin', '2020-01-01')")

        except sql.errors.ProgrammingError :
            
            pass
print("starting.....")   
start()
print("done")
    
def login() :

    global variable
    global user
    db = sql.connect(host = "localhost", user = "root", passwd = "google")
    cur = db.cursor()

    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grades_1 int(254) DEFAULT 0,grades_2 INT(254) DEFAULT 0, INT(254) DEFAULT 0)")
                                                                                                                                      

        except sql.errors.ProgrammingError :

            pass


    finally :

        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grades_1 int(254) DEFAULT 0,grades_2 INT(254) DEFAULT 0,grade_3 INT(254) DEFAULT 0)")
        except sql.errors.ProgrammingError :

            pass
   

    while True :


        flag = 0

        user = input("Enter Username :")

        passwd = getpass()


        cur.execute("select * from members where username = '%s' and password = '%s'" % (user, passwd))
                                                                                                                            

        rud = cur.fetchall()


        if rud :

            print("----------- Welcome "+user+"------------")

            flag = 1

            if flag == 1 :
                variable = 1

                break

        elif user == "root" and passwd == "root":
            print("-------------Welcome To Admin Account-------------")

            flag = 1

            if flag == 1 :
                variable = 2

                break

            
        else :
            print("account does't not exists!!!")
            break


            
    cur.close()
    db.close()






def register():
    db = sql.connect(host = "localhost", user = "root", passwd = "google")
    cur = db.cursor()
    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")

        cur = db.cursor()


        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grades_1 int(254) DEFAULT 0,grades_2 INT(254) DEFAULT 0,grade_3 INT(254) DEFAULT 0)")
                                                                                                                                      

        except sql.errors.ProgrammingError :

            pass


    finally :

        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grades_1 int(254) DEFAULT 0,grades_2 INT(254) DEFAULT 0,grade_3 INT(254) DEFAULT 0)")

        except sql.errors.ProgrammingError :

            pass



    while True :


        flag = 0

        user = input("Enter Username :")
        dob = input("enter date of birth in format yyyy-mm-dd")
        email = input("enter email (\"optional\")")
        passwd = getpass()


        cur.execute("select * from members where username = '%s' AND password = '%s'" % (user, passwd))
                                                                                                                            

        rud = cur.fetchall()


        if rud :

            print("Account is alredy exists !!!")

            flag = 1

            if flag == 1 :

                break


        else :
            try:
                cur.execute("insert into members(username , password , dob , email) values('{}', '{}', '{}','{}')". format(user, passwd,dob,email))
                db.commit()
                print("Account Created")
                flag = 1
                if flag == 1 :
                    break


            except sql.errors.ProgrammingError :
                print("username already exist")
                pass
    cur.close()
    db.close()

def members_details():
    db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")
    cur = db.cursor()

       



    cur.execute("select * from members ")
    rud = cur.fetchall()
    for i in rud:
        print(i)
       


    

    cur.close()
    db.close()

def delete():
    db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")
    cur = db.cursor()
    u = input("enter username of account to delete")
    i = int(input("enter id of account to delete"))
    try:
        cur.execute("DELETE FROM members where username = '%s' AND id = %s" % (u,i))
    
        print("deleted succesfully")
        db.commit()
        cur.close()
        db.close()

    except sql.errors.ProgrammingError :
        print("no record found")
        pass
def edit():

    db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")
    cur = db.cursor()
    while True:
        print("--------Account Info--------")
        cur.execute("select * from members where username = '%s'" % (user,))
        red = cur.fetchall()
        print(red)
        print("what you want to change")
        print("1.)DOB")
        print("2.)Email Id")
        print("3.)Password")
        print("4.) Back")
        option = int(input("enter the option"))
        if option == 1:
            dob = input("enter new Date_of_birth YYYY-MM-DD")
            cur.execute("update members set dob = '%s' where username = '%s'" % (dob,user))
            db.commit()
        elif option == 2:
            email = input("enter new email")
            cur.execute("update members set email = '%s' where username = '%s'" % (email,user))
            db.commit()
        elif option == 3:
            passw = getpass("enter new password")
            cur.execute("update members set password = '%s' where username = '%s'" % (passw,user))
            db.commit()
        elif option == 4:
            break
       

def forget_password():
    db = sql.connect(host = "localhost", user = "root", passwd = "google", database = "login")
    cur = db.cursor()
    user = input("enter your username")
  #  cur.execute("select dob from members where username = '%s'"% (user,))
  #  red = cur.fetchall()
    dob = input("enter your date of birth in format yyyy-mm-dd")
    cur.execute("update members set password = '%s' where username = '%s' AND dob = '%s'"%("passwd123",user,dob))
    db.commit()
    cur.execute("select password from members where username ='%s'"%(user,))
    r = cur.fetchall()
    a = r[0][0]
    if a == "passwd123":
        print("your password is \"passwd123\" use this to login and change your password")
    else:
        print("Error: please contact admin or try again")

def dashboard():
    global user
    print(user)
    print("-------------You are in dashboard -----------")
    print("1.)open messaging groups")
    print("2.)Create a group")


    option = int(input("enter choice"))
    if option == 1:
        see_groups()
        grp = input("enter name of group without .txt")
        
        try:
            print("Welcome to "+grp+"group")
            make_a_message(grp)
        except:
            print("error has occured !! somthing went wrong!!!!")
    elif option == 2:
        newgroup = input("enter group name")
        print("makeing new_group")
        try:
            make_new_group(newgroup)
        except:
            print("something went wrong!!!!!")



        
        
    
    
while True:    

    while variable == 0 :
        print("-------------------Welcome  to Student_Portal ---------------")
        print("1.) login")
        print("2.)register")
        print("3.)forget password")
        print("4.)quit")
        option =int(input("enter 1 for login and 2 for register"))


        if  option == 1:
            login()

        elif option == 2:
            register()

        elif option == 3:
            forget_password()
            
        elif option == 4:
            break
            

    else:
        if variable == 1:
            print("-------------Logged in by ",user,"-----------")
            print("1.) logout")
            print("2.)edit_user_details")
            print("3.)Dasboard")
            option =int(input("enter 1 for logout and 2 for post question and 3 for see posts"))
            if option == 1:
                variable = 0
            elif option == 2:
                    edit()
            elif option == 3:
                dashboard()


        elif variable == 2:
            print("-------------Logged in by admin---------")
            print("1.) logout")
            print("2.)see all user details")
            print("3.) for deleting a account")
            option =int(input("enter 1 for logout and 2 for details 3 for deleting"))
            if option == 1:
                variable = 0
            elif option == 2:
                members_details()
            elif option == 3:
                delete()
            

    

        
    




