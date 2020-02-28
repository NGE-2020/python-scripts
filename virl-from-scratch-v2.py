
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
        print("\nSSH is properly configured in",nodename)
        return('true')

    except ConnectionRefusedError:
        pass

    except:
        print("\nSSH is not properly configured in",nodename)
        return('false')

    finally:
        ssh_client.close()

def sshconnect(device_info, username, password):

    for device_list in device_info:
        mgmt_ip = device_list[3]
        port = device_list[2]
        nodename = device_list[0]
        nodetype = device_list[1]

        ssh_attempt = test_ssh_con(mgmt_ip, nodename, username, password)

        if ssh_attempt == 'false':
            print('\nConfiguring SSH on',nodename, 'with ip', mgmt_ip)

            if nodetype == 'IOS XRv':
                print('Type not suported yet')

            elif nodetype == 'CSR1000v':
                tn = telnetlib.Telnet(mgmt_ip)
                tn.read_until(b"Username: ")
                tn.write(username.encode('ascii') + b"\n")
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
                tn.write(b"   conf t\n   crypto key generate rsa modulus 1024\n")
                time.sleep(1)
                tn.write(b"   ip domain-name ngn.com \n   ip ssh version 2\n   aaa new-model\n   exit\n   wr\n")
                time.sleep(1)
                tn.write(b"   netconf-yang \n  yes\n ")
                time.sleep(1)
                tn.write(b"   netconf-yang feature candidate-datastore\n ")
                time.sleep(1)
                tn.write(b"   ip http secure-server\n   restconf\n")
                time.sleep(1)
                tn.write(b"   exit\n   exit\n")
                tn.close()
                print("SSH configuration done in",nodename,"\n")

            else:
                print(nodename,' is not a known type of device\n')

if __name__ == '__main__':

    user = input("Enter your username: ")
    pswd = getpass.getpass()

    device_info = virl_device_data()

    sshconnect(device_info, pswd, user)

    print("\n Let's make a final test to confirm\n")

    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        test_ssh_con(mgmt_ip, nodename, user, pswd)
