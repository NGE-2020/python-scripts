import getpass
from time import sleep
import paramiko
import requests

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

def configure_ip_address(device_info,username,password):
    requests.packages.urllib3.disable_warnings()

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]

        headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
        url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native".format(h=mgmt_ip)

        response = requests.get(url, auth=(username, password),
        headers=headers, verify=False)

        print(response.text)
        sleep(5)


if __name__ == '__main__':

    user = input("Enter your username: ")
    pswd = getpass.getpass()

    device_info = virl_device_data()

    configure_ip_address(device_info,user,pswd)
