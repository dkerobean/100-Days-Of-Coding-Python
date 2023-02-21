import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as quotes:
    quote = quotes.readlines()

my_email = "jodsnmedia@gmail.com"
password = "password!345)"
message = random.choice(quote)
print(message)


if day_of_week == 0:
    with smtplib.SMTP("smtp.mailgun.org") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dkerobean@gmail.com",
                            msg=f"Subject:Hello from python\n\n {message}"
                            )