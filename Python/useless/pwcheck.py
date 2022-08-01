import sys
import os, string


linear_pw = ["01234567890", "9876543210", "qwertyuiop", "QWERTYUIOP", "asdfghjkl", "ASDFGHJKL", "zxcvbnm", "ZXCVBNM", "POIUYTREWQ", "poiuytrewq", "lkjhgfdsa", "LKJHGFDSA", "mnbvcxz", "MNBVCXZ", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "zyxwvutsrqponmlkjihgfedcba", 
"ZYXWVUTSRQPONMLKJIHGFEDCBA"] # pw

print(len(linear_pw))

def isLinear(passwd):
    for h in range(len(linear_pw)):
        select_linear = linear_pw[h]
        for i in range(len(passwd)-2):
            pass_section = passwd[i:i+3]
            
            for j in range(len(select_linear)-2):
                if(pass_section == select_linear[j:j+3]):
                    return 0
    return 1  

def passAllhave(passwd):
    have_upper = 0
    have_lower = 0
    have_digit = 0
    have_func = 0
    
    for piece in passwd:
        if(piece in string.ascii_uppercase):
            have_upper += 1
        elif(piece in string.ascii_lowercase):
            have_lower += 1
        elif(piece in string.digits):
            have_digit += 1
        elif(piece in string.punctuation):
            have_func += 1
            
    if(have_upper == 0 or have_lower == 0 or have_func == 0 or have_digit == 0):
        return 0
        
def isIterate(passwd):
    for i in range(len(passwd)-2):
        if(passwd[i] == passwd[i+1] and passwd[i+1] == passwd[i+2]):
            return 0
    return 1

def check(pw):
    if(len(pw) < 9 or len(pw) > 32):
        return 2
    if(isLinear(pw) == 0):
        return 3
    if(isIterate(pw) == 0):
        return 4
    if(passAllhave(pw) == 0):
        return 5
    
    return 1

#input_pwd = sys.argv[1]

def test(input_pwd):
    isSuccess = check(input_pwd)
    if(isSuccess == 1):
        None
    else:
        print(input_pwd)
        os.system("echo 0")
