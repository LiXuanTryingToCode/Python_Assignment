#TP060916
#LEE LIK SHANN

import datetime

def addSavingAccount():
    name = input('Please enter your name\n: ')
    name.upper()
    print('Name registered!')
    while True:
        age = input('Please enter your age\n: ')
        if age.isdigit():
            if int(age) <= 17:
                print('You are not eligible to create an account!')
                adminmenu()
            else:
                print('age registered!')
                break
        else:
            print('Enter numbers only!')
            
    
    while True:            
        phone_num = input("Please input your phone number\n: ")
        if phone_num.isdigit():
            if len(phone_num) < 8:
                print("Invalid Phone Number")
            elif len(phone_num) > 12:
                print("phone Number too long. Please try Again.")
            else:
                print("Phone number registered!.")
                break
        else:
            print("Enter numbers only!")
    
    while True:
        icnumber = input('Please enter your ic number\n: ')
        if icnumber.isdigit():
            if len(icnumber) < 12: 
                print ('IC number less than 12 digit, Please enter again!')
            elif len(icnumber) > 12:
                print('IC number more than 12 digit, Please enter again!')
            else:
                print('IC number registered!')
                break
        else:
            print('Enter numbers only!')
    

    with open('Customerlogin.txt','r') as loginfile:
        balance = 0
        for line in loginfile:
            loginlist = line.strip().split(',')
            pass
        oldAccNum = loginlist[0]
        newAccNum = int(oldAccNum) + 1
    with open('Customerlogin.txt','a') as loginfile:
        defaultpassword = str('default')
        loginfile.write('\n')
        loginfile.write(str(newAccNum) + ',' + str(defaultpassword) + ','+ 'S')
    with open('Savinginfo.txt','a') as Savinginfo:
        Savinginfo.write('\n')
        Savinginfo.write(name + '|' + age + '|' + phone_num + '|' + icnumber + '|' + str(newAccNum) + '|' + str(balance))
    print('Account has been made!\n')
    print('Your account info:' + name+'|'+ age + '|' + phone_num + '|' +icnumber)
    print('This is your account number:' +str(newAccNum))
    print('Your password is"default", Please change immediately!')
    adminmenu()



def addCurrentAccount():
    name = input('Please enter your name\n: ')
    name.upper()
    print('Name registered!')
    while True:
        age = input('Please enter your age\n: ')
        if age.isdigit():
            if int(age) <= 17:
                print('You are not eligible to create an account!')
                adminmenu()
            else:
                print('age registered!')
                break
        else:
            print('Enter numbers only!')
            
    
    while True:            #Phone number input
        phone_num = input("Please input your phone number\n: ")
        if phone_num.isdigit() == True:
            if len(phone_num) < 5:
                print("not a valid Phone Number")
            elif len(phone_num) > 12:
                print("phone Number too long. Please try Again.")
            else:
                print("Phone Number Registered!.")
                break
        else:
            print("Enter numbers only!")
    
    while True:
        icnumber = input('Please enter your ic number\n: ')
        if icnumber.isdigit() == True:
            if len(icnumber) < 5: 
                print ('IC less than 12 digit, Please enter again!')
            elif len(icnumber) > 12:
                print('IC number more than 12 digit, Please enter again!')
            else:
                print('IC number registered successfully!')
                break
        else:
            print('Enter numbers only!')

    with open('Customerlogin.txt','r') as Currentlogin:
        balance = 0
        for lastline in Currentlogin:
            loginlist = lastline.strip().split(',')
            pass
        oldAccNum = loginlist[0]
        newAccNum = int(oldAccNum) + 1
    with open('Customerlogin.txt','a') as Currentlogin:
        defaultpassword = 'default'
        Currentlogin.write('\n')
        Currentlogin.write(str(newAccNum) + ',' + str(defaultpassword) + ',' + 'C')
    with open('Currentinfo.txt','a') as Currentinfo:
        Currentinfo.write('\n')
        Currentinfo.write(name + '|' + age + '|' + phone_num + '|' + icnumber + '|' + str(newAccNum) + '|' + str(balance))
    print('Account has been made!\n')
    print('Your account info:' + name + '|' +age + '|' + phone_num + '|' + icnumber)
    print('This is your account number:' + str(newAccNum) )
    print('Your password is "default", please change immediately')
    adminmenu()


