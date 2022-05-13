import connectiondb as connection
import re

print('Please select an option:')
print('1) Create a new student')
print("2) Update student's data")
print('3) Delete student')
print('4) List of students')

a = int(input('Your option:  '))

email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
phone_regexp = re.compile(r'77[0-9]{9}$')
iin_regex = re.compile(r'[0-9]{12}$')

if a == 1:

    try:
        first_name = str(input("first_name:  "))
        last_name = str(input("last_name:  "))
        middle_name = str(input("middle_name:  "))
        iin = str(input("iin:  "))
        if iin_regex.match(iin):
            pass
        else:
            print('iin format is not correct!')
        phone = str(input("phone:  "))
        if phone_regexp.match(phone):
            pass
        else:
            print('phone format is not correct')
        email = str(input("email:  "))
        if email_regex.match(email):
            pass
        else:
            print('email format is not correct')
        address = str(input("address:  "))
        insert_query = """INSERT INTO student (first_name, last_name, middle_name, iin, phone, email, address) 
                               VALUES 
                               (%s, %s, %s, %s, %s, %s, %s) """
        value = [
            first_name,
            last_name,
            middle_name,
            iin,
            phone,
            email,
            address
        ]

        cursor = connection.cursor
        cursor.execute(insert_query, value)
        connection.connection.commit()
        print(cursor.rowcount, "Record inserted successfully into table")
        cursor.close()

    except connection.Error as error:
        print("Failed to insert record into table {}".format(error))

if a == 2:
    try:
        id = int(input("Choose the row's id for update"))

        cursor = connection.cursor
        select_query = """select * from student where idstudent = %s"""
        choosen_id=[id]
        cursor.execute(select_query, choosen_id)
        record = cursor.fetchone()
        print(record)

        print('Please fill the rows for update')
        first_name = str(input("first_name:  "))
        last_name = str(input("last_name:  "))
        middle_name = str(input("middle_name:  "))
        iin = str(input("iin:  "))
        if iin_regex.match(iin):
            pass
        else:
            print('iin format is not correct!')
        phone = str(input("phone:  "))
        if phone_regexp.match(phone):
            pass
        else:
            print('phone format is not correct')
        email = str(input("email:  "))
        if email_regex.match(email):
            pass
        else:
            print('email format is not correct')
        address = str(input("address:  "))

        update_query = """Update student set first_name = %s, last_name = %s, middle_name = %s, iin = %s, phone = %s, email = %s, address = %s where idstudent = %s"""
        value = [
            first_name,
            last_name,
            middle_name,
            iin,
            phone,
            email,
            address,
            id,
        ]
        cursor.execute(update_query, value)
        connection.connection.commit()
        print("Record Updated successfully ")

        cursor.execute(select_query)
        record = cursor.fetchone()
        print(record)

    except connection.Error as error:
        print("Failed to update table record: {}".format(error))

if a==3:
    try:
        id = int(input("Choose the row's id for delete"))
        cursor = connection.cursor
        select_query = """select * from student where idstudent = %s"""
        choosen_id = [id]
        cursor.execute(select_query, choosen_id)
        record = cursor.fetchone()
        print(record)

        print('You really want to delete this record?')
        answer = str(input('Write only yes or no \n'))

        if answer == 'yes':
            delete_query = """delete from student where idstudent = %s"""
            cursor.execute(delete_query, choosen_id)
            connection.connection.commit()
            print('the row has been deleted', cursor.rowcount)
        elif answer == 'no':
            print('You destroyed deleting option \n')
        else:
            print('Wrong answer! \n')

    except connection.Error as error:
        print("Failed to delete table record: {}".format(error))


if a == 4:
    try:
        select_query = "select * from student"
        cursor = connection.cursor
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("idstudent = ", row[0], )
            print("first_name = ", row[1])
            print("last_name  = ", row[2])
            print("middle_name  = ", row[3], )
            print("iin  = ", row[4], )
            print("phone  = ", row[5], )
            print("email  = ", row[6], )
            print("address  = ", row[7], "\n")
    except connection.Error as error:
        print("Error reading data from MySQL table".format(error))
