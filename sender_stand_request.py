import configuration
import requests
import data
from data import new_kit


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.text)

user_response_data = response.json()



auth_token = user_response_data.get("authToken")
data.headers["Authorization"] = f"Bearer {auth_token}"



def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=data.new_kit, headers=data.headers)
kit_response = post_new_client_kit(data.new_kit)

print(kit_response.status_code)
print(kit_response.text)