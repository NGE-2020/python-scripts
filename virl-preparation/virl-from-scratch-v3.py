#!/usr/bin/env python

import getpass
import time
import paramiko
import os
import telnetlib
import json
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

def test_ssh_con(address, nodename, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=address, username=username, password=password)
        return('true')
    except ConnectionRefusedError:
        pass
    except:
        return('false')
    finally:
        ssh_client.close()

def sshconnect(mgmt_ip, nodename, nodetype, username, password):
    print('\nConfiguring SSH and Netconf on',nodename, 'with ip', mgmt_ip, "\n")
    if nodetype == 'IOS XRv':
        print('Type not suported yet')
    elif nodetype == 'CSR1000v':
        tn = telnetlib.Telnet(mgmt_ip)
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"   enable\n")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"   conf t\n   crypto key generate rsa modulus 1024\n")
        time.sleep(2)
        tn.write(b"   ip domain-name ngn_richo.com \n   ip ssh version 2\n   aaa new-model\n   exit\n   wr\n")
        tn.write(b"   netconf-yang \n \n \n")
        time.sleep(2)
        tn.write(b"   yes\n ")
        time.sleep(2)
        tn.write(b"   netconf-yang feature candidate-datastore\n ")
        time.sleep(2)
        tn.write(b"   ip http secure-server\n   restconf\n")
        tn.write(b"   exit\n   exit\n")
        tn.close()
        print("Configuration done in ",nodename,"\n")
    else:
        print(nodename,' is not a known type of device\n')

def test_netconf(mgmt_ip):
    try:
        tn = telnetlib.Telnet(mgmt_ip, "830")
        tn.write(b"   exit\n   exit\n")
        tn.close()
        return("true")
    except:
        return("false")

if __name__ == '__main__':

    user = input("Enter your username: ")
    pswd = getpass.getpass(prompt='Enter your password: ', stream=None)

    device_info = virl_device_data()

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        nodetype = device_list[1]
        ssh_veredict = test_ssh_con(mgmt_ip, nodename, user, pswd)
        netconf_veredict = test_netconf(mgmt_ip)

        if ssh_veredict or netconf_veredict == 'false': sshconnect(mgmt_ip, nodename, nodetype, user, pswd)

    print("\n Let's make a final test to confirm\n")

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]

        ssh_veredict = test_ssh_con(mgmt_ip, nodename, user, pswd)
        netconf_veredict = test_netconf(mgmt_ip)

        if ssh_veredict and netconf_veredict == 'true':
            print("\n Both protocols are now configured in ", mgmt_ip)
        else:
            print("\n There is something wrong with SSH or Netconfg in {node}({ip}), please review it with @richo".format(node=nodename, ip=mgmt_ip))
