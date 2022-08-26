from binascii import unhexlify as unhex
from binascii import hexlify as hex
import hashlib
import passlib

# init datas
_password = 'dnflskfk'
_key = 'key'
_hash_type = 'SHA-512'
_type_512_header = '$6$'

# main sentence
aaa= passlib.hash.sha512_crypt(_password)

print(aaa)