import csv
import connectiondb as connection
from datetime import datetime
today = datetime.now().strftime("%d-%m-%y %H-%M-%S")


with open(f"Dump_{today}.csv", "w", encoding="utf-8") as file:
    queryset = "SELECT first_name, last_name, middle_name, iin, phone, email, address FROM student;"
    cur = connection.cursor
    cur.execute(queryset)
    rows = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    fp = open(f"dump_{today}.csv", 'w')
    dump = csv.writer(fp, lineterminator='\n')
    dump.writerow(column_names)
    dump.writerows(rows)
    fp.close()



