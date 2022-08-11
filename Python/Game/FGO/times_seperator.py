import datetime

month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

def year_flow(fyear, cyear):
    
    normal_year_to_days = 365
    
    diff = fyear - cyear
    
    return 0

def month_flow(fmon, cmon):
    # 3, 9
    if(0 == fmon or fmon > 12):
        return 99
    if(0 == cmon or cmon > 12):
        return 99
    
    
    if(fmon == 12):
        static_month = 0
    else:
        static_month = fmon
    
    target_month = cmon
    days_count = 0
    
    # infinite loop stop
    stopper = 0
    
    while 1:
        if(target_month % 12 == static_month):
            return days_count
        else:
            days_count += month[target_month]
            target_month += 1
            stopper += 1

def seperator(current_time, future_time):
    
    cur_material = current_time.split("-")
    future_material = future_time.split("-")
    
    # example
    # cur_material = ["2022", "09", "27"]
    # future_material = ["2023", "03", "19"]
    
    year_gap = year_flow(int(future_material[0]), int(cur_material[0]))
    month_gap = month_flow(int(future_material[1]), int(cur_material[1]))
    
    return None

gg = month_flow(9, 3)

print(gg)