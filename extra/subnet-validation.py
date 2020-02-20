import os
import subprocess

subnets = []

with open('/home/quezrica/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        for item in words:
            octets= item.split('.')
            if len(octets)==4:
                if '/' in item:
                    subnets.append(item)
                else:
                    item = item[:-1]
                    item = item + '/32,'
                    subnets.append(item)

f.close()

regions = {"iad" : 'iad2-br-cor-r1', "dub" : 'dub2-br-cor-r1', "syd" : 'syd1-br-cor-r1', "gru" : 'gru3-br-cor-r1'}

common_1 = '/apollo/env/NetengAutoChecks/bin/autochecks_manager --no-login-prompt --checks routes.check_ip_prefix_longer_not_exist --target '
common_2 = ' --prefix "'

print('Copy the following entries and paste in the nebastion shown\n')

string = ''

for subnet in subnets:
    string = string + subnet

string = string[:-1] + '"'

for key,val in regions.items():
    print("nebastion-" + key)
    print(common_1 + val + common_2 + string + '\n')

region = input("Please provide the region of the implementation: ")

regional_br_cor = os.popen('ls ~/GenevaBuilder/targetspec/border | grep br-cor-r1 | grep ' + region).read()

list_br_cor = regional_br_cor.replace(' ', '')
list_br_cor = regional_br_cor.split('\n')
list_br_cor.pop(2)

for br_cor in list_br_cor:
    reg = br_cor[:3]
    if reg in regions.keys():
        print('You have already done the ip validation for ' + br_cor + ' so not need further revision')
        break
    else:
        print('The command to validate ips in your local BR-COR is as follows \n')
        print(common_1 + br_cor + common_2 + string + '\n')

