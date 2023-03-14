import smtplib
import datetime as dt
import random

today = dt.datetime.now()
weekday = today.weekday()

my_email = "ikmvarma1998@gmail.com"
password = "lxlztmldseuisqmh"

if weekday == 2:
    my_quotes = [line.strip() for line in open('quotes.txt')]
    quote = random.choice(my_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ikmvarma.gre@gmail.com",
            msg=f"Subject:Today's Motivational Quote\n\n{quote}"
        )
