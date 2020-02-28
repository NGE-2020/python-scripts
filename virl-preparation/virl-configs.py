import getpass
from time import sleep
import paramiko
from ncclient import manager
from ncclient.transport.errors import AuthenticationError, SessionCloseError, SSHError, SSHUnknownHostError, NetconfFramingError
import json
from pprint import pprint
import xmltodict
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

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]

        netconf_manager = manager.connect(host=mgmt_ip,username=username,password=password,hostkey_verify=False,allow_agent=False,look_for_keys=False)

        try:
            running_config = netconf_manager.get_config('running')

        except:

        raise SSHError:
            print("Could not open socket")

        finally:
            responsejson = xmltodict.parse(str(running_config))
            pprint(responsejson['rpc-reply']['data']['native']['interface'])
            netconf_manager.close_session()


if __name__ == '__main__':
    user = input("Enter your username: ")
    pswd = getpass.getpass(prompt='Enter your password: ', stream=None)

    device_info = virl_device_data()

    configure_ip_address(device_info,user,pswd)
