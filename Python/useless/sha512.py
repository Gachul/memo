from binascii import unhexlify as unhex
from binascii import hexlify as hex
from passlib.hash import sha512_crypt as sh512

# init datas
_password = 'dnflskfk'
_key = 'key'
_hash_type = 'SHA-512'
_type_512_header = '$6$'

# main sentence
aaa = sh512.hash(_password)

# $6$rounds$salt$hash
bbb = sh512.using(rounds=1500, salt ='salt').hash(_password)

# if rounds=5000 >> $6$salt$hash
ccc = sh512.using(rounds=5000, salt = 'salt').hash(_password)

print(aaa)
print(bbb)
print(ccc)