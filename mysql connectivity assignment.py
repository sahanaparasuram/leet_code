import mysql.connector as a
cnx=a.connect(host="127.0.0.1",user="root",password="Aishu123")
if cnx.is_connected:
    def create():
        global name
        name=input("Enter name of database  :")
        cursor=cnx.cursor()
        cursor.execute("create database {name1}".format(name1=name))
        cnx.commit()
   
    def table():
        c=cnx.cursor()
        global name,tab
        c.execute("use {name1}".format(name1=name))
        cnx.commit()
        tab=input("Enter table name:")
        c.execute("""create table {tab1} (admno varchar(20) primary key,
                  name varchar(20),class int,section char(1),physics int,math int,
                  chemistry int,total int null)""".format(tab1=tab))
        cnx.commit()
    def rows():
        c=cnx.cursor()
        global name,tab,phy,mat,chem
        c.execute("use {name1}".format(name1=name))
        cnx.commit()
        n=int(input("Enter number of rows:"))
        for i in range(0,n):
            adm=input("Enter admission number:")
            nam=input("Enter student name:")
            clas=int(input("Enter class:"))
            sec=input("Enter section:")
            phy=int(input("Enter physics marks:"))
            mat=int(input('Enter math marks:'))
            chem=int(input("Enter chem marks:"))
            
            command="insert into {} values('{}','{}',{},'{}',{},{},{},Null)"
            c.execute(command.format(tab,adm,nam,clas,sec,phy,mat,chem))
            cnx.commit()
    def update():
       c=cnx.cursor()
       global name,tab,phy,mat,chem
       c.execute(("use {name1} ").format(name1=name))
       cnx.commit()
       command="update {tab1} set total=physics+chemistry+math "
       c.execute(command.format(tab1=tab))
       cnx.commit()
    def display():
        c=cnx.cursor()
        global name,tab
        c.execute(("use {name1} ").format(name1=name))
        cnx.commit()
        c.execute(("select * from {tab1} ").format(tab1=tab))
        for i in c:
            print(i)
    def displaycondition():
        c=cnx.cursor()
        global name,tab
        c.execute(("use {name1} ").format(name1=name))
        cnx.commit()
        c.execute(("select * from {tab1} where (physics>{no1} and chemistry>{no2} and math>{no3})").format(tab1=tab,no1=75,no2=75,no3=75))
        for i in c:
            print(i)
        
        
    cont="y"
    while cont=="y" or cont=='Y':
        opt=input("""Enter 1 to create database\n2 to create table\n3 to add rows\n4 to update total\n5 to display all records\n6 to display records of
students whose marks>75""")
        if opt=="1":
            create()
            cont=input("Enter y/Y to continue:")
            continue
        if opt=="2":
            table()
            cont=input("Enter y/Y to continue:")
            continue
        if opt=="3":
            rows()
            cont=input("Enter y/Y to continue:")
            continue
        if opt=="4":
            update()
            cont=input("Enter y/Y to continue:")
            continue
        if opt=="5":
            display()
            cont=input("Enter y/Y to continue:")
            continue
        if opt=="6":
            displaycondition()
            cont=input("Enter y/Y to continue:")
            continue
    cnx.close()
else:
    print(" connection error")
