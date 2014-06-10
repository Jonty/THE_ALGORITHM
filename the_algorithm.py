#!/usr/bin/python
import calendar
import datetime

def get_middle_thursday(year, month):
    startday, numdays = calendar.monthrange(year, month)
    middle_of_month = numdays / 2
    middleday = 0
    distance = 30

    for day in range(1, numdays + 1):
        weekday = calendar.weekday(year, month, day)
        day_distance = abs(middle_of_month - day)
        if weekday == 3 and day_distance < distance:
            middleday = day
            distance = day_distance

    return middleday

def gen_ps_dates(start):
    while True:
        day = get_middle_thursday(start.year, start.month)
        if day > start.day:
            yield datetime.date(year=start.year, month=start.month, day=day)

        start = datetime.date(year=start.year, month=start.month, day=1) + datetime.timedelta(days=31)

if __name__ == '__main__':
    start = datetime.date.today()
    generator = gen_ps_dates(start)
    for _ in range(0,10):
        print generator.next()
