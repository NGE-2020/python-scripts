import napalm
from pprint import pprint as pp
from time import sleep
driver = napalm.get_network_driver('ios')

list_of_devices = ['ios-xe-mgmt-latest.cisco.com']

for device in list_of_devices:
    connection = driver(hostname=device, username='developer', password='C1sco12345', optional_args={'port': 8181})
    connection.open()
    destination = '8.8.8.8'
    pp(connection.get_facts())
    print('\n \n')
    pp(connection.is_alive())
    print('\n \n')
    pp(connection.get_interfaces())
    print('\n \n')
    pp(connection.get_lldp_neighbors())
    print('\n \n')
    pp(connection.get_arp_table())
    print('\n \n')
    # pp(connection.get_bgp_neighbors())
    # print('\n \n')
    pp(connection.get_config())
    print('\n \n')
    # pp(connection.get_interface_counters())
    # print('\n \n')
    pp(connection.get_interfaces_ip())
    print('\n \n')
    pp(connection.get_lldp_neighbors_detail())
    print('\n \n')
    pp(connection.get_mac_address_table())
    print('\n \n')
    # pp(connection.get_network_instances())
    # print('\n \n')
    pp(connection.get_route_to(destination))
    print('\n \n')
    pp(connection.ping(destination))
    print('\n \n')
    pp(connection.traceroute(destination))
    print('\n \n')

    connection.close()

