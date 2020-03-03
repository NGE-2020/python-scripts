import napalm
from netmiko import ConnectHandler

def netmiko_xe_get_cdp_neigh(ip, user, pswd, port=22):
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username=user, password=pswd, port=port)
        output = net_connect.send_command("show cdp neighbor")

    finally:
        if "CDP is not enabled" in output:
            return("false")
        else:
            return(output)

def netmiko_xe_get_lldp_neigh(ip, user, pswd, port=22):
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username=user, password=pswd, port=port)
        output = net_connect.send_command("show lldp neighbor")

    finally:
        if "LLDP is not enabled" in output:
            return("false")
        else:
            return(output)

def netmiko_xe_get_interfaces(ip, user, pswd, port=22):
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username=user, password=pswd, port=port)
        output = net_connect.send_command("show interface description")

    finally:
        if "LLDP is not enabled" in output:
            return("false")
        else:
            return(output)

def netmiko_xe_show_cmds(command_list, ip, user, pswd, port=22):
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username=user, password=pswd, port=port)
        final_output = ('')
        for command in command_list:
            output = net_connect.send_command(command)
            final_output = final_output + output
    finally:
        return(final_output)

def netmiko_xe_config_cmds(command_list, ip, user, pswd, port=22):
    try:
        net_connect = ConnectHandler(device_type='cisco_ios', host=ip, username=user, password=pswd, port=port)
        output = net_connect.send_config_set(command_list)
    finally:
        return(output)

port = 8181
ip = "ios-xe-mgmt-latest.cisco.com"
user = "developer"
pswd = "C1sco12345"
command_list = ['cdp run', 'lldp run']
print(netmiko_xe_get_lldp_neigh(ip, user, pswd, port))
