import mysql.connector as ms
cn=ms.connect(host="localhost",user='root',password='Shagun02#',auth_plugin='mysql_native_password')
cur=cn.cursor()
cur.execute('create database if not exists expense_tracker')
cur.execute('use expense_tracker')
cur.execute('create table if not exists track(name char(20),email char(50) primary key,mobile_no char(10),salary int,expense_r varchar(15),epense int)')
print("******------ DAILY EXPENSE TRACKER ------******")
print()
print()
while(True):
    print("1.Create Account")
    print("2.Add Bill")
    print("3.Dispaly Account")
    print("4.Exit")
    print()
    ch=int(input("Enter your choice"))
    if ch==1:
        print("CREATE YOUR ACCOUNT")
        print()
        name=str(input("Enter your name: "))
        email=str(input("Enter your e-mail id: "))
        mobile_no=str(input("Enter your Mobile Number: "))
        salary=int(input("Enter your salary: "))
        expense_r="None"
        expense=0
        cur.execute('insert into track values("'+name+'","'+email+'","'+mobile_no+'",'+str(salary)+',"'+expense_r+'",'+str(expense)+')')
        cur.commit()
        print("Account created successfully!")
    elif ch==2:
        print("ADD YOUR EXPENSES")
        print()
        email=str(input("Enter your e-mail id: "))
        expense_r=input("Enter reason of your expense: ")
        expense=input("Enter the amount spend: ")
        salary1=slaray-expense
        cur.exexute('update track set +expense_r="'+expense_r+'" and expense='+expense+' where email='"+email+"')')
        cur.execute('update track set salary=salary1 where email='"+email+"')')
        cur.commit()
        print("BILL ADDED SUCCESSFULLY")
    elif ch==3:
        print("PROVIDE YOUR E-MAIL TO SEARCH YOUR ACCOUNT")
        print()
        email=str(input("Enter your e-mail id: "))
        cur.execute('selecr * from track where email="'+email+'")')
        for i in cur:
            print(i)

    elif ch==4:
        print("******______ THANK YOU ______******")
    else:
        break
    
        
        
        
        
    
