import json
import requests
import pprint


response = requests.get('http://10.10.20.160:19399/roster/rest/', auth=('guest', 'guest'))

uglyjson = response.json()

dic_list = []

for k,v in uglyjson.items():
    # for value in v.items():
    #     # device_type.append(value[1])
    dic_list.append(v)
    #print(type(v))

# pprint.pprint(dic_list)

hostname = []

for dic in dic_list:
    try:
        print(dic['NodeName'])
        hostname.append(dic['NodeName'])

    except TypeError:
        pass

    except KeyError:
        pass

print(hostname)

device_type = []
managemnt_ip = []
console_port = []


#
# pprint.pprint(uglyjson['guest|SP-XER-SH0y9u|virl|CER-51'])
#
# # parsed = json.loads(uglyjson)
# # print(json.dumps(parsed, indent=2, sort_keys=True))

