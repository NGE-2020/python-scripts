#!/usr/bin/env python
import getpass
import time
import json
import requests
from pprint import pprint
from prettytable import PrettyTable
import ngn_get

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

def prepare_lldp(device_info, user, pswd):
    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        nodetype = device_list[1]

        print("\n===== Connecting to {node} with ip {ip} =====\n".format(node=nodename, ip=mgmt_ip))
        lldp = ngn_get.netmiko_xe_get_lldp_neigh(mgmt_ip, user, pswd)
        lldp_configured = 'false'

        if lldp == 'false':
            print("lldp is not configured, let's do it")
            commands = ['lldp run']
            lldp_config = ngn_get.netmiko_xe_config_cmds(commands, mgmt_ip, user, pswd)
            print('lldp was configured succesfully and the output as follows:\n')
            print(lldp_config)
            lldp_configured = 'true'
        else:
            print("See the lldp output as follows:\n")
            print(lldp)

        if lldp_configured == 'true':
            lldp = ngn_get.netmiko_xe_get_lldp_neigh(mgmt_ip, user, pswd)
            print("See the lldp output as follows:\n")

def main():
    user = input("Enter your username: ")
    pswd = getpass.getpass(prompt='Enter your password: ', stream=None)
    device_info = virl_device_data()
    prepare_lldp(device_info, user, pswd)



if __name__ == '__main__':
    main()
