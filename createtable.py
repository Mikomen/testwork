import connectiondb as connection
import mysql.connector

try:

    mySql_Create_Table_Query = """CREATE TABLE `testdb`.`student` (
                                  `idstudent` INT NOT NULL AUTO_INCREMENT,
                                  `first_name` VARCHAR(45) NOT NULL,
                                  `last_name` VARCHAR(45) NOT NULL,
                                  `middle_name` VARCHAR(45) NOT NULL,
                                  `iin` INT(12) NOT NULL,
                                  `phone` INT(11) NOT NULL,
                                  `email` VARCHAR(45) NOT NULL,
                                  `address` VARCHAR(45) NOT NULL,
                                  PRIMARY KEY (`idstudent`));"""

    cursor = connection.cursor
    result = cursor.execute(mySql_Create_Table_Query)
    print("Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
