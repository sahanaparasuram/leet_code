import mysql.connector as sqltor
mycon=sqltor.connect(host= "127.0.0.1", user = "root", password = "Aishu123")
if mycon.is_connected:
    def create_database():
        global d
        d=input('enter database name: ')
        cur = mycon.cursor()
        str='create database '+d
        cur.execute(str)

    def create_table():
        cur=mycon.cursor()
        global n
        n=input('enter table name: ')
        global d
        cur.execute('use database '+d)
        mycon.commit()
        cur.execute('create table '+n+'(admno varchar(20) primary key, name varchar(20),class int,section varchar(1),physics int,math int,chemistry int,total int null')
        
        mycon.commit()

    def row():
        n=int(input('enter no. of rows: '))
        for i in range(n):
            adm=input("Enter admission number:")
            nam=input("Enter student name:")
            class=int(input("Enter class:"))
            sec=input("Enter section:")
            phy=int(input("Enter physics marks:"))
            math=int(input('Enter math marks:'))
            chem=int(input("Enter chem marks:"))
            cur.execute('insert into '+n+' values('+adm+','+nam+','+class+','+sec+','+phy+','+math+','+chem+')')
            mycon.commit()
            
    def total():
        cur=mycon.cursor()
        global n
        cur.update('update '+n+' set total = physics+chemistry+math ')
        mycon.commit()

    def fetchall():
        global n
        cur=mycon.cursor()
        cur.execute('select * from '+n)
        mycon.commit()
        data=cur.fetchall()
        print('admission number\t\tname\t\tclass\t\tsection\t\tphysics\t\tmatht\tchem\t\ttot')
        for i in data:
            print(i,end='\t\t')
            
    def fetchfew():
        
        global n
        cur=mycon.cursor()
        cur.execute('select name,toatal from '+n+' where marks>75')
        mycon.commit()
        data=cur.fetchall()
        print('admission number\t\tname\t\tclass\t\tsection\t\tphysics\t\tmatht\tchem\t\ttot')
        for i in data:
            print(i,end='\t\t')

f=1
while f:
    f=int(input('enter:\n1 for create database\n2 for create table\n3 for add rows\n4 for updating total\n5 for displaying all rows\n6 for displaying rows with marks greater than 75\n0 for exit\n'))
    if f==1:
        create_database
    elif f==2:
        create_table
    elif f==3:
        row()
    elif f==4:
        total()
    elif f==5:
        fetchall()
    elif f==6:
        fetchfew()
          
        
        
            
            
        
    

























'''
    cursor = mycon.cursor()
    cursor.execute('create database Schools')
    cursor.execute('use database Schools')
    cursor.execute('create table student(admno varchar(5) primary key, name varchar(30), class varchar(2), section varchar(1), p_marks int, m_marks int, c_marks int, tot int')
    cursor.execute('insert into student values(S1234,Vinay,12,C,78,90,85)')
    cursor.execute('insert into student values(S2345,Ameya,12,B,88,89,70)')
    cursor.execute('insert into student values(S6789,Vishak,12,A,89,78,80)')
    cursor.execute('insert into student values(S4567,Rahul,12,B,97,93,92)')
    cursor.execute('insert into student values(S2222, Kishan, 12, A, 89,89,97)')
    cursor.execute('insert into student values(S3444,Pritham,12,B,89,99,98)')
    cursor.execute('alter table student add total int ')
    cursor.execute('update student set total = ((c_marks+m_marks+p_marks)/3)')
    records=cursor.fetchall()
    print('Admno\tname\tclass\tsec.\tphysics\tchem\tmaths\ttotal')
    for i in records:
        for j in i:
            print(j,end= '\t')
        print()
    print('Name\ttotal')
    for i in records:
          if records[i][7]>75:
              print(records[i][1],'\t',records[i][7])
    '''
          
          
    
    
    
    
    
