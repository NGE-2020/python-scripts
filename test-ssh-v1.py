#!/usr/bin/env python

import time
import paramiko
import os
import threading

initial_time = time.time()

def virl_find_ips():
    # os.system(' fping -g 172.16.30.0/25 | grep -v unreachable > device-list ')
    # time.sleep(25)
    string = os.popen(' more device-list ').read()
    list = string.split('\n')

    ips = []

    for ip in list:
        ip = ip.replace(' is alive', '')
        if '172.16.30.50' in ip:
            pass
        else:
            ips.append(ip)

    ips = ips[:-1]

    ips_to_work = ''

    for ip in ips:
        ips_to_work = ips_to_work + ip + '\n'

    print('\nWill work with the following ips: \n' + ips_to_work)

    return (ips)

def sshconnect(address):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=address, username='cisco', password='cisco')

        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("show ip int br \n")
        time.sleep(1)

        output = remote_connection.recv(65535)
        print('chingon ' + address + '\n')

    except paramiko.SSHException:
        print('valio verga')

    finally:
        ssh_client.close()


def threaths(host, function):
    threaths = []

    for ip in host:
        try:
            th = threading.Thread(target=function, args=(ip,))
            th.start()

        finally:
            threaths.append(th)

    for tr in threaths:
        tr.join()

ipaddr = virl_find_ips()

threaths(ipaddr, sshconnect)
