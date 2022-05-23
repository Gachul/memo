import numpy as np

def get_unicode_number(cho_index, jung_index, jong_index):
    return((cho_index * 588) + (jung_index * 28) + (jong_index) + 44032)

def devide_unicode_number(word_unicode):
    
    main_indexing_num = 588 * 28
    
    a = word_unicode - 44032
    b = a - main_indexing_num
    
    return 0

def gen_err_msg(index):
    if index == 1:
        err_msg = '초성 입력이 잘못되었습니다.'
    elif index == 2:
        err_msg = '중성 입력이 잘못되었습니다.'
    else:
        err_msg = '종성 입력이 잘못되었습니다.'
    
    return err_msg

def get_hangeul_index(cho, jung, jong):
    err_session = []
    for session_id in range(1,4):
        try:
            if(session_id == 1):
                cho_index = cho_list.index(cho)
            if(session_id == 2):
                jung_index = jung_list.index(jung)
            if(session_id == 3):
                jong_index = jong_list.index(jong)
        except:
            err_session.append(session_id)
            continue
    
    if err_session:
        err_msg = '\n'
        for i in err_session:
            err_msg += gen_err_msg(i) + '\n'
        raise ValueError(err_msg)
    
    index_list = [cho_index, jung_index, jong_index]
    
    return index_list

def main():
    global cho_list, jung_list, jong_list
    
    cho_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
                'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    jung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ',
                'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

    jong_list = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ',
                'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ',
                'ㅄ','ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    hangul_set = np.array([chr(code) for code in range(44032,55204)])
    hangeul_set = hangul_set.reshape(19,21,28)  # unicode 한글표
    
    ghi = eval('get_hangeul_index')
    gun = eval('get_unicode_number')
    
    handex = ghi('ㄱ', 'ㅑ', 'ㅇ')
    hancode = gun(handex[0], handex[1], handex[2])
    mixing = chr(hancode)
    
    print(mixing)

if __name__ == '__main__':
    main()