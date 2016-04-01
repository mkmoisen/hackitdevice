__author__ = 'mmoisen'
import sys
import requests
from config import FRAMEWORK_URL, DEVICE_UUID
import json

url = FRAMEWORK_URL + '/hackit/device/ip/'
ip = sys.argv[1]

ip += ':5000'
headers = {'Content-Type': 'application/json'}
data = json.dumps({'device_uuid': DEVICE_UUID, 'ip': ip})
r = requests.post(url, data, headers=headers, verify=False)

failed = True
if r.status_code == 200:
    if r.json()['success']:
        failed = False

'''
args = ['/home/pushover.sh', '-T', 'aZMFQxkVrmhEw8EUAYZEB75FMDXWbS', '-U', 'uwbm6zLzbs1YBtHPGg1aM5t9S3dAut', '"Failed to register IP address!"']
p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()


10.154.242.229:5000
'''