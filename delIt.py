import mysql.connector
conn = mysql.connector.connect(host='localhost',password='Mysql@123database',user='root')

if conn.is_connected():
    print("The connection with database is successful.")