import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, headers=data.headers)

def post_new_client_kit(body):
    response = post_new_user(data.user_body)
    user_response_data = response.json()
    auth_token = user_response_data.get("authToken")

    new_headers = data.headers.copy()
    new_headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=body, headers=new_headers)

kit_response = post_new_client_kit(data.new_kit)