def addadminaccount():
    adminid = str(input('Please create username\n: '))
    adminpassword = str(input('Please create a password (Must be 8 character!)\n: '))
    confirmpassword = str(input('Please confirm your password\n: '))
    if adminpassword != confirmpassword:
        print('Password does not match!!')
        addadminaccount()
    else:
        if len(adminpassword)<= 7:
            print('Password is too short!!')
            addadminaccount()
        else:
            with open('adminaccount.txt','a') as adminaccount:
                adminaccount.write(adminid+','+adminpassword+'\n')
                print('Admin account has been created')
    supermenu()



def logincustomer():
    accountnumber = input('Please enter your account number\n: ')
    customerpassword = input('Please enter your password\n: ')   
    success = False
    with open('Customerlogin.txt','r') as customerlogin:
        for i in customerlogin:
            loginlist = i.strip().split(',')
            if (loginlist[0] == accountnumber and loginlist[1] == customerpassword):
                success = True
                break
    if (success):
        print('Login succesful!')
        customermenu(loginlist)
    else:
        print('Invalid account number and password!')
        print('Please login again!') 
        logincustomer()


def loginadmin():
    adminid = input('Please enter your username\n: ')
    adminpassword = input('Please enter your password\n: ')
    if adminid == 'admin' and adminpassword == 'admin':
        supermenu()
    else:
        success = False
        with open('adminaccount.txt','r') as adminaccount:
            for i in adminaccount:
                adminlist = i.strip().split(',')
                if (adminlist[0] == adminid and adminlist[1] == adminpassword):
                    success = True
                    break
        if (success):
            print('Admin login succesful!')
            adminmenu()
        else:
            print('Invalid admin username and password!')
            print('Please login again!')
            loginadmin()


def changecustomerpassword(loginlist):
    allrecord = []
    with open('Customerlogin.txt','r') as customerlogin:
        for rec in customerlogin:
            reclist = rec.strip().split(',')
            allrecord.append(reclist)
    newpassword = input('Please enter your new password\n: ')
    i = -1
    all = len(allrecord) 
    for count in range(0,all):
        if loginlist[0] == allrecord[count][0]:
            i = count
            break
    if i >= 0:
        allrecord[i][1] = newpassword
    with open('Customerlogin.txt','w') as customerlogin:
        all = len(allrecord)
        for count in range(0,all):
            rec = ','.join(allrecord[count])+"\n"
            customerlogin.write(rec)
    print('Password has been changed sucessfully\nPlease login again!')
    logincustomer()


def editsavingdetail():
    allrec = []
    with open('Savinginfo.txt','r') as saving:
        accountnumber = input('Please enter account number to edit\n: ')
        num = 0
        for rec in saving:
            reclist = rec.strip().split('|')
            allrec.append(reclist)

        with open('Savinginfo.txt','r') as saving:
            for rec in saving:
                reclist = rec.strip().split('|')    
                if accountnumber == reclist[4]:
                    print ('Account found!')
                    print ("Account: " + str(reclist))
                    while True:
                        editchoice = input('Choose a detail to edit \n1.Age \n2.Phone number \n3.Save and exit \n: ')
                        if editchoice == '1':
                            while True:
                                try:
                                    newage = int(input('Please enter new age: '))
                                    break
                                except ValueError:
                                    print('Enter numbers only!')
                            reclist[1] = str(newage)
                            print('Age has been changed successfully!')
                            print('New customer detail:' + str(reclist))
                            allrec[num] = reclist
                            continue

                        elif editchoice == '2':
                            while True:
                                try:
                                    newphonenum = int(input('Please enter new phone number: '))
                                    break
                                except ValueError:
                                    print('Enter numbers only!')
                            reclist[2] = str(newphonenum )
                            print('Phone number has been changed successfuly!')
                            print('New customer detail:' + str(reclist))
                            allrec[num] = reclist
                            continue
                        
                        elif editchoice == '3':
                            with open('Savinginfo.txt','w') as blank:
                                blank.write('')
                                with open('Savinginfo.txt','a') as saving:
                                    for edited_list in allrec:
                                        joinstring = '|'.join(edited_list)
                                        saving.write(joinstring +'\n')
                                adminmenu()
                                break
                        else:
                            print ('Please enter a valid input!')
                else:
                    print('Account number does not exist!')
                num = num + 1

def editcurrentdetail():
    allrec = []
    with open('Currentinfo.txt','r') as current:
        accountnumber = input('Please enter account number to edit\n: ')
        num = 0
        for rec in current:
            reclist = rec.strip().split('|')
            allrec.append(reclist)

        with open('Currentinfo.txt','r') as current:
            for rec in current:
                reclist = rec.strip().split('|')    
                if accountnumber == reclist[4]:
                    print ('Account found!')
                    print ("account: " + str(reclist))
                    while True:
                        editchoice = input('Choose a detail to edit \n1.Age \n2.Phone number \n3.Save and exit \n: ')
                        if editchoice == '1':
                            while True:
                                try:
                                    newage = int(input('Please enter new age: '))
                                    break
                                except ValueError:
                                    print('Enter numbers only!')
                            reclist[1] = str(newage)
                            print('Age has been changed successfully!')
                            print('New customer detail:' + str(reclist))
                            allrec[num] = reclist
                            continue

                        elif editchoice == '2':
                            while True:
                                try:
                                    newphonenum = int(input('Please enter new phone number: '))
                                    break
                                except ValueError:
                                    print('Enter numbers only!')
                            reclist[2] = str(newphonenum)
                            print('Phone number has been changed successfuly!')
                            print('New customer detail:' + str(reclist))
                            allrec[num] = reclist
                            continue
                        
                        elif editchoice == '3':
                            with open('Currentinfo.txt','w') as blank:
                                blank.write('')
                                with open('Currentinfo.txt','a') as current:
                                    for edited_list in allrec:
                                        joinstring = '|'.join(edited_list)
                                        current.write(joinstring +'\n')
                                adminmenu()
                                break    
                        else:
                            print('Please enter a valid input!')
                else:
                    print('Account number does not exist!')
                num = num + 1


def savingwithdrawal(loginlist):
    print('----------Withdraw from Savings----------')
    print('=========================================')
    allrec = []
    with open('Savinginfo.txt','r') as saving:
        for rec in saving:
            reclist = rec.strip().split('|')
            allrec.append(reclist)
            if loginlist[0] == reclist[4]:
                print('Your balance is:RM ' + str(reclist[5]))
                while True: 
                    try:
                        withdrawamount = int(input('Enter withdraw amount:'))
                        break
                    except ValueError:
                        print ('Enter numbers only!')
                newbalance = int(reclist[5]) - int(withdrawamount)
                if int(newbalance) < 100:
                    print ('Withdraw unsuccessful!')
                    print ('Balance insufficient!')
                else:
                    reclist[5] = str(newbalance)
                    print ('Your balance is : RM'+ reclist[5])

                date = datetime.datetime.now()
                with open('transaction.txt','a') as transactionfile:
                    tran =(reclist[0] + ',' + reclist[4] + ',' + 'withdraw' +','+ 'RM' + str(withdrawamount) + ',' + date.strftime('%d/%m/%Y') + '\n')
                    transactionfile.write(tran)

    with open('Savinginfo.txt','w') as blank:
        blank.write('')
        with open('Savinginfo.txt','a') as saving:
            for newrec in allrec:
                joinstring = '|'.join(newrec)
                saving.write(joinstring + '\n')

