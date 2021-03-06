import os
import requests
from flight_data import FlightData
from pprint import pprint


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.token = os.environ.get("KIWI_API_KEY")
        self.endpoint = "https://tequila-api.kiwi.com/"
        self.header = {
            "apikey": self.token
        }

    def city_search(self, city_list):
        """ Returns city code based on actual city list in google sheet """
        query = {
            "term": city_list,
            "location_types": "city",
        }
        response = requests.get(
            url=f"{self.endpoint}locations/query",
            params=query,
            headers=self.header)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Get flights on origine_city_code, destination_city_code, from and to dates
        """
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "stop_overs": 0,
            "via_city": "",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{self.endpoint}v2/search",
            headers=self.header,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
        # If there's no flight try with 1 stop over
        except IndexError:
            ##########################
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{self.endpoint}v2/search",
                headers=self.header,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
            except IndexError:
                print(f"No flight available for {destination_city_code}")
                return None
