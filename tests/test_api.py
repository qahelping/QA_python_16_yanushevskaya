import requests
import json

from sevices.cats_services import CatServices


# def test_api_get():
#     r = requests.get('https://httpbin.org/get')
#     assert r
#
# def test_api_get_params():
#     parametrs = {'ANNA': 5, 'DEN': 10}
#     r = requests.get('https://httpbin.org/get', params=parametrs)
#     print(r.url)
#     assert r.url == 'https://httpbin.org/get?ANNA=5&DEN=10'

# def test_api_get_params_text():
#     params = {"limit": "1"}
#     r = requests.get('https://api.thecatapi.com/v1/images/search', params=params)
#     assert r.url == 'https://httpbin.org/get?ANNA=5&DEN=10'

# def test_api_get_params_json():
#     params = {"limit": "1"}
#     response = requests.get('https://api.thecatapi.com/v1/images/search', params=params)
#     response_json = response.json()
#     assert response_json[0].get('height')
#     assert response_json[0].get('id')
#     assert response_json[0].get('url')
#     assert response_json[0].get('width')
#
# def test_api_get_params_json_str_in():
#     params = {"limit": "1"}
#     response = requests.get('https://api.thecatapi.com/v1/images/search', params=params)
#     response_json = response.json()
#     assert 'https://cdn2.thecatapi.com/images/' in response_json[0].get('url')
#
#
# def test_api_get_code_200():
#     params = {"limit": "1"}
#     url = 'https://api.thecatapi.com/v1/images/search'
#     response = requests.get('https://api.thecatapi.com/v1/images/search', params=params)
#     assert response.status_code == 200, f"URL: {url} = 500"
#
#
# def test_api_get_code_500():
#     url = 'https://httpbin.org/status/500'
#     response = requests.get(url)
#     assert response.status_code == 500, f"URL: {url} != 500"
#

# def test_api_history():
#     url = 'http://github.com/'
#     response = requests.get(url)
#     print(response.url)
#     print(response.history)
#
#
# def test_api_raise_for_status():
#     url = 'https://httpbin.org/status/500'
#     response = requests.patch(url)
#
#     try:
#         response.raise_for_status()
#         print('OK')
#     except requests.exceptions.HTTPError as error:
#         print("Fail:", error)
#
#
def test_api_get_params_json():
    cat_services = CatServices()


    response = cat_services.search()
    assert response[0].get('height')
    assert response[0].get('id')
    assert response[0].get('url')
    assert response[0].get('width')
#
#
# def test_api_raise_for_codes_ok():
#     url = 'https://httpbin.org/status/500'
#     response = requests.patch(url)
#     assert response.status_code == requests.codes.ok
#
#
# def test_find_pet_by_id():
#     url = 'https://petstore.swagger.io/v2/pet/1'
#     response = requests.get(url)
#     assert response.status_code == 200
#
#     response_json = response.json()
#     assert response_json.get('id')
#     assert response_json.get('category').get('id')
#     assert response_json.get('category').get('name')
#     assert response_json.get('name') == 'dog'
#     assert response_json.get('status') == 'sold'


def test_api_post():
    body = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    url = 'https://petstore.swagger.io/v2/user/createWithArray'
    reponse = requests.post(url, data=body)
    print(reponse.json())


def test_api_post_json():
    body = [{
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }]

    url = 'https://petstore.swagger.io/v2/user/createWithArray'
    reponse = requests.post(url, data=json.dumps(body))
    print(reponse.json())


def test_add_new_pet_to_the_store():
    name = 'caatty'
    status = 'available'
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "caatty",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": status
    }

    url = 'https://petstore.swagger.io/v2/pet'
    reponse = requests.post(url, data=json.dumps(body))
    reponse_json = reponse.json()
    assert reponse.status_code == 200
    assert reponse_json.get("name") == name
    assert reponse_json.get("status") == name


def test_api_headers():
    url = 'https://petstore.swagger.io/v2/user/createWithArray'
    headers = {'accept': 'application/json',
               'Content-Type': 'application/json'}
    body = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }

    response = requests.post(url, data=body, headers=headers)
    assert response

def test_api_file():
    import logging
    url = 'https://petstore.swagger.io/v2/pet/1/uploadImage'
    headers = {'accept': 'application/json',
               'Content-Type': 'application/json'}

    file = {'file': open ('/Users/elenayanushevskaya/Desktop/QA_python_16_yanushevskaya/cute-cat-relaxing-in-studio_23-2150692717.avif', 'rb')}

    response = requests.post(url, headers=headers, files=file)
    reponse_json = response.json()
    logging.error(f'EROOR {reponse_json}')