def currentwithdrawal(loginlist):
    print('----------Withdraw from current----------')
    print('=========================================')
    allrec = []
    with open('Currentinfo.txt','r') as current:
        for rec in current:
            reclist = rec.strip().split('|')
            allrec.append(reclist)
            if loginlist[0] == reclist[4]:
                print('Your balance is =RM' + str(reclist[5]))
                while True:
                    try:
                        withdrawamount = int(input('Enter withdraw amount:'))
                        break
                    except ValueError:
                        print ('Enter numbers only!')
                newbalance = int(reclist[5]) - int(withdrawamount)
                if int(newbalance) < 500:
                    print ('Withdraw unsuccessful!')
                    print ('Balance insufficient!')
                elif int(newbalance) >= 500:
                    reclist[5] = str(newbalance)
                    print ('Your balance is : RM'+ reclist[5])

                date = datetime.datetime.now()
                with open('transaction.txt','a') as transactionfile:
                    tran =(reclist[0] + ',' + reclist[4] + ',' + 'withdraw' +','+ 'RM' + str(withdrawamount) + ',' + date.strftime('%d/%m/%Y') + '\n')
                    transactionfile.write(tran)

    with open('Currentinfo.txt','w') as blank:
        blank.write('')
        with open('Currentinfo.txt','a') as saving:
            for newrec in allrec:
                joinstring = '|'.join(newrec)
                saving.write(joinstring + '\n')


def savingdeposit(loginlist):
    print('----------Deposit to Savings----------')
    print('======================================')
    allrec = []
    with open('Savinginfo.txt','r') as saving:
        for rec in saving:
            reclist = rec.strip().split('|')
            allrec.append(reclist)
            if loginlist[0] == reclist[4]:
                print('Your balance is:RM ' + str(reclist[5]))
                while True:
                    try:
                        depositamount = int(input('Enter deposit amount:'))
                        break
                    except ValueError:
                        print ('Enter numbers only!')
                newbalance = int(reclist[5]) + int(depositamount)
                reclist[5] = str(newbalance)
                print ('Your balance is : RM'+ reclist[5])

                date = datetime.datetime.now()
                with open('transaction.txt','a') as transactionfile:
                    tran =(reclist[0] + ',' + reclist[4] + ',' + 'deposit' + ',' +'RM'+ str(depositamount) + ',' + date.strftime('%d/%m/%Y') + '\n')
                    transactionfile.write(tran)

    with open('Savinginfo.txt','w') as blank:
        blank.write('')
        with open('Savinginfo.txt','a') as saving:
            for newrec in allrec:
                joinstring = '|'.join(newrec)
                saving.write(joinstring + '\n')


def currentdeposit(loginlist):
    print('----------Deposit to current----------')
    print('======================================')
    allrec = []
    with open('Currentinfo.txt','r') as current:
        for rec in current:
            reclist = rec.strip().split('|')
            allrec.append(reclist)
            if loginlist[0] == reclist[4]:
                print('Your balance is:RM ' + str(reclist[5]))
                while True:
                    try:
                        depositamount = int(input('Enter deposit amount:'))
                        break
                    except ValueError:
                        print ('Enter numbers only!')
                newbalance = int(reclist[5]) + int(depositamount)
                reclist[5] = str(newbalance)
                print ('Your balance is : RM'+ reclist[5])

                date = datetime.datetime.now()
                with open('transaction.txt','a') as transactionfile:
                    tran =(reclist[0] + ',' + reclist[4] + ',' + 'deposit' + ',' + 'RM' +str(depositamount) + ',' + date.strftime('%d/%m/%Y') + '\n')
                    transactionfile.write(tran)

    with open('Currentinfo.txt','w') as blank:
        blank.write('')
        with open('Currentinfo.txt','a') as saving:
            for newrec in allrec:
                joinstring = '|'.join(newrec)
                saving.write(joinstring + '\n')


def balanceinquiry(loginlist):
    with open('Savinginfo.txt','r') as saving:
        for rec in saving:
            reclist = rec.strip().split('|')
            if loginlist[0] == reclist[4]:
                available = int(reclist[5]) - 100
                print ('Your balance is :RM' + reclist[5])
                print ('Maximim withdrawal is:RM' + str(available) )
    with open('Currentinfo.txt','r') as current:
        for rec in current:
            reclist = rec.strip().split('|')
            if loginlist[0] == reclist[4]:
                available = int(reclist[5]) - 500
                print ('Your balance is :RM' + reclist[5])
                print ('Maximum withdrawal is:RM' + str(available))
    customermenu(loginlist)



def viewcustomerdetail():
    admininput = input('Which account detail do you want to view? \n1.Saving \n2.Current \n3.Exit \n: ')
    if admininput == '1':
        print(' Name |Age|Phone no| IC number |Acc no|Balance')
        print('================================================')
        with open('Savinginfo.txt','r') as saving:
            for line in saving:
                print(line)
        viewcustomerdetail()
    elif admininput == '2':
        print(' Name |Age|Phone no| IC number |Acc no|Balance')
        print('================================================')
        with open('Currentinfo.txt','r') as current:
            for line in current:
                print(line)
        viewcustomerdetail()
    elif admininput == '3':
        adminmenu()
    else:
        print ('Please enter a valid input!')
        viewcustomerdetail()


def transaction():
    allrec = []
    with open('transaction.txt','r') as transactionfile:
        for tran in transactionfile:
            recList = tran.strip().split(",")
            allrec.append(recList)
    while True:
        try:   
            accountnumber = int(input("Please enter your account number: "))
            break
        except ValueError:
            print('Enter numbers only!')
    while True:
        try:
            startday = input('Please enter start day(dd): ')
            startmonth = input('Please enter start month(mm): ')
            startyear = input('Please enter start year(yyyy): ')
            datetime.datetime.strptime(startday, '%d')
            datetime.datetime.strptime(startmonth, '%m')
            datetime.datetime.strptime(startyear, '%Y')
            break
        except ValueError:
            print("Please follow the format (dd for day) (MM for month) (yyyy for year)")
    while True:
        try:
            endday = input('Please enter end day(dd): ')
            endmonth = input('Please enter end month(mm): ')
            endyear = input('Please enter end year(yyyy): ')
            datetime.datetime.strptime(endday, '%d')
            datetime.datetime.strptime(endmonth, '%m')
            datetime.datetime.strptime(endyear, '%Y')
            break
        except ValueError:
            print("Please follow the format: (dd for day) (MM for month) (YYYY for year)")
    if len(str(startday)) == 1:
        startday = "0" + str(startday)
    if len(str(endday)) == 1:
        endday = "0" + str(endday)
    if len(str(startmonth)) == 1:
        startmonth = "0" + str(startmonth)
    if len(str(endmonth)) == 1:
        endmonth = "0" + str(endmonth)
    startdate = startday + "/" + startmonth + "/" + startyear
    enddate = endday + "/" + endmonth + "/" + endyear
    print('Starting from ' + startdate)
    print('Until ' + enddate)
    totalwithdrawal = 0
    totaldeposit = 0
    i = -1
    totalrec = len(allrec)
    for count in range(0,totalrec):
        if str(accountnumber) == allrec[count][1]:
            i = count
            if startdate <= (allrec[i][4]) and enddate >= (allrec[i][4]):
                if allrec[i][2] == 'withdraw':
                    num = int(allrec[i][3][2:])
                    totalwithdrawal += num
                    print(allrec[i])
                if allrec[i][2] == 'deposit':
                    num = int(allrec[i][3][2:])
                    totaldeposit += num
                    print(allrec[i])
    if i >= 0:
        print("Total withdrawal: " + 'RM' + str(totalwithdrawal))
        print("Total deposit: " + 'RM' + str(totaldeposit))
    adminmenu()


def supermenu():
    print('----------You are in super user account menu----------')
    print('======================================================')
    option = input('Please choose an option \n1.Create admin account \n2.Transaction \n3.Exit \n: ')
    if option == '1':
        addadminaccount()
    elif option == '2':
        transaction()
    elif option == '3':
        print('Thank you for using APU bank!')
        print('Hope you have a wonderful day! :)')
        menu()
    else:
        print('Please enter a valid input!!')
        supermenu()


def adminmenu():
    print('----------You are in admin menu----------')
    print('=========================================')
    adminchoice = input('Please choose an option \n1.Create customer account \n2.Edit customer detail \n3.View all data \n4.Transaction \n5.Exit \n: ')
    if adminchoice == '1':
        while True:
            accounttype = input('Which account do you want to create? \n1.Saving \n2.Current \n3.Exit \n: ')
            if accounttype == '1':
                addSavingAccount()
            elif accounttype == '2':
                addCurrentAccount()
            elif accounttype == '3':
                adminmenu() 
                break
            else:
                print('Please enter a valid input')
    elif adminchoice == '2':
        while True:
            accounttype = input('Which account do you want to edit? \n1.Saving \n2.Current \n3.Exit \n: ')
            if accounttype == '1':
                editsavingdetail()
            elif accounttype == '2':
                editcurrentdetail()
            elif accounttype == '3':
                adminmenu()
                break
            else:
                print('Please enter a valid input!')
    elif adminchoice == '3':
        viewcustomerdetail()
    elif adminchoice == '4':
        transaction()
    elif adminchoice == '5':
        print('Thank you for using APU bank!')
        print('Hope you have a wonderful day! :)')
        menu()
    else:
        print('Please enter a valid input!')
        adminmenu()


def customermenu(loginlist):
    print('---------You are in customer menu----------')
    print('===========================================')
    customerchoice = input('Please choose an option \n1.Withdrawal \n2.Deposit \n3.Balance Inquiry \n4.Change password \n5.Exit \n: ')
    if customerchoice == '1':
        while True:
            customerchoice2 = input('Withdraw from\n1.Saving \n2.Current \n3.Exit \n: ')
            if customerchoice2 == '1':
                savingwithdrawal(loginlist)
            elif customerchoice2 == '2':
                currentwithdrawal(loginlist)
            elif customerchoice2 == '3':
                customermenu(loginlist)
                break
            else:
                print('Please enter a valid input!')
    elif customerchoice == '2':
        while True:
            customerchoice2 = input('Deposit to\n1.Saving \n2.Current \n3.Exit \n: ')
            if customerchoice2 == '1':
                savingdeposit(loginlist)
            elif customerchoice2 == '2':
                currentdeposit(loginlist)
            elif customerchoice2 == '3':
                customermenu(loginlist)
            else:
                print('Please enter a valid input!')
    elif customerchoice == '3':
        balanceinquiry(loginlist)
    elif customerchoice == '4':
        changecustomerpassword(loginlist)
    elif customerchoice == '5':
        print('Thank you for using APU bank!')
        print('Hope you have a wonderful day! :)')
        menu()
    else:
        print('Please entert a valid input!')
        customermenu(loginlist)


def menu():
    while True:
        print('----------Welcome to APU bank----------')
        print('=======================================')
        accounttype = input('Which account do you want to login? \n1.Customer account \n2.Admin \n: ')
        if accounttype == '1':
            logincustomer()
        elif accounttype == '2':
            loginadmin()
        else:
            print ('Please enter a valid input!!')

menu()



