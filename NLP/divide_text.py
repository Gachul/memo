target_string = []

with open('./use_file/wtext.txt', 'r', encoding='utf-8') as wtx:
    for line in wtx:
        target_string.append(line.strip('.\n').split(' '))
        
for target in target_string[0][0]:
    print(target)
    
error_status = -1
while error_status != 1:
    for i in range(0,200):
        try:
            print(i)
            if(i == 53):
                print("i" * "i")
        except:
            error_status = 1
            break

print('apple')