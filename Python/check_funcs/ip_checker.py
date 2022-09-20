import sys, os
import string

_IPV6_SET = string.digits + 'abcdef'

_VALID = 0
_TYPE_CHECK = sys.argv[1]
_TYPE = "Error"
_ORG_INTERFACE = sys.argv[2]

def ipv4(ip, subnet):
    try:
        if(int(subnet) > 32):
            return 0
        
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
    
    try:
        if(int(prefix) > 128):
            return 0
        
        ip_devide = ip.split(':')
        
        if(len(ip_devide) != 8):
            return 0
        else:
            for part_ip in ip_devide:
                
                for part in part_ip:
                    if(part not in _IPV6_SET):
                        return 0
    except:
        return 0
    
    return 1

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