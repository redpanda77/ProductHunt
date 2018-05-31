import requests
from pprint import pprint

# For this example, the API key is provided as a command-line argument.
api_key = 'tpk4ikuf8bChSG_FVMN463OBQadgLs_J317HaxfraCrpqnONm0iBJZBMWWEeOn-OgeBa5LYbepxTOxZ6M8DcRmg-_-O0_tcUJxfvQA2fslAaK8KAREskuFshqiUNW3Yx'


url = 'https://api.yelp.com/v3/businesses/search'

headers = {
        'Authorization': 'Bearer %s' % api_key,
}

parameters = {
    'term': 'restaurantes',
    'location': 'las rozas',

}

r = requests.get(url, headers=headers, params=parameters)
response = r.json()
restaurants = response['businesses']

for element in restaurants:
    print(element['alias'])
    print(element['categories'])
    print(element['coordinates'])
    print(element['display_phone'])
    print(element['distance'])
    print(element['image_url'])
    print(element['location'])
    print(element['name'])
    print(element['price'])
    print(element['rating'])
    print(element['review_count'])
    print(element['url'])
    print('----')




