from yelpapi import YelpAPI
import argparse
from pprint import pprint

api_key ='yours here'
yelp_api = YelpAPI(api_key)

import pandas as pd
import censusdata
mydata = censusdata.download('acs5', 2017,
                            censusdata.censusgeo([('state','34'), ('county', '*'),
                            ('county subdivision','*')]),
                            ['B19013_001E', 'B01003_001E'])
mydata['city'] = mydata.index
mydata = mydata.reset_index()

cities = []
clean = []
length = len(mydata['city'])
for i in range (0,length):
    cities.append(str(mydata['city'].to_list()[i]).split(',')[0])
for i in cities:
    end = (len(i.split(' ')))
    i = (i.split(' ')[:end-1])
    clean.append(" ".join(i))
    
df = pd.DataFrame({"City": [],"Income":[],"Population":[]})
df['City'] = clean
df['Income'] = mydata["B19013_001E"]
df['Population'] = mydata['B01003_001E']

county = []
for i in range(len(mydata.city)):
    county.append(str(list(mydata.city)[i]).split(',')[1].split(" ")[1])
    
df['County'] = county

all_data = []
for i in list(df.City):
    try:
        response = yelp_api.search_query(categories='pick a yelp category', location=str(i)+", nj", limit=50)
        names = []
        places = []
        ratings = []
        reviews = []
        phone = []
        lat = []
        lon = []
        for n in range(len(response['businesses'])):
            names.append(response['businesses'][n]['name'])
            places.append((", ").join(response['businesses'][n]['location']['display_address'][:]))
            ratings.append(response['businesses'][n]['rating'])
            reviews.append(response['businesses'][n]['review_count'])
            phone.append(response['businesses'][n]['phone'])
            lat.append(response['businesses'][n]['coordinates']['latitude'])
            lon.append(response['businesses'][n]['coordinates']['longitude'])
        data = {'Store':names, 'address':places,'rating':ratings,'review_count':reviews,
                'phone':phone,'lat':lat,'lon':lon} 
        df = pd.DataFrame(data)
        all_data.append(df)
        print(i,"done...")
    except:
        print(i,"error...")
        pass
new_df = pd.concat(all_data)
new_df = new_df.drop_duplicates()
