from yelpapi import YelpAPI
import argparse
from pprint import pprint

api_key ='yours here'
yelp_api = YelpAPI(api_key)

response = yelp_api.search_query(categories='bagels', longitude=-74.167730, latitude=40.848961, limit=50)
pprint(response)

names = []
places = []
ratings = []
reviews = []
for i in range(len(response['businesses'])):
    names.append(response['businesses'][i]['name'])
    places.append((",").join(response['businesses'][i]['location']['display_address'][:]))
    ratings.append(response['businesses'][i]['rating'])
    reviews.append(response['businesses'][i]['review_count'])
    
for i in range(len(names)):
    print(names[i]+"*"+places[i]+"*"+str(ratings[i])+"*"+str(reviews[i]))
