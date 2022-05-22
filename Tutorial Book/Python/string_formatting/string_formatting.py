def debut() -> None:
    group: str = "IZ*ONE"
    debut_year: str = 1029

    #Python version > 3.6 
    print(f'group : {group}, debut_year : {debut_year}')

    #Python versing > 3
    print('group : {}, debut_year : {}'.format(group, debut_year))

    #Pyhton All version
    print('group : %s, debut_year : %i' % (group, debut_year))
    

def math_exam() -> None:
    math_exam: str = "45 / 7 = ?"
    num1, num2 = 45, 7
    
    print(f'{math_exam} -> value = {int(num1/num2)}, remainder = {num1%num2}')
    
    print('{} -> value = {}, remainder = {}'.format(math_exam, int(num1/num2), num1%num2))
    
    print('%s -> value = %i, remainder = %i' % (math_exam, int(num1/num2), num1%num2))

math_exam()