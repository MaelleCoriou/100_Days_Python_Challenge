from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from email_manager import EmailManager

ORIGIN_CITY_IATA = "NTE,PAR"

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
email_manager = EmailManager()

# Current data in Google sheet
current_data = data_manager.read_data()

# iataCode update in Google sheet if code isn't entered
for city in current_data:
    if city["iataCode"] == "":
        # Call city_search to get iatacode
        city["iataCode"] = flight_search.city_search(city['city'])
        # Update Google sheet with line id and iatacode
        response = data_manager.update_destination_code(id=city["id"], iata=city["iataCode"])
        # Update current data to get the next empty iatacode
        current_data = data_manager.read_data()

# print(current_data)

# Date set up
today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in current_data:
    # Check flights for each destination
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )
    
    if flight is None:
        continue

    # If cost is lower than the price in Google sheet send an alert
    if flight.price < destination["lowestPrice"]:
        users = data_manager.users()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only {flight.price} Euros to fly from {flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        email_manager.send_email(emails, message, link)
