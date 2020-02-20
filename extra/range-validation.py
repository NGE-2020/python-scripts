def getRange(IPf):
      flag = 1
      lis = []
      ranges = []

      for value in IPf:
          if flag == 1:
              octe = value.split('.')
              fir = octe[0]
              sec = octe[1]
              thi = octe[2]
              lis.append(int(octe[3]))
              flag = 0
          else:
              newocte = value.split('.')
              if newocte[0] != fir:
                  lis.sort()
                  ranges.append(octe[0] + '.' + octe[1] + '.' + octe[2] + '.' +
                      str(lis[0]) + '-' + str(lis[-1]))
                  lis = []
                  octe = value.split('.')
                  fir = newocte[0]
                  sec = newocte[1]
                  thi = newocte[2]
                  lis.append(int(newocte[3]))
                  flag = 1
              else:
                  octe = value.split('.')
                  lis.append(int(octe[3]))

      return(ranges)

def order(IPf):
    orderedIPs = []
    firstocte = []
    for value in IPf:
        octe = value.split('.')
        if octe[0] in firstocte:
            pass
        else:
            firstocte.append(octe[0])
    for x in firstocte:
        for value in IPf:
            octe = value.split('.')
            if octe[0] == x:
                if value in orderedIPs:
                    pass
                else:
                    orderedIPs.append(value)
    return(orderedIPs)

if __name__ == "__main__":

    subnets = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(' ')
            for item in words:
                octets= item.split('.')
                if len(octets)==4:
                    if '/' in item:
                        item = item[:-1]
                        subnets.append(item)
                    else:
                        item = item[:-1]
                        item = item + '/32'
                        subnets.append(item)

    f.close()

    IP = []

    for sub in subnets:
        if '/32' in sub:
            sub = sub[:-3]
            IP.append(sub)
        else:
            sub = sub[:-3]       #First IP from /32 range
            IP.append(sub)
            octets = sub.split('.')
            finoct = int(octets[3])
            finoct += 1
            octets[3]= str(finoct)
            string = '.'.join(octets)      #Second IP from /32 range
            IP.append(string)

    IP = order(IP)
    IP.append('0.0.0.0')
    output = getRange(IP)

    string = '/apollo/env/ISDTools/bin/ipcheck.sh '
    for i in output:
        string += i + ' '

    print (string)

