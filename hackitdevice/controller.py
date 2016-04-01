__author__ = 'mmoisen'

from models import Probe
import time


PROBE_FILE_NAME = '28-000004a8649d'

probe = Probe(file_name=PROBE_FILE_NAME)

def start():
    while True:
        try:
            temp = probe.temp
        except Exception as ex:
            print "Exception: ", ex.message

        print "temp is ", temp

        time.sleep(2)
