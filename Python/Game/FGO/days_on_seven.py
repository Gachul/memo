import datetime
import errmsg

class wiz_day():
    
    def __init__(self, in_year):
        self.year = in_year
        
    def max_days_month(self):
        self.january = 31
        self.february = 28
        self.march = 31
        self.april = 30
        self.may = 31
        self.june = 30
        self.july= 31
        self.august = 31
        self.september = 30
        self.october = 31
        self.november = 30
        self.december = 31
        
    def leap_year(self):
        self.february = 29

def specially_year(year):
    
    is_special = None
    
    if(year // 4 == 0):
        is_special = "yes"
    else:
        is_special = "no"
    
    return year


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
    
    weeks_achieve['stone'] = count_weeks * 3
    weeks_achieve['hobu'] = count_weeks
    
    if(remain_days in days_achieve.keys()):
        getting_what = days_achieve[remain_days]
    
    if(getting_what != 0):
        weeks_achieve[getting_what] += 1
    
    return weeks_achieve

future_stone = weeks_getting_stone(100, 0)

print(future_stone)