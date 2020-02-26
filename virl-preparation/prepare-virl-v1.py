import threading
import getpass
import time
import paramiko
import os
import datetime

initial_time = time.time()

def virl_find_ips():
    os.system(' fping -g 172.16.30.0/25 | grep -v unreachable > device-list ')
    time.sleep(25)
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

def sshconnect(address, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=address, username=username, password=password)
        print("\nSSH is properly configured in ", address)

    except:
        print('\nDevice: ' + address + ' is not configured so lets get our hands dirty\n')
        tn = telnetlib.Telnet(address)
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"   conf t\n   crypto key generate rsa modulus 1024\n")
        time.sleep(2)
        tn.write(b"   ip domain-name ngn.com \n   ip ssh version 2\n   exit\n   wr\n")
        time.sleep(2)
        tn.write(b"   exit\n   exit\n")
        tn.close()
        print("SSH configuration done, let's test\n")

        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname = address, username = username, password = password, timeout=5)
            print("SSH test successfully on", address, '\n')
            ssh_client.close

        except:
            print('Seems like there is an issue with the ssh keys on ' +  ip + '\n')


def threaths(host, function):
    threaths = []

    for ip in host:
        try:
            th = threading.Thread(target=function, args=(ip, user, password, ))
            th.start()

        finally:
            threaths.append(th)

        print('Abri el TH en ' + ip)

    for tr in threaths:
        tr.join()


user = input("Enter your username: ")
password = getpass.getpass()

ipaddr = virl_find_ips()

threaths(ipaddr, sshconnect)
