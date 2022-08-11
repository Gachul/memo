import errmsg

def weeks_getting_stone(start_date, end_date = 0, day_catcher = 0):
    
    days_achieve = {2 : 'stone', 4 : 'stone', 6 : 'stone'}    
    weeks_achieve = {'stone' : 0, 'hobu' : 0}
    getting_what = 0
    
    if(end_date == 0):
        day_catcher = 730   # 종료일 미정시 시작 기간으로부터 2년을 산정
    else:
        day_catcher = end_date - start_date
        
    if(day_catcher < 0):
        return errmsg.err_msg(1)
    
    count_weeks = day_catcher // 7
    remain_days = day_catcher % 7
    
    weeks_achieve['stone'] = count_weeks * 4
    weeks_achieve['hobu'] = count_weeks
    
    if(remain_days == 2):
        weeks_achieve['stone'] += 1
    elif(remain_days == 4):
        weeks_achieve['stone'] += 2
    elif(remain_days == 6):
        weeks_achieve['stone'] += 4
    
    return weeks_achieve

future_stone = weeks_getting_stone(100, 0)
print(future_stone)