import datetime
import os
google = "google"


path = os.path.dirname(os.path.realpath(__file__))

newpath= path+"\\posts\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
#filename = newpath+ user+".txt"
#filename = newpath+ group+".txt"
def delete_group(group_entry):
    global status
    filename = newpath+"\\"+group_entry
    os.remove(filename)
def make_a_message(group_entry,post):
    global filename
    global no_of_post
    global group
    group = group_entry
    filename = newpath+ group_entry
    if post:
        f = open(filename,"a+" )
        d = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        f.writelines(d+": by "+username_info+"--> "+post+"\n")
        f.close()
    a = 0

def see_my_all_post(group):
    filename = newpath + group
    global message
    f = open(filename,"r" )
    message=f.read()
    f.close()
    return message

def see_groups():
    global all_files
    all_files = os.listdir(newpath)


def make_new_group(name):
    global group_made
    filename = newpath+ name+".txt"
    f = open(filename,"a+")
    f.write("group has been made by"+username_info+"\n")
    f.close()
    group_made = 1

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
    db = sql.connect(host = "localhost", user = "root", passwd = google)
    cur = db.cursor()

    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

        cur = db.cursor()


        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY , username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grade_1 int(254) DEFAULT 0,grade_2 INT(254) DEFAULT 0,grade_3 INT(254) DEFAULT 0)")
                                                                                                                   

        except sql.errors.ProgrammingError :

            pass      

    finally :

        try :

            cur.execute("create table members(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY , username varchar(65) NOT NULL UNIQUE, password varchar(65) NOT NULL ,dob date NOT NULL,email varchar(65),grade_1 int(254) DEFAULT 0,grade_2 INT(254) DEFAULT 0,grade_3 INT(254) DEFAULT 0)")
            cur.execute("insert into members(username , password , dob) values('admin', 'admin', '2020-01-01')")

        except sql.errors.ProgrammingError :
            
            pass
print("starting.....")   
start()
print("done")
    
def login(user1,passwd) :
    global correct
    correct = 0
    global variable
    global user
    db = sql.connect(host = "localhost", user = "root", passwd = google)
    cur = db.cursor()

    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

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


        cur.execute("select * from members where username = '%s' and password = '%s'" % (user1, passwd))
                                                                                                                            

        rud = cur.fetchall()


        if rud :

            correct = 1

            flag = 1

            if flag == 1 :
                variable = 1

                break

        elif user1 == "root" and passwd == "root":
            correct = 2

            flag = 1

            if flag == 1 :
                variable = 2

                break

            
        else :
            correct = 0
            break


            
    cur.close()
    db.close()






def register(user_name,passwd,DOB,email1):
    global reg
    db = sql.connect(host = "localhost", user = "root", passwd = google)
    cur = db.cursor()
    
    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError :

        db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")

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

        cur.execute("select * from members where username = '%s'" % (user_name))
                                                                                                                            

        rud = cur.fetchall()


        if rud :

            reg = 0

            flag = 1

            if flag == 1 :

                break


        else :
            try:
                cur.execute("insert into members(username , password , dob , email) values('{}', '{}', '{}','{}')". format(user_name, passwd,DOB,email1))
                db.commit()
                reg = 1
                flag = 1
                if flag == 1 :
                    break


            except sql.errors.ProgrammingError :
                reg = 0
                pass
    cur.close()
    db.close()

def members_details():
    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
    cur = db.cursor()

       



    cur.execute("select * from members ")
    rud = cur.fetchall()
    for i in rud:
        print(i)
       


    

    cur.close()
    db.close()



def table_info():
    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
    cur = db.cursor()





    cur.execute("show columns from members")
    rud = cur.fetchall()
    for i in rud:
        print(i)
       


    

    cur.close()
    db.close()



def command():
    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
    cur = db.cursor()

    try :   

        c = input("for help type help ...enter mysql command to execute without ';'")
        if c != "help":

            cur.execute(c)
            rud = cur.fetchall()
            for i in rud:
                print(i)

        else:
            print(help())
       
    except:
        print("wrong syntax !!!!")

    

    cur.close()
    db.close()

def help():
    a = """
        
        
        for adding a column to a table ----> ALTER TABLE 'table_name' ADD COLUMN 'column_name' 'data_type'
        to show table info ----->  SHOW COLUMNS FROM 'members'
        to drop a column from a table -----> ALTER TABLE 'members' DROP COLUMN 'column name'
        To drop table -----> DROP TABLE 'members'
        To Rename a table -----> RENAME TABLE 'current_table_name' TO 'new_table_name'
        To change column of any table ----> ALTER TABLE 'members' CHANGE COLUMN 'full_names' 'fullname' char(250) NOT NULL
        To Modify table column datatype ----> ALTER TABLE 'members' MODIFY 'fullname' char(50) NOT NULL
        To add a column in b/w -----> ALTER TABLE  'members' ADD  'date_of_registration' date NULL AFTER  'date_of_birth'
        """
    print(a)


def delete():
    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
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
def edit(user):
    global id_info
    global dob_info
    global username_info
    global email_info

    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
    cur = db.cursor()
    if 1==1:
        cur.execute("select * from members where username = '%s'" % (user,))
        red = cur.fetchall()
        id_info = red[0][0]
        username_info = red[0][1]
        dob_info = red[0][3]
        email_info = red[0][4]
        '''
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
       '''

def edit_info(u,p,d,e):
    global done
    db = sql.connect(host="localhost", user="root", passwd=google, database="login")
    cur = db.cursor()
    cur.execute("update members set dob = '%s',email = '%s',password = '%s' where username = '%s'" % (d,e,p,u))
    db.commit()
    done = 1
def forget_password():
    db = sql.connect(host = "localhost", user = "root", passwd = google, database = "login")
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
    print("3.)back")


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

    elif option == 3:
        variable == 0



        
        
'''
    
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
            print("4.) for database info ")
            print("5.) for executing a command in mysql database")
            option =int(input("enter 1 for logout and 2 for details 3 for deleting"))
            if option == 1:
                variable = 0
            elif option == 2:
                members_details()
            elif option == 3:
                delete()
            elif option == 4:
                table_info()
            elif option == 5:
                command()
            
'''
    

        
    




