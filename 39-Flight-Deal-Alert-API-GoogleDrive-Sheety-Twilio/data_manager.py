import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.environ.get("SHEETY_TOKEN")
        self.endpoint = os.environ.get("URL_PRICES_ENDPOINT")
        self.header = {
            "Authorization": f"bearer {self.token}"
        }
        self.data = {}

    def read_data(self):
        """
        Read current data in Google sheet. Data saved in self.data dic
        """
        response = requests.get(self.endpoint,
                                headers=self.header)
        data = response.json()
        self.data = data["prices"]
        return self.data

    def update_destination_code(self, id, iata):
        """
        Updates Google sheet on iataCode by id lines
        """
        new_data = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(
            url=f"{self.endpoint}/{id}",
            json=new_data,
            headers=self.header
        )
        print(response.text)

