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

def salt_extractor(infile):
    
    extract_salt = ""
    with open(infile, 'r', encoding='utf8') as textfile:
        extract_salt = textfile.readline()
        
    byte_salt = b64d(extract_salt)[8:]     # remove Salted__
    hex_salt = hexing(byte_salt)[:16]       # hex_salt size 16
    salt = unhexing(hex_salt)               # return salt type is byte
    
    return salt

def encrypt(key, iv, salt, infile, outfile):
    
    read_text = ""
    with open(infile, 'r', encoding = 'utf8') as textfile:
        for line in textfile:
            read_text += line
    plain_text = text_pad(read_text)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    cipher_text = cipher.encrypt(plain_text)
    salting_cipher = b'Salted__' + unhexing(salt) + cipher_text
    result_text = b64e(salting_cipher).decode()
    
    text_length = len(result_text)
    block_size = math.ceil(text_length/64)
    
    with open(outfile, 'w') as outer:
        for i in range(block_size):
            start = i * 64
            end = (i + 1) * 64
            outer.write(result_text[start:end] + '\n')
            
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
    
def password_checker(arg, min=8, max=16):
    from string import whitespace
    
    passlen = len(arg)
    if(passlen < min or passlen > max):
        raise argparse.ArgumentTypeError("Password length 8 ~ 16")
    for elem in arg:
        if(elem in whitespace):
            raise argparse.ArgumentTypeError("Password Don't use blank")
    
    return arg

def in_datas():
    parser = argparse.ArgumentParser(description = 'Encryption Test')
    parser.add_argument('-E', '--encryption', help = 'Select >> [encrypt / decrypt]', required = True)
    parser.add_argument('-P', '--password', help = 'Password using pbkdf2 (length 8~16)' , required = True, type = password_checker)
    parser.add_argument('-I', '--iterate', help = "Iteration count in pbkdf2 (if iterate < 1000 -> iterate = 1000)", default = 1000, type = int)
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

    if(args.encryption == 'encrypt'):
        salt = secrets.token_bytes(8)   # random 8byte salt 
        
        key, iv = key_iv_generator(md, args.password, iterate, salt)
        
        encrypt(key, iv, hexing(salt), args.infile, args.outfile)
    
    elif(args.encryption == 'decrypt'):
        salt = salt_extractor(args.infile)
        key, iv = key_iv_generator(md, args.password, iterate, salt)
        decrypt(key, iv, args.infile, args.outfile)
    
    elif(args.encryption not in ['encrypt', 'decrypt']):
        print("Encryption Value select \'encrypt\' or \'decrypt\'")
     
if __name__ == '__main__':   
    in_datas()