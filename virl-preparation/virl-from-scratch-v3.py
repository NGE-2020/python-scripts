#!/usr/bin/env python

import getpass
import time
import paramiko
import telnetlib
import json
import requests
from pprint import pprint
from ncclient import manager

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
        ssh_client.connect(hostname=address, username=username, password=password, look_for_keys=False, allow_agent=False)
        send_command = ssh_client.invoke_shell()
        send_command.send("sh ip int br\n ")
        ssh_client.close()
        return('true')
    except ConnectionRefusedError:
        pass
    except:
        return('false')

def test_netconf(mgmt_ip, username, password):
    try:
        netconf_manager = manager.connect(host=mgmt_ip,username=username,password=password,hostkey_verify=False,allow_agent=False,look_for_keys=False)
        netconf_manager.close_session()
        return("true")
    except:
        return("false")

def ssh_config(mgmt_ip, nodename, nodetype, username, password):
    print('\nConfiguring SSH on',nodename, 'with ip', mgmt_ip)
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
        tn.write(b"   conf t\n   crypto key generate rsa modulus 2048\n")
        time.sleep(1)
        tn.write(b"   line vty 0 4 \n   no password cisco\n   no login authentication\n   privilege level 15\n")
        tn.write(b"   ip domain-name ngn_richo.com \n  aaa new-model\n  lldp run \n   cdp run \n  aaa new-model\n   exit\n   wr\n")
        time.sleep(1)
        tn.write(b"   exit\n   exit\n")
        tn.close()
        print("Configuration done in ",nodename)
    else:
        print(nodename,' is not a known type of device\n')

def netconf_config(mgmt_ip, nodename, nodetype, username, password):
    print('\nConfiguring Netconf on',nodename, 'with ip', mgmt_ip)
    if nodetype == 'IOS XRv':
        print('Type not suported yet')
    elif nodetype == 'CSR1000v':
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=mgmt_ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
            send_command = ssh_client.invoke_shell()
            send_command.send("  conf t\n ")
            time.sleep(1)
            send_command.send("  netconf-yang \n")
            time.sleep(1)
            send_command.send("  yes\n")
            time.sleep(30)
            send_command.send("  netconf-yang feature candidate-datastore \n")
            time.sleep(3)
            send_command.send("  ip http secure-server\n aaa authentication login default local\n aaa authorization exec default local\n")
            send_command.send("  restconf\n ")
            time.sleep(1)
            send_command.send("end\n ")
            send_command.send("wr\n ")
        except ConnectionRefusedError:
            pass
        finally:
            ssh_client.close()
        print("Configuration done in ",nodename)
    else:
        print(nodename,' is not a known type of device\n')

def netconf_prepare(device_info, user, pswd):
    for device_list in device_info:
        mgmt_ip = device_list[3]
        nodename = device_list[0]
        nodetype = device_list[1]
        netconf_veredict = test_netconf(mgmt_ip, user, pswd)

        if netconf_veredict == 'false':
            netconf_config(mgmt_ip, nodename, nodetype, user, pswd)
            print("Final test for Netconf in " , nodename)

            netconf_veredict = test_netconf(mgmt_ip, user, pswd)
            if netconf_veredict == 'true': print("Netconf is now configured in ", nodename)
            else: print("\nThere is something wrong with Netconf in {node}, please review it with @richo".format(node=nodename))
        else: print("\nNetconf is properly configured in ", nodename)

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
    ssh_prepare(device_info, user, pswd)
    netconf_prepare(device_info, user, pswd)

if __name__ == '__main__':
    main()
