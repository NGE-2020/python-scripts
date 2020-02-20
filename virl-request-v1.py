#!/usr/bin/env python
import json
import requests
import pprint

def virl_device_data():
    response = requests.get('http://10.10.20.160:19399/roster/rest/', auth=('guest', 'guest'))

    uglyjson = response.json()

    dic_list = [v for k,v in uglyjson.items()]

    onlyrouters_dic = [pair for pair in dic_list if 'PortConsole' in pair ]

    finaldata = []

    for pair in onlyrouters_dic:
        temp_list = [value for key, value in pair.items() if key == 'PortConsole' or key == 'NodeSubtype' or key == 'NodeName' or key == 'managementIP']
        finaldata.append(temp_list)

    return(finaldata)

pprint.pprint(virl_device_data())
