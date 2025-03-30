import pandas as pd
import datetime as dt
import random
import smtplib

df = pd.read_csv("birthdays.csv", header=None)
df.columns = ["name", "email", "year", "month", "day"]

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

todays_birthday = df[(df["month"] == current_month) & (df["day"] == current_day)]


birthday_dict = todays_birthday[["name", "email"]].to_dict(orient="records")
random_num = random.randint(1, 2)

with open(f"letter_templates/letter_{random_num}.txt") as file:
    letter = file.read().replace("[NAME]", birthday_dict[0]["name"])

my_email = "jpsjoaosilvadevtesting@gmail.com"
my_password = "lnfdapiprqqohzbf"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_dict[0]["email"],
        msg=f"Subject:Happy Birthday\n\n{letter}",
    )
