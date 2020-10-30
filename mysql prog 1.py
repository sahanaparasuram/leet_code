import mysql.connector
cnx = mysql.connector.connect(user='root', password='Aishu123', host='localhost',port=5000,database='test',
auth_plugin='mysql_native_password')


if cnx.is_connected():
    print('Connection successful')
    print('Connection has been established yay!')
    cursor = cnx.cursor()
    cursor.execute("select * from student")
    for x in cursor:
       print(x)

cnx.close()

