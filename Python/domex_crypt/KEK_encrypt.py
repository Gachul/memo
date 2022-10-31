from binascii import hexlify as hexing
from binascii import unhexlify as unhexing
import secrets, math, argparse, hashlib
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Cryptodome.Cipher import AES

def text_pad(textline):
    
    pad_size = 16 - (len(textline) % 16)
    pad_value = format(pad_size, '02x')
    
    padding = format(pad_value * pad_size)
    
    return_pad = textline.encode() + unhexing(padding.encode())
    
    return return_pad    # byte type

def remove_text_pad(textline):
    
    chk_pad = textline[-1] * (-1)
    
    return textline[:chk_pad].decode()

def encrypt(key, iv, infile):
    
    read_text = ""
    with open(infile, 'r', encoding = 'utf8') as textfile:
        for line in textfile:
            read_text += line
    plain_text = text_pad(read_text)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    cipher_text = cipher.encrypt(plain_text)
    result_text = b64e(cipher_text).decode()
    
    return result_text
            
def decrypt(key, iv, infile, outfile):
    
    read_text = ""
    with open(infile, 'r') as crypto_file:
        for line in crypto_file:
            read_text += line.rstrip('\n')
            
    texture = (b64d(read_text.encode()))[8:]   # remove Salted__
    hexing_texture = hexing(texture)[16:]      # remove salt
    cipher_text = unhexing(hexing_texture)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec_text = cipher.decrypt(cipher_text)
    
    real_text = remove_text_pad(dec_text)

    textext = (real_text.split('\r'))   # openssl
    out_text = ""
    for part in textext:
        out_text += part 
    
    with open(outfile, 'w', encoding='utf8') as outer:
        outer.write(out_text)
    outer.close()
    
def key_iv_generator(in_dgst_type, in_pwd, in_iter, salt):
        
    material_pass = in_pwd.encode()
    
    pbkdf2_key = hashlib.pbkdf2_hmac(in_dgst_type, material_pass, salt, in_iter, dklen = 48)
    
    re_key = pbkdf2_key[:32]
    re_iv = pbkdf2_key[32:]
    
    return re_key, re_iv
    
def in_datas():
    parser = argparse.ArgumentParser(description = 'Encryption Test')
    parser.add_argument('-E', '--encryption', help = 'Select >> [ e: encrypt / d: decrypt]', required = True)
    parser.add_argument('-P', '--password', help = 'Password using pbkdf2 (length 8~16)' , required = True)
    parser.add_argument('-I', '--iterate', help = "Iteration count in pbkdf2", default = 1000, type = int)
    parser.add_argument('-IF', '--infile', help = "Input File Path/filename", required = True)
    parser.add_argument('-OF', '--outfile', help = "Output File Path/filename", required = True)
    parser.add_argument('-MD', '--mdigest', help = "Message Digest [sha256, sha384, sha512 / invalid digest type -> sha256]", default = "sha256")
    
    args = parser.parse_args()
    
    md = args.mdigest
    iterate = args.iterate
    passwd = args.password
    
    ## Minimum Specifications ##
    if(len(passwd) < 8):
        passwd = "password"
    if(iterate < 1000):
        iterate = 1000
    if(md not in ['sha256', 'sha384', 'sha512']):
        md = 'sha256'
    ##############################

    if(args.encryption == 'e'):
        salt = secrets.token_bytes(8)   # random 8byte salt 
        
        key, iv = key_iv_generator(md, args.password, iterate, salt)
        
        encrypt(key, iv, hexing(salt), args.infile, args.outfile)
    
    elif(args.encryption == 'd'):
        in_salt = input('Input Your Salt : ')
        salt = in_salt.encode()
        key, iv = key_iv_generator(md, args.password, iterate, salt)
        decrypt(key, iv, args.infile, args.outfile)
    
    elif(args.encryption not in ['encrypt', 'decrypt']):
        print("Encryption Value select \'encrypt\' or \'decrypt\'")
     
if __name__ == '__main__':
    salt = secrets.token_bytes(16)
    print(salt)
    print(hexing(salt))
    #in_datas()
