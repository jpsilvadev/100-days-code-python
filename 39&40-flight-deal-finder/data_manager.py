import os
from dotenv import load_dotenv
import requests
import requests.auth

load_dotenv()


class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")

        self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
        self._auth = requests.auth.HTTPBasicAuth(self._user, self._password)

        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, auth=self._auth, timeout=30)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}

            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                auth=self._auth,
                json=new_data,
                timeout=30,
            )

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self._auth, timeout=30)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
