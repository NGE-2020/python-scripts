import getpass
import telnetlib

host = "172.16.30.54"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"show ip int br\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))