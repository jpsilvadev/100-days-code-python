import time
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from data_manager import DataManager
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
nofication_manager = NotificationManager()

# origin airport
ORIGIN_CITY_IATA = "LON"

# update iata code in sheet data
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # Sleep to avoid hitting API rate limits

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# retrieve customer emails
customer_data = data_manager.get_customer_emails()
customer_emails = [customer_data["whatIsYourEmail?"] for customer_data in customer_data]

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    print("=" * 50)
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.get_flight_data(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now,
    )
    cheapest_flight = find_cheapest_flight(flights)

    print(f"{destination['city']}: £{cheapest_flight.price}")
    print("=" * 50)
    print()
    time.sleep(2)

    # check for indirect flights if no direct flights found
    if cheapest_flight.price == "N/A":
        print("=" * 50)
        print(f"Getting indirect flights for {destination['city']}...")
        indirect_flights = flight_search.get_flight_data(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_now,
            is_direct=False,
        )
        cheapest_flight = find_cheapest_flight(indirect_flights)

        print(f"Cheapest indirect flight: £{cheapest_flight.price}")
        print("=" * 50)
        print()

    # send email if flight is cheaper than the price in the sheet
    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly direct"
                f" from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
                f" on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly from"
                f" {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},"
                f" on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        print("Check your email. Lower price flight found to {destination['city']}.")
        nofication_manager.send_email(customer_emails, message)
        print("Email sent.")
