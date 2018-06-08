#!/usr/bin/env python2

import requests

# put your keys in the header
headers = {
    "app_id": "5849c259",
    "app_key": "20f3b7f8be7d437a09825ef63a777460"
}

payload = '{"image":"https://vignette.wikia.nocookie.net/theperksofbeingawallflower/images/4/42/018.jpg/revision/latest?cb=20140925021337"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content
