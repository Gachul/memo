# just print function
# return = None
# in java's void function
def test01() -> None:
    print('hello')

# This function is return value is 10
# value = test02()
# is value = test02 function's return value
# value = 10    
def test02() -> int:
    return 10

# This function converts the received values into string types
# And return value's type is string
# test03 is received two values
# a is int type, b is string type
def test03(a: int, b: str) -> str:
    return f'input int value is {a}, string value is {b}'

# Received values are used to plus arithmetic
# So, Return value type is int
def test04(a: int, b: int) -> int:
    return f'{a} + {b} = {a + b}'

# lambda is one-line function
# [value1] if [conditional expression] else [value2]
# => if([conditional expression]): value1
#    else: value2
test05 = lambda a, b, c : b if a > 10 else c

# test06 and test05 are the same
def test06(a: int, b: int, c: int) -> int:
    if(a > 10):
        return b
    else:
        return c

# function in function
def test07(num: int) -> int:
    return lambda addon : addon * num

test01()
val02 = test02(); print(val02)
val03 = test03(10, "choice"); print(val03)
val04 = test04(25, 50); print(val04)
val05 = test05(5,10,15); print(val05)
val06 = test06(5,10,15); print(val06)
# test07(10) -> num is 10
# val07(25) -> addon is 25
val07 = test07(10); print(val07(25))