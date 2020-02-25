#!/usr/bin/env python

import threading
import getpass
import time
import paramiko
import os
import datetime
import telnetlib
import json
import requests
from pprint import pprint

initial_time = time.time()

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

def test_ssh_con(address, nodename, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=address, username=username, password=password)
        time.sleep(1)
        print("\nSSH is properly configured in",nodename)
        return('true')

    except ConnectionRefusedError:
        pass

    except:
        time.sleep(1)
        print("\nSSH is not configured in",nodename)
        return('false')

    finally:
        ssh_client.close()

def sshconnect(mgmt_ip, port, nodename, nodetype, username, password):

    ssh_attempt = test_ssh_con(mgmt_ip, nodename, username, password)

    if ssh_attempt == 'false':
        time.sleep(1)
        print('\n Configuring SSH on',nodename, 'with ip', mgmt_ip)

        if nodetype == 'IOS XRv':
            print('Type not suported yet')
        elif nodetype == 'CSR1000v':
            tn = telnetlib.Telnet(mgmt_ip)
            tn.write(b" \n")
            tn.read_until(b">")
            tn.write(b" enable\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.read_until(b"Username: ")
            # tn.write(username.encode('ascii') + b"\n")
            # tn.read_until(b"Password: ")
            # tn.write(password.encode('ascii') + b"\n")
            tn.write(b" conf t\n crypto key generate rsa modulus 1024\n")
            tn.read_until(b"#")
            tn.write(b" ip domain-name ngn.com \n ip ssh version 2\n aaa new-model\n exit\n wr\n")
            tn.read_until(b"#")
            tn.write(b" exit\n exit\n")
            tn.close()
            print("SSH configuration done in \n",nodename)

        else:
            print(nodename,' is not a known type of device\n')

def prepare_threaths(device_info, password, username, function):
    threaths = []

    for device_list in device_info:
        mgmt_ip = device_list[3]
        port = device_list[2]
        nodename = device_list[0]
        nodetype = device_list[1]
        try:
            th = threading.Thread(target=function, args=(mgmt_ip ,port, nodename, nodetype, username, password, ))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

def testssh_threaths(device_info, password, username, function):
    threaths = []

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        try:
            th = threading.Thread(target=function, args=(mgmt_ip, nodename, username, password, ))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

user = input("Enter your username: ")
pswd = getpass.getpass()

device_info = virl_device_data()

prepare_threaths(device_info, pswd, user, sshconnect)

print("\n Let's make a final test to confirm\n")

testssh_threaths(device_info, pswd, user, test_ssh_con)
