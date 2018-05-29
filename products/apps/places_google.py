import requests
from pprint import pprint
import pandas as pd
import psycopg2
from django.utils import timezone
import datetime

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

df = pd.DataFrame()
ids = list()
names = list()
addresses = list()
ratings = list()
types = list()
photos = list()
geoms = list()


for element in restaurants:
    valores = list()
    ids.append(element['place_id'])
    names.append(element['name'])
    addresses.append(element['formatted_address'])
    ratings.append(element['rating'])
    types.append(element['types'])
    photos.append(element['photos'])
    geoms.append(element['geometry'])

    valores.append(str(element['name']))
    valores.append(str(element['place_id']))
    valores.append(str(timezone.datetime.now()))
    valores.append(str('No description'))
    valores.append(str(element['formatted_address']))
    valores.append(str(element['rating']))
    valores.append(str(element['types']))
    valores.append(str(element['geometry']))
    valores.append(str('google.com'))
    valores.append(1)

    fields = "name, product_id, pub_date, body, address, rating, categories, coordinates, url, votes_total"
    conn_string = "host='localhost' dbname='restopoint' user='postgres' password='77'"
    connection = psycopg2.connect(conn_string)
    cur = connection.cursor()
    statement =  "INSERT into products_product ("+fields+") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cur.execute(statement, valores)
    connection.commit()

df['ids'] = ids
df['names'] = names
df['addresses'] = addresses
df['ratings'] = ratings
df['types'] = types
df['photos'] = photos
df['geoms'] = geoms

#print(df)



