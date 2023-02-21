import datetime as dt
import smtplib

now = dt.datetime.now()

year = now.year
month = now.month
minute = now.minute
day_of_the_week = now.weekday()

dob = dt.datetime(year=1997, month=9, day=27)

my_email = "jodsnmedia@gmail.com"
password = "Frogman28@(0)jodsmedia(0)"

with smtplib.SMTP("smtp.mailgun.org") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="dkerobean@gmail.com",
                        msg="Subject:Hello from python\n\n this is the content"
                        )





