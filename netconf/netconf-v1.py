from ncclient import manager
import json
from pprint import pprint
import xmltodict
import xml.dom.minidom

netconf_manager = manager.connect(host='ios-xe-mgmt-latest.cisco.com',
								port=10000,username='developer',
								password='C1sco12345',
								hostkey_verify=False,
								allow_agent=False,
								look_for_keys=False,
								device_params={'name': 'csr'})

running_config = netconf_manager.get_config('running')

print(netconf_manager.server_capabilities)

schema = netconf_manager.get_schema('ietf-ip')
print(schema)
# pprint(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

responsejson = xmltodict.parse(str(running_config))
pprint(responsejson['rpc-reply']['data']['native']['interface'])



netconf_manager.close_session()

