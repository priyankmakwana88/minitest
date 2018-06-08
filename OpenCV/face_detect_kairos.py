#!/usr/bin/env python2

import requests

# put your keys in the header
headers = {
    "app_id": "xxxx",
    "app_key": "xxxx"
}

payload = '{"image":"https://vignette.wikia.nocookie.net/theperksofbeingawallflower/images/4/42/018.jpg/revision/latest?cb=20140925021337"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content
