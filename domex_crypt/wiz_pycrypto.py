from binascii import hexlify as hexing
from binascii import unhexlify as unhexing
import secrets, math, argparse, hashlib
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Cryptodome.Cipher import AES

# plaintext에 패딩을 더해서 text+padding화 함
def text_pad(textline):

    hex_text = hexing(textline.encode()).decode()   # plaintext의 data를 hex data로 변환
    pad_size = 16 - (len(textline) % 16)            # plaintext의 길이를 16byte의 배수로 설정하기 위해 padding의 크기 조정
    pad_value = str(hex(pad_size))[2:]              # padding값
    if(pad_size != 16):
        pad_value = "0" + pad_value
    
    padding = "{}".format(pad_value * pad_size)
    
    change_text = hex_text + padding        # plaintext에 padding 추가
    
    return_string = unhexing(change_text.encode())  # plaintext의 hex data를 data로 변환
    
    return return_string    # byte type

# text+padding을 plaintext로 변환
def remove_text_pad(hex_text):
    
    pad_list = ["01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10"]
       
    text_size = len(hex_text)
    with_pad_block_size = int(text_size / 32)
    
    change_block_start = 32 * (with_pad_block_size - 1)
    change_block_end = text_size
    
    change_block = hex_text[change_block_start:change_block_end]    # 마지막 32bit사이즈의 padding+text에서 plaintext만 추출
    
    real_count = 0
    true_target = ""
    no_pad_block = ""
    
    for i in range(16):
        count = i * 2
        target = change_block[count:count+2]
        
        if(target not in pad_list):
            real_count = count
            true_target = target
            
    if(true_target != ""):
        no_pad_block = change_block[0:real_count + 2]

    real = hex_text[:change_block_start] + no_pad_block
    
    # text is hex data, type is byte
    # text is multiple of 32  ==>  plain_text(with padding) size is multiple of 16
    
    real_text_byte = unhexing(real.encode()).decode()
    
    return real_text_byte

def salt_extractor(infile):
    
    extract_salt = ""
    with open(infile, 'r', encoding='utf8') as textfile:
        extract_salt = textfile.readline()
        
    byte_salt = b64d(extract_salt)[8:]     # remove Salted__
    
    hex_salt = hexing(byte_salt)[:16]       # hex_salt size 16
    
    salt = unhexing(hex_salt)               # return salt type is byte
    
    return salt

def encrypt(key, iv, salt, infile, outfile):
    
    is_salt = b'53616c7465645f5f'
    salting = is_salt + salt
    
    read_text = ""
    with open(infile, 'r', encoding = 'utf8') as textfile:
        for line in textfile:
            read_text += line
    plain_text = text_pad(read_text)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    cipher_text = cipher.encrypt(plain_text)
    salting_cipher = salting + hexing(cipher_text)
    encode_text = unhexing(salting_cipher)
    result_text = b64e(encode_text).decode()
    
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
    
    padding_with_hex = hexing(dec_text).decode()
    real_text = remove_text_pad(padding_with_hex)
    
    textext = (real_text.split('\r'))   # openssl에서의 암호문 처리 부분
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
    re_iv = pbkdf2_key[32:]     # iv값은 salt와 password로 부터 도출할 수 있도록 설정
    
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