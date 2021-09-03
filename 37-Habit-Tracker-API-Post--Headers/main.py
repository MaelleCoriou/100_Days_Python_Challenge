""" HTTP Requests:
        GET : requests.get() ----> To get data from an API
        POST : requests.post() ----> To send new data ex: twit post
        PUT : requests.put() ----> To update a piece of data
        DELETE : requests.delete() ----> To delete a specific data """

import requests
import os
from datetime import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph2"
TODAY = datetime.now()

#------------------ CREATE PIXELA USER ACCOUNT -------------------#

# Documentation: https://docs.pixe.la/entry/post-user
# Pixela end point
PIXELA_URL = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# To create the user account, set my own token and username, to run once
# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)

#------------------ CREATE PIXELA GRAPH -------------------#

# Documentation: https://docs.pixe.la/entry/post-graph
# Graph end point
graph_url = f"{PIXELA_URL}/{USERNAME}/graphs"

# Params set up to create graph
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ichou"
}

# Set up params for header authentification
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_url, json=graph_params, headers=headers)
# print(response.text)

# Graph created under : https://pixe.la/v1/users/maellec/graphs/graph2.html

#------------------ CREATE GRAPH PIXELATION -------------------#

# Documentation: https://docs.pixe.la/entry/post-graph
# Pixelation end point
pixel_url = f"{graph_url}/{GRAPH_ID}"

# Set pixel params
pixel_params = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": input("How many hours did you work today? ")
}

response = requests.post(url=pixel_url, json=pixel_params, headers=headers)
print(response.text)

#------------------ UPDATE GRAPH PIXELATION -------------------#

# Documentation: https://docs.pixe.la/entry/put-pixel
# Pixelation update end point, set the date to update
update_pixel_url = f"{pixel_url}/20210903"

# Set update params
update_params = {
    "quantity": "3"
}

# response = requests.put(url=update_pixel_url, json=update_params, headers=headers)
# print(response.text)

#------------------ DELETE GRAPH PIXELATION -------------------#

# Documentation: https://docs.pixe.la/entry/delete-pixel
# Pixelation delete end point, set the date to delete
delete_pixel_url = f"{pixel_url}/20210903"

# response = requests.delete(url=update_pixel_url, headers=headers)
# print(response.text)