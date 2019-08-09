from fake_useragent import UserAgent
import requests
import time
data = []
for i in links:
    with requests.Session() as s:
        ua = UserAgent()
        x = ua.random
        headers = {"user-agent" : x}
        r = s.get(i, headers=headers)
        data.append(r)
        time.sleep(1)
        print(i)
