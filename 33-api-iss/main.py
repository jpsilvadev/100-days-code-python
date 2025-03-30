"""API Lectures"""

import smtplib
from datetime import datetime
import time
import requests

MY_LAT = 40.136940  # Your latitude
MY_LONG = -7.499460  # Your longitude

MY_EMAIL = "SOMEEMAIL@gmail.com"
MY_PASSWORD = "SOME_PASSWORD_HERE"


def is_iss_overhead():
    """Check if ISS is overhead"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night_time():
    """Check if dark outside"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset and time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS Overhead\n\nLook up!",
            )
        break
