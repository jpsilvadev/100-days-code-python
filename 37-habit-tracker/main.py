"""Graph at --> https://pixe.la/v1/users/USERNAME/graphs/learn-ml-graph.html"""

import requests
from datetime import datetime

USERNAME = "SOME USERNAME"
TOKEN = "SOME TOKEN"
GRAPH_ID = "learn-ml-graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# create user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "learn-ml-graph",
    "name": "Learning ML",
    "unit": "pages",
    "type": "int",
    "color": "sora",
}

headers = {"X-USER-TOKEN": TOKEN}

# graph_response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# add pixels to graph

today = datetime.now()

add_pixel_to_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

add_pixel_tp_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

add_pixel_response = requests.post(
    url=add_pixel_tp_graph_endpoint, json=add_pixel_to_graph_params, headers=headers
)
print(add_pixel_response.text)

# update pixel


update_params = {"quantity": "30"}

update_pixel_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(update_pixel_response.text)

delete_pixel_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
)

# delete_pixel_response = requests.delete(
#     url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)
