import numpy as np

def get_unicode_number(cho_index, jung_index, jong_index):
    return((cho_index * 588) + (jung_index * 28) + (jong_index) + 44032)

def gen_err_msg(index):
    if index == 1:
        err_msg = '초성 입력이 잘못되었습니다.'
    elif index == 2:
        err_msg = '중성 입력이 잘못되었습니다.'
    else:
        err_msg = '종성 입력이 잘못되었습니다.'
    
    return err_msg

def get_hangeul_index(cho, jung, jong):
    return 0

def main():
    divide_dict = {}
    
    divide_dict['book'] = 'box'
    
    hangul_set = np.array([chr(code) for code in range(44032,55204)])
    hangeul_set = hangul_set.reshape(19,21,28)
    
    print(hangeul_set)
    
    with open('./use_file/tokens.txt', 'r', encoding='utf-8') as text:
        for line_num, line in enumerate(text):
            elem = line.strip('\n').split(', ')
            divide_dict[line_num] = elem
            
    print(divide_dict)
    
    
    if 'book1' in divide_dict.keys():
        print('yes')

if __name__ == '__main__':
    main()