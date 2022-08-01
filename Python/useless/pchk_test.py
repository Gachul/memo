import pwcheck
import random, string


allover = string.printable

for i in range(500):
    my_pwd = ""
    for i in range(18):
        rand_int = random.randint(0,94)
        my_pwd = my_pwd + allover[rand_int]

    result = pwcheck.test(my_pwd)
    
    if(result == 3 or result == 4):
        print(result)
        print(my_pwd)
