__author__ = 'mmoisen'
import time
import requests
from config import FRAMEWORK_URL
from config import FRAMEWORK_PUSH
url = FRAMEWORK_URL + FRAMEWORK_PUSH
from config import DEVICE_UUID
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from datetime import datetime
import json
def start():
    while True:
        temp = int(raw_input("Please enter a temperature: "))
        print "the temp was ", temp
        location = 'California'
        dt = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({"uuid": DEVICE_UUID, "payload": {"temperature": temp, 'dt': dt}})
        r = requests.post(url, data, headers=headers, verify=False)

        print r.json()