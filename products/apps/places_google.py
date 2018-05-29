import requests
from pprint import pprint

# For this example, the API key is provided as a command-line argument.
api_key = 'AIzaSyAuNM3SehKx2kCFXUR5Ad6SM0aLll6FbQU'

url = 'https://maps.googleapis.com/maps/api/place/details/output'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'


parameters = {
    'key': api_key,
    'query': 'restaurantes las rozas',
}

headers = {
    'Content-Type': 'application/json',
}

r = requests.get(url, params=parameters)
response = r.json()
restaurants = response['results']
for element in restaurants:
    print(element['place_id'])
    print(element['name'])
    print(element['formatted_address'])
    #print(element.id)
    print(element['rating'])
    print(element['types'])
    print(element['photos'])
    print(element.geometry)
    print('-----')


