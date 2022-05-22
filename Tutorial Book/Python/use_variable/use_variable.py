# 기본 변수 설정
hello = "world"
print(hello)    # world

# 사전 이용
variable_dict = {}
variable_dict['world'] = 'hello'
print(variable_dict['world'])       # hello

# 지역변수 조작 (추천하지 않음)
# 이미 존재하는 변수를 조작할 우려가 있기 때문
# -> 언제나 시스템을 직접 조작하는 일은 권유되지 않음
# 굳이 사용한다면, 대문자와 밑줄을 사용하여 고정변수로 생성하는 것을 권함
locals()['_FGO'] = 'Fate Grand Order'
print(_FGO)


# 지역변수 조회
print(locals())

# 전역변수 조회
print(globals())