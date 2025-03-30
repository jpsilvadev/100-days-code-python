"""Send quote if current day"""

import smtplib
import datetime as dt
import random

current_time = dt.datetime.now().weekday()

if current_time == 6:
    with open("quotes.txt", "r") as quotes:
        data = [quote.strip() for quote in quotes.readlines()]
        quote = random.choice(data)

    my_email = "SOMEEMAIL@gmail.com"
    my_password = "SOMEPASSWORD"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="SOMEEMAIL@gmail.com",
            msg=f"Subject:Quote\n\n{quote}",
        )
