import crypt, getpass, spwd
import sys, os

_USER=sys.argv[1]
_PASS=sys.argv[2]

def check_pass(username, clr_pass):
    try:
        password = spwd.getspnam(username).sp_pwdp
    except:
        return False

    if password:
        return crypt.crypt(clr_pass, password) == password
    else:
        return 1

if check_pass(_USER, _PASS):
   print("Success", end="", sep="")
else:
   print("Fail", end="", sep="")
