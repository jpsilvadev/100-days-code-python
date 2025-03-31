import requests
from twilio.rest import Client

API_KEY = "SOME KEY HERE"
MY_LAT = 90.136940  # toulouse cause it was raining
MY_LONG = -200.499460

account_sid = "SOME SID HERE"
auth_token = "SOME TOKEN HERE"


params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "minutely,daily,current",
    "appid": API_KEY,
}


request = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/onecall", params=params
)
request.raise_for_status()

data = request.json()
data_12h = data["hourly"][:12]


will_rain = False
for hour_data in data_12h:
    check_rain = hour_data["weather"][0]["id"]
    if check_rain < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella ☔.",
        from_="+SOME NUMBER HERE",
        to="+SOME NUMBER HERE",
    )
    print(message.status)
