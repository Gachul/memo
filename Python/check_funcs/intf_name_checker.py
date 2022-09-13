#import argparse as arp
import os, sys

_MODE = sys.argv[1]
_INTERFACE_NAME = sys.argv[2]

def normal_interface(intf):
    if(intf[0:3] != "eth"):
        if(intf[:5] == "bond0"):
            return 1
        return 0
    try:
        interface_number = int(intf[3:])    # check interface number is valid

        inter_number = str(interface_number)
        check_number = intf[3:]

        if(inter_number != check_number):
            return 0

        if(interface_number > 20):
            return 0
        return 1
    except:
        return 0

def alias_interface(intf):
    if(intf[0:3] != "eth"):
        return 0
    try:
        interface_number = int(intf[3])
        if(interface_number > 20):
            return 0

        if(intf[4] != ":"):
            return 0

        interface_mask = int(intf[5:])

        inter_mask = str(interface_mask)
        check_mask = intf[5:]
        if(inter_mask != check_mask ):
            return 0
        if(interface_mask > 255):
            return 0

        return 1
    except:
        return 0

def vlan_interface(intf):
    if(intf[0:3] != "eth"):
        return 0
    try:
        interface_number = int(intf[3])
        if(interface_number > 20):
            return 0

        if(intf[4] != "."):
            return 0

        interface_mask = int(intf[5:])

        inter_mask = str(interface_mask)
        check_mask = intf[5:]

        if(inter_mask != check_mask ):
            return 0
        if(interface_mask > 255):
            return 0

        return 1

    except:
        return 0

def bonding_interface(intf):
    if(intf[:5] != "bond0"):
        return 0
    try:
        interface_number = int(intf[4:])

        inter_number = str(interface_number)
        check_number = intf[4:]

        if(inter_number != check_number):
            return 0

        if(interface_number > 5):
            return 0

        return 1

    except:
        return 0

def bridge_interface(intf):
    if(intf != "br0"):
        return 0

    return 1

def mode_checker(mode, interface):
    if (mode == "address" or mode == "address6"):
        valid = normal_interface(interface)

    elif (mode == "alias"):
        valid = alias_interface(interface)

    elif (mode == "vlan"):
        valid = vlan_interface(interface)

    elif (mode == "bonding"):
        valid = bonding_interface(interface)

    elif (mode == "bridge"):
        valid = bridge_interface(interface)

    if(valid == 1):
        os.system("echo 1")
    else:
        os.system("echo 0")
print(_MODE)
print(_INTERFACE_NAME)
mode_checker(_MODE, _INTERFACE_NAME)
        
