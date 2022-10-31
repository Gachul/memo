from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import hashes

print(backend.openssl_version_text())

hash_d = hashes.SHA256()

print("\thello \roh! my \r\nTommy")

a = backend.create_hmac_ctx(b'password', hash_d)

print(a)

if(1):
    print("1")