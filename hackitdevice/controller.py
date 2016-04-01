__author__ = 'mmoisen'

from models import Probe
import time
import requests
from config import FRAMEWORK_URL
from config import FRAMEWORK_PUSH
url = FRAMEWORK_URL + FRAMEWORK_PUSH
device_uuid = 'abcdefg'
from datetime import datetime
import json


PROBE_FILE_NAME = '28-000004a8649d'

probe = Probe(file_name=PROBE_FILE_NAME)

def start():
    while True:
        time.sleep(2)
        try:
            temp = probe.temp
        except Exception as ex:
            print "Exception: ", ex.message
            continue

        print "temp is ", temp
        location = 'California'
        dt = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({"uuid": device_uuid, "payload": {"temperature": temp, 'dt': dt}})
        r = requests.post(url, data, headers=headers)

        print r.json()