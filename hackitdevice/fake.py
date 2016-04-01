__author__ = 'mmoisen'
import time
import requests
framework_url = 'http://127.0.0.1:5000'
framework_push = '/hackit/device/payload/post/'
url = framework_url + framework_push
device_uuid = 'abcdefg'
from datetime import datetime
import json
def start():
    while True:
        temp = int(raw_input("Please enter a temperature: "))
        print "the temp was ", temp
        location = 'California'
        dt = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({"uuid": device_uuid, "payload": {"temperature": temp, 'dt': dt}})
        r = requests.post(url, data, headers=headers)

        print r.json()