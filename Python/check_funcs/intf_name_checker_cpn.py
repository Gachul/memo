#import argparse as arp
import os, sys

_MODE = sys.argv[1]
_INTERFACE_NAME = sys.argv[2]

def normal_interface(intf):
    if(intf[0:3] != "eth"):
        if(intf == "bond0"):
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
        if(intf[4] == ":"):
            interface_number = int(intf[3])
            if(interface_number > 20):
                return 0

            interface_mask = int(intf[5:])

            inter_mask = str(interface_mask)
            check_mask = intf[5:]
            
            if(inter_mask != check_mask ):
                return 0
            if(interface_mask > 255):
                return 0
            
        elif(intf[5] == ":"):
            interface_number = int(intf[3:5])
            if(interface_number > 20):
                return 0

            interface_mask = int(intf[6:])

            inter_mask = str(interface_mask)
            check_mask = intf[6:]
            
            if(inter_mask != check_mask ):
                return 0
            if(interface_mask > 255):
                return 0
            
        else:
            return 0

        return 1
    except:
        return 0

def vlan_interface(intf):
    if(intf[0:3] != "eth"):
        return 0
    try:
        if(intf[4] == "."):
            interface_number = int(intf[3])
            if(interface_number > 20):
                return 0

            interface_mask = int(intf[5:])

            inter_mask = str(interface_mask)
            check_mask = intf[5:]
            
            if(inter_mask != check_mask ):
                return 0
            if(interface_mask > 255):
                return 0
            
        elif(intf[5] == "."):
            interface_number = int(intf[3:5])
            if(interface_number > 20):
                return 0

            interface_mask = int(intf[6:])

            inter_mask = str(interface_mask)
            check_mask = intf[6:]
            
            if(inter_mask != check_mask ):
                return 0
            if(interface_mask > 255):
                return 0
            
        else:
            return 0

        return 1
    except:
        return 0

def bonding_interface(intf):
    if(intf != "bond0"):
        return 0
    
    return 1

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

mode_checker(_MODE, _INTERFACE_NAME)