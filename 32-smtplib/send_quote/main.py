# import smtplib

# my_email = "jpsjoaosilvadevtesting@gmail.com"
# my_password = "lnfdapiprqqohzbf"


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="minusw0w2@gmail.com",
#         msg="Subject:Hello\n\nThis is a test email!"
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
