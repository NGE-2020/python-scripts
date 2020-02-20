import getpass
import telnetlib
import time
import datetime
import paramiko
import os

initial_time = time.time()

current_time = datetime.datetime.now()
daytime = current_time.strftime("%Y-%m-%d-%H-%M")

# os.system(' fping -g 172.16.30.0/24 | grep -v unreachable > device-list ')
# time.sleep(25)
string = os.popen(' more device-list ').read()
list = string.split('\n')

ips = []

for ip in list:
    ip = ip.replace(' is alive', '')
    if '172.16.30.254' in ip:
        pass
    elif '172.16.30.50' in ip:
        pass
    else:
        ips.append(ip)

ips = ips[:-1]

ips_to_work = ''

for ip in ips:
    ips_to_work = ips_to_work + ip + '\n'

print('\nWill work with the following ips: \n' + ips_to_work)

user = input("Enter your username: ")
password = getpass.getpass()

for ip in ips:
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname = ip, username =user, password = password)
        ssh_client.close
        print("SSH is properly configured in ", ip)

    except paramiko.SSHException:
        pass

    finally:
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"show version \n")
        tn.write(b"    exit\n")
        tn.write(b"    exit\n")
        version = tn.read_all().decode('ascii')
        tn.close()

        if 'Cisco IOS XR' in version:
            print('Device: ' + ip + ' is an IOS XR device, proceeding to configure it\n')
            tn = telnetlib.Telnet(ip)
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"   configure \n   domain name ngn.com \n   ssh server v2\n   commit\n")
            time.sleep(2)
            tn.write(b"   end \n   crypto key generate rsa general-keys\n")
            time.sleep(2)
            tn.write(b"   yes\n")
            time.sleep(2)
            tn.write(b"   1024\n")
            print('aqui voy')
            tn.write(b"   \n   exit\n")
            print('aqui voy')
            tn.close()
            print("SSH configuration done\n")

        elif 'Cisco IOS XE' in version:
            print('device: ' + ip + ' is an IOS XE device, proceeding to configure it\n')
            tn = telnetlib.Telnet(ip)
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"   conf t\n   crypto key generate rsa modulus 1024\n")
            time.sleep(2)
            tn.write(b"   ip domain-name ngn.com \n   ip ssh version 2\n   exit\n   wr\n")
            time.sleep(2)
            tn.write(b"   exit\n   exit\n")
            tn.close()
            print("SSH configuration done\n")

        else:
            print('This is not a known type of device\n')

elapsed_time = time.time() - initial_time
print("\n===== This script took: ===== \n" + str(elapsed_time) + " sec\n" + "===== to finish the task =====")
