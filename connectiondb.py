import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='testdb',
                                         user='root',
                                         password='mikomen')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected succesfully")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

except Error as e:
    print("Error while connecting to MySQL", e)