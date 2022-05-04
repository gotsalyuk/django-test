import datetime


def calculate_week_number(input_date: str) -> int:
    try:
        date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
    except:
        return None

    
    week_number = date.isocalendar()[1]
    day_of_week = datetime.datetime.weekday(date)
    
    
    if date.year in [2021, 2027, 2038, 2044, 2049, 2055, 2066, 2072, 2077, 2083, 2094, 2100]:
        if date.month == 1:
            if date.day in [1,2]:
                return 1
            elif date.day in [3,4,5,6,7,8,9]:
                return 2
            else:
                week_number += 1
        else:
            week_number +=1
    
    elif date.year in [2022, 2028, 2033, 2039, 2050, 2056, 2061, 2067, 2078, 2084, 2089, 2095]:
        if date.month == 1:
            if date.day == 1:
                return 1
            elif date.day in [2,3,4,5,6,7,8]:
                return 2
            else:
                week_number += 1
        else:
            week_number +=1

    
    elif day_of_week == 6 and date.month == 1 and date.day == 1:
        return 1


    if day_of_week == 6:
        week_number += 1


    return week_number


