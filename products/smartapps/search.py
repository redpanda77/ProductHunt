import requests
from pprint import pprint
import pandas as pd
import psycopg2
from django.utils import timezone
import datetime

# For this example, the API key is provided as a command-line argument.


def google_search(search_term):

    api_key = 'AIzaSyB0NxLzrqTRi_TUyQDsPKjGXRYmpcVNQL0'
#'AIzaSyAuNM3SehKx2kCFXUR5Ad6SM0aLll6FbQU'

    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    parameters = {
        'key': api_key,
        'query': search_term,
    }

    headers = {
        'Content-Type': 'application/json',
    }

    r = requests.get(url, params=parameters)
    response = r.json()
    restaurants = response['results']

    pprint(response)


    restaurant_list = list()
    for element in restaurants:
        rest_info = dict()
        rest_info['name'] = element['name']
        rest_info['place_id'] = element['place_id']
        rest_info['formatted_address'] = element['formatted_address']
        rest_info['rating'] = element['rating']
        rest_info['types'] = element['types']
        rest_info['photo'] = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + element['photos'][0]['photo_reference']# + '&key=' + api_key
        #rest_info['photos'] = element['photos']
        rest_info['geometry'] = element['geometry']['location']
        rest_info['place_id'] = element['place_id']
        restaurant_list.append(rest_info)

    return restaurant_list