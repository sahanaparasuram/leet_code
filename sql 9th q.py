con=mysql.connector.connect(host='',database='',password='')
if  con.is_connected()==True:
    cursor=con.cursor()
    cursor.execute('create table Bank(Acc_no varchar(20) pre('imary key,Acc_name  varchar(20), cur_bal float(10,2),Interest float(10,2))')
    cursor.execute('insert into Bank values 
                
