import requests
import sys
from time import sleep

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# use the IP address or hostname of your Cat9300
HOST = ('ios-xe-mgmt-latest.cisco.com')
PORT = (9443)

# use your user credentials to access the Cat9300
USER = ("developer")
PASS = ("C1sco12345")

# RESTCONF media types for REST API headers
headers = {'Content-Type': 'application/yang-data+json',
'Accept': 'application/yang-data+json'}

url = "https://{h}:{p}/restconf/data/iana-hardware:hardware".format(h=HOST,p=PORT)

# this statement performs a GET on the specified url
response = requests.get(url, auth=(USER, PASS),
headers=headers, verify=False)

# print the json that is returned
print(response.text)
sleep(5)

