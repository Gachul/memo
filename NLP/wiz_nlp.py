def endp():
    print("="*100, end = '\n\n')
    
def count(instance, word):
        count = 0
        searching_width = len(word)
        instance_size = len(instance) + 1
        for idx in range(instance_size - searching_width):
            if(instance[idx:idx+searching_width] == word):
                count += 1
        return count

def main():
      
    # Numbering
    with open('./use_file/izone.txt', 'r', encoding='utf-8') as text:
        for line_num, line in enumerate(text):
            print("{}. {}".format(line_num, line.strip()))
    endp()
            
    # Replace
    with open('./use_file/izone.txt', 'r', encoding='utf-8') as text:
        for line in text:
            textline = line.replace('위즈원', '팬들')
            print(textline.rstrip())
    endp()
            
    # Find
    with open('./use_file/izone.txt', 'r', encoding='utf-8') as text:
        hide = '아이즈원'
        hide_and_seek = 0
        for line in text:
            hide_and_seek += line.count(hide)
            print(line.rstrip())
        print("{}이 쓰인 횟수 : {}".format(hide, hide_and_seek))
    endp()
    
    with open('./use_file/izone.txt', 'r', encoding='utf-8') as text:
        word = '원'
        for line in text:
            custom_count_result = count(line.strip(), word)
            basic_count_result = line.strip().count(word)
            print(line.strip())
            print('custom count method result \'{}\' : {}'.format(word, custom_count_result))
            print('basic count method result \'{}\' : {}'.format(word, basic_count_result))
        


if __name__ == "__main__":
    
    main()