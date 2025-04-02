import os
from dotenv import load_dotenv
import requests

load_dotenv()


TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        # access token refreshes at every ~30 minutes, so calling this method each initialization
        self._access_token = self._get_access_token()

    def _get_access_token(self):
        header = {"Content-Type": "application/x-www-form-urlencoded"}

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(TOKEN_ENDPOINT, headers=header, data=body, timeout=30)
        return response.json().get("access_token")

    def get_destination_code(self, city_name):
        header = {"Authorization": f"Bearer {self._access_token}"}
        params = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS",
        }

        response = requests.get(
            IATA_ENDPOINT, headers=header, params=params, timeout=30
        )
        try:
            return response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"City {city_name} not found.")
            return None
        except KeyError:
            print(f"Error retrieving data for city {city_name}.")
            return None

    def get_flight_data(
        self, origin_code, destination_code, from_time, to_time, is_direct=True
    ):
        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers={"Authorization": f"Bearer {self._access_token}"},
            params=params,
            timeout=30,
        )

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        return response.json()
