import sys, os

_VALID = 0
_TYPE_CHECK = sys.argv[1]
_TYPE = "Error"
_ORG_INTERFACE = sys.argv[2]

def ipv4(ip, subnet):
    try:
        ip_devide = ip.split('.')
        
        if(len(ip_devide) != 4):
            return 0
        else:
            for part_ip in ip_devide:
                chking = int(part_ip)
                
                if(chking < 0 or chking > 255):
                    return 0
    except:
        return 0
    return 1

def ipv6(ip, prefix):
    
    return 0

def devider(all_ip):
    ip_box = all_ip.split('/')
         
    return ip_box[0], ip_box[1]

ip_addr, subnet = devider(_ORG_INTERFACE)

if(_TYPE_CHECK == "Y"):
    _TYPE = "ipv4"
    ip_addr, subnet = devider(_ORG_INTERFACE)
    _VALID = ipv4(ip_addr, subnet)

elif(_TYPE_CHECK == "N"):
    _TYPE = "ipv6"
    ip_addr, prefix = devider(_ORG_INTERFACE)
    _VALID = ipv6(ip_addr, prefix)

if(_VALID == 1):
    os.system("echo 01")
    print("{} 는 {} 형식입니다.".format(_ORG_INTERFACE, _TYPE))
elif(_VALID == 0):
    os.system("echo 00")
    print("{} 는 {} 형식이 아닙니다.".format(_ORG_INTERFACE, _TYPE))