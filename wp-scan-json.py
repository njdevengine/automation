import os
import json

site = "www.yoursite.com"
os.system('wpscan --url'+' '+site+' -o '+site.split('.')[1]+' -f json')
with open(site.split('.')[1], 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)
obj
