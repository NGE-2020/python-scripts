# This program do the following
# - opens a list of devices to telne
# - save the list of devices in a list
# - asks for user and password
# - then loops entering to devices and sendsa command
# - the output is shown and stored in a file

import getpass
import telnetlib
import time

with open ("device-list.list", "r") as devicelist:
   hosts = []
   hosts=devicelist.readlines()

# with open ("command-list.txt", "r") as commandlist:
#    commands = []
#    commands = commandlist.readlines()
#    print(commands)

user = input("Enter your username: ")
password = getpass.getpass()

for host in hosts:
	tn = telnetlib.Telnet(host)
	time.sleep(2)
	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	time.sleep(2)
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")
	time.sleep(2)
	tn.write(b"show ip int br\n")
	time.sleep(2)
	tn.write(b"exit\n")
	time.sleep(2)
	lastpost = tn.read_all().decode('ascii')
	op = open(host+".txt", "w")
	op.write(lastpost)
	op.close()
	print(lastpost)
	tn.close()