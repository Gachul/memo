
#import pymysql
import sys
import os

#db = pymysql.connect(host = "localhost", port = 3306, user = "entro", passwd = "dnflskfk_ppx_2000", db = "radius")
#cur = db.cursor()

linear_pw = ["01234567890", "9876543210" "qwertyuiop", "QWERTYUIOP", "asdfghjkl", "ASDFGHJKL", "zxcvbnm", "ZXCVBNM", "POIUYTREWQ", "poiuytrewq", "lkjhgfdsa", "LKJHGFDSA", "mnbvcxz", "MNBVCXZ" "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "zyxwvutsrqponmlkjihgfedcba", 
"ZYXWVUTSRQPONMLKJIHGFEDCBA"] # pw

# def passToDB(passwd):
#     latest_pw = "entrolink"
#     dummy_pw = latest_pw
    
#     isUse_sql = "select * from pwcheck"
#     try:
#         cur.execute(isUse_sql)
#         rows = cur.fetchall()
#         a = rows[0]
#         # checking any space exist in rows
#         # rows[0] = null >> error
        
#         for row in rows:
#             latest_pw = row[0]
#     except:
#         insert_sql = "insert into pwcheck(pw) values(%s)"
#         cur.execute(insert_sql, (passwd))
    
#     if(passwd == latest_pw):
#         return 0
#     if(latest_pw != dummy_pw):
#         update_sql = "update pwcheck set pw = %s where pw = %s"
#         cur.execute(update_sql,(passwd, latest_pw))    
    # db.commit()
    # return 1

def isLinear(passwd, select_num = 0):
    for h in range(len(linear_pw)):
        select_linear = linear_pw[select_num]
        for i in range(len(passwd)-2):
            pass_section = passwd[i:i+3]
            
            for j in range(len(select_linear)-2):
                if(pass_section == select_linear[j:j+3]):
                    return 0
        select_num += 1
    return 1  

def passAscii(pw):
    pw_to_ascii = []
    for i in range(len(pw)):
        pw_to_ascii.append(ord(pw[i]))
    return pw_to_ascii

def passAllhave(passwd):
    p_list = passAscii(passwd)
    have_upper = 0
    have_lower = 0
    have_digit = 0
    have_func = 0
    for p_cell in p_list:
        if(65 <= p_cell < 91):
            have_upper += 1
        elif(97 <= p_cell < 123):
            have_lower += 1
        elif(33 <= p_cell < 48 or 58 <= p_cell < 65 or 91 <= p_cell < 97 or 123 <= p_cell < 127):
            have_func += 1
        elif(48 <= p_cell < 58):
            have_digit += 1
            
    if(have_upper == 0 or have_lower == 0 or have_func == 0 or have_digit == 0):
        return 0
        
def isIterate(passwd):
    p_list = passAscii(passwd)
    for i in range(len(p_list)-2):
        if(p_list[i] == p_list[i+1] and p_list[i+1] == p_list[i+2]):
            return 0
    return 1

def check(pw, check_key = 12):
    if(len(pw) < 9):
        return 2
    if(isLinear(pw) == 0):
        return 3
    if(isIterate(pw) == 0):
        return 4
    if(passAllhave(pw) == 0):
        return 5
    
    return 1

input_pwd = sys.argv[1]

isSuccess = check(input_pwd)
if(isSuccess == 1):
    os.system("echo 1")
else:
    os.system("echo 0")
