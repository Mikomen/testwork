import csv
import connectiondb as connection
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
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


def send_mail():
    msg = MIMEMultipart()
    body_part = MIMEText('New Dump', 'plain')
    msg['Subject'] = 'Mirakhmat Khavazkhanov'
    msg['From'] = 'miko.240067@gmail.com'
    msg['To'] = 'marat_dosmuhanov@mail.ru'
    msg.attach(body_part)
    with open("Dump_{today}.csv",'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name=f"Dump_{today}.csv"))
    servrer = smtplib.SMTP("smtp.gmail.com", 587)
    servrer.login('miko.240067@gmail.com', 'password')
    servrer.sendmail(msg['From'], msg['To'], msg.as_string())
    servrer.quit()