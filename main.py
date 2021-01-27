import PySimpleGUI as sg
import student as lib
import time
import datetime
opt = 2
login = 0
'''
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
a=""
layout = [  [sg.Text('LOGIN PAGE')],
            [sg.Text(key = 'output',size=(40,1))],
            [sg.Text('Username'), sg.InputText(key='username')],
            [sg.Text('Password'), sg.InputText(key='password')],
            [sg.Button('Login'), sg.Button('Cancel'),sg.Button('Register')],
            [sg.Text(key='output2')]]



# Create the Window
window = sg.Window('LOGIN PAGE', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    user_name=values['username']
    passwd = values['password']
    log = lib.login(user_name, passwd)
    if event == 'Login':
        correct = lib.correct
        if correct == 1:
            window['output'].update('Hello ' + values['username'])
            login = 1
            break
        else:
            window['output'].update("incorrect username or password!!!!",text_color='red')
    if event == 'Register':
        opt = 1
        break

window.close()
'''
#------------------------------------------------------------------------------------------------------------------------------
while True:

    if opt == 1:
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        a = ""
        layout = [[sg.Text('Register For New User')],
                  [sg.Text(key='output', size=(40, 1))],
                  [sg.Text('Username*'), sg.InputText(key='username')],
                  [sg.Text('DOB(yyyy-mm-dd)*'), sg.InputText(key='DOB')],
                  [sg.Text('Email'), sg.InputText(key='e-mail')],
                  [sg.Text('Password*'), sg.InputText(key='password')],
                  [sg.Button('Register'), sg.Button('Cancel'), sg.Button('Login')],
                 [sg.Text("* means compulsury to write")],
                 [sg.Text(key='output2')]]

        # Create the Window
        window = sg.Window('Register for new user', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
               break
            user_name = values['username']
            DOB = values['DOB']
            email1 = values['e-mail']
            passwd = values['password']


            if event == 'Register':

               try:
                    log = lib.register(user_name, passwd, DOB, email1)
                    reg = lib.reg
                    if reg == 1:
                        window['output'].update('Succesfully Registered !!!!!!' + values['username'],text_color='Green')
                    else:
                       window['output'].update("Account already exists for this username", text_color='red')
               except:
                   window['output'].update("error occured !!!!1", text_color='red')
            if event == 'Login':
                opt = 2
                break
        window.close()

#---------------------------------------------------------------------------------------------------------------------------

    if opt == 2 :
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        a = ""
        layout = [[sg.Text('LOGIN PAGE')],
                  [sg.Text(key='output', size=(40, 1))],
                  [sg.Text('Username'), sg.InputText(key='username')],
                  [sg.Text('Password'), sg.InputText(key='password'password_char='*')],
                  [sg.Button('Login'), sg.Button('Cancel'), sg.Button('Register')],
                  [sg.Text(key='output2')]]

        window = sg.Window('LOGIN PAGE', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
               break
            user_name = values['username']
            passwd = values['password']
            log = lib.login(user_name, passwd)
            if event == 'Login':
                correct = lib.correct
                if correct == 1:
                    window['output'].update('Hello ' + values['username'])
                    login = 1
                    opt = 3
                    break
                else:
                   window['output'].update("incorrect username or password!!!!", text_color='red')
            if event == 'Register':
                opt = 1
                break

        window.close()

# -----------------------------------------------------------------------------------------------------------------------

    if login == 1 and opt == 3:
        lib.edit(user_name)
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        a = ""
        layout = [[sg.Text('Hello' + user_name)],
                 [sg.Text(key='output', size=(40, 1))],
                 [sg.Text("INFO Of USER", text_color='white')],
                 [sg.Text("Username  --->" + lib.username_info)],
                 [sg.Text("Id  ---->" + str(lib.id_info))],
                 [sg.Text("Date Of Birth  ---->"+str(lib.dob_info ))],
                 [sg.Text("E-mail  ---->"+lib.email_info )],
                 [sg.Button('Account')],
                 [sg.Button('Dashboard')],
                 [sg.Button('Edit_user details')],
                 [sg.Button('Logout')],
                 [sg.Button('Cancel')],
                 [sg.Text(key='output2')]]

        # Create the Window
        window = sg.Window('Account', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break
            if event == 'Logout':
                login = 0
                opt = 2
                break
            if event == 'Dashboard':
                opt = 5
                break
            if event == 'Edit_user details':
                opt = 4
                break

        window.close()

# ---------------------------------------------------------------------------------------------------------------------
    if login == 1 and opt == 4:
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        a = ""
        layout = [[sg.Text('EDIT USER DETAILS HERE')],
                  [sg.Text(key='output', size=(40, 1))],
                  [sg.Text('Username'),sg.Text(lib.username_info)],
                  [sg.Text('Password'), sg.InputText(key='new_password')],
                  [sg.Text('DOB'), sg.InputText(lib.dob_info,key='new_dob')],
                  [sg.Text('email'),sg.InputText(lib.email_info,key='new_email')],
                  [sg.Button('SAVE')],
                  [sg.Button('Back')],
                  [sg.Text(key='output2')]]

        # Create the Window
        window = sg.Window('EDIT USER INFO', layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            pas = values['new_password']
            new_dob = values['new_dob']
            new_email = values['new_email']
            if event == 'Back':
                opt = 3
                break
            elif pas == '':
                window['output'].update("Please enter Password also", text_color='red')


            elif event == 'SAVE':
                log = lib.edit_info(user_name, pas, new_dob, new_email)
                if lib.done == 1:
                    window['output'].update('Succesfully changed ')
                else:
                    window['output'].update("Error !! something went wrong", text_color='red')

        window.close()


    if login == 1 and opt == 5:
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        lib.see_groups()
        a = ""
        layout = [[sg.Text('-------------DASHBOARD------------')],
                  [sg.Text(key='output', size=(40, 1))],
                  [sg.Button(f'{col}') for col in lib.all_files],
                  [sg.Text("-----------------------------------",size=(40,20))],
                  [sg.Text("new group name"),sg.InputText(key='name'),sg.Button('Create_New_Group')],
                  [sg.Button('Back')],
                  [sg.Text(key='output2',size=(40,1))]]

        # Create the Window
        window = sg.Window('Dashboard', layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            group_name = values['name']
            if event == 'Back':
                opt = 3
                break

            elif event == 'Create_New_Group':
                log = lib.make_new_group(group_name)
                if lib.group_made == 1:
                    window['output2'].update('Succesfully made group '+group_name)
                    opt = 5
                    break
                else:
                    window['output2'].update("Error !! something went wrong", text_color='red')

            elif ".txt" in event:
                group_entry=event
                opt = 6
                break


        window.close()
#--------------------------------------------------------------------------------------------------------------------

    if login == 1 and opt == 6:
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        lib.see_groups()
        post = lib.see_my_all_post(group_entry)
        a = ""
        layout = [[sg.Text('------------'+group_entry+'------------')],
                  [sg.Text(key='output', size=(40, 1)),sg.Button("Delete_Group")],
                  [sg.Text(lib.message,key='mess')],
                  [sg.Text("-----------------------------------", size=(4, 2))],
                  [sg.Text("Write message"), sg.InputText(key='post1'), sg.Button('Send')],
                  [sg.Button('Back')],
                  [sg.Text(key='output2', size=(40, 1))]]

        # Create the Window
        window = sg.Window('Message', layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            post1 = values['post1']
            temp = lib.message
            if event == 'Back':
                opt = 5
                break

            elif event == 'Send':
                lib.make_a_message(group_entry,post1)
                window['post1'].update("")
                post = lib.see_my_all_post(group_entry)
                window['mess'].update(lib.message)
                opt = 6
                break


            elif event == 'Delete_Group':
                lib.delete_group(group_entry)
                opt = 5
                break



        window.close()


    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
