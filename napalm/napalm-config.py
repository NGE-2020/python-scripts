import napalm
from pprint import pprint as pp
from time import sleep

driver = napalm.get_network_driver('ios')

list_of_devices = ['ios-xe-mgmt-latest.cisco.com']

for device in list_of_devices:
    connection = driver(hostname=device, username='developer', password='C1sco12345', optional_args={'port': 8181})
    connection.open()

    pp(connection.get_interfaces())
    print('\n \n')

    configuration =('interface loopback 667')

    connection.load_merge_candidate(config=configuration)
    print(connection.compare_config())
    connection.commit_config()

    pp(connection.get_interfaces())
    print('\n \n')

    connection.close()

