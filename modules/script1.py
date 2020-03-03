#!/usr/bin/env python
import getpass
import time
import json
import requests
from pprint import pprint
from prettytable import PrettyTable

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

def ssh_prepare(device_info, user, pswd):
    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        nodetype = device_list[1]
        ssh_veredict = test_ssh_con(mgmt_ip, nodename, user, pswd)

        if ssh_veredict == 'false':
            ssh_config(mgmt_ip, nodename, nodetype, user, pswd)
            print("Final test for SSH in " , nodename)

            ssh_veredict = test_ssh_con(mgmt_ip, nodename, user, pswd)
            if ssh_veredict == 'true': print("SSH is now configured in ", nodename)
            else: print("\nThere is something wrong with SSH in {node}, please review it with @richo".format(node=nodename))

        else: print("\nSSH is properly configured in ", nodename)

def main():
    user = input("Enter your username: ")
    pswd = getpass.getpass(prompt='Enter your password: ', stream=None)
    device_info = virl_device_data()

    print_table = input("Would you like to see the device list info? ")

    if print_table == (yes or YES or Yes or Y or y):
        table = PrettyTable(['Teamname', 'Scores'])
        for device in device_info:
            table.add_row(device)
        print(table.get_string(title="Device detail"))
        sleep(2)
    elif print_table == (No or no or NO or N or n):
        print('Got it, the script will continue')
    else:
        print('The answer wasn correct, the script will run anyways')

if __name__ == '__main__':
    main()
