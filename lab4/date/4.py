from datetime import datetime

def difference_in_sec(date1, date2):
    d = date2 - date1
    return d.total_seconds()

date1_str = input("Введите 1 дату в формате (гггг-мм-дд чч:мм:сс): ")
date2_str = input("Введите 2 дату в формате (гггг-мм-дд чч:мм:сс): ")

date1 = datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

difference = difference_in_sec(date1, date2)

print(difference)