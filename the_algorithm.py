#!/usr/bin/python
import calendar
import datetime
from dateutil.relativedelta import relativedelta

FIRST_PUBSTANDARDS = datetime.date(year=2005, month=12, day=14)

def calc_middle_thursday(year, month):
    _, numdays = calendar.monthrange(year, month)
    middle_of_month = numdays / 2
    date = datetime.date(year, month, middle_of_month)
    return middle_of_month - (date.weekday() - 3)


def gen_ps_dates(start=None):
    if start == None:
        start = FIRST_PUBSTANDARDS

    while True:
        day = calc_middle_thursday(start.year, start.month)
        if day >= start.day:
            date = datetime.datetime(
                        year=start.year, 
                        month=start.month, 
                        day=day, 
                        hour=18, 
                        minute=0, 
                        second=0)
            yield date

        start = datetime.datetime(
                    year=start.year, 
                    month=start.month, 
                    day=1, 
                    hour=18, 
                    minute=0, 
                    second=0) + datetime.timedelta(days=31)


def ps_offset_from_date(date):
    return (date.year - FIRST_PUBSTANDARDS.year) * 12 + date.month - FIRST_PUBSTANDARDS.month + 1


def ps_date_from_offset(integer):
    offset = FIRST_PUBSTANDARDS + relativedelta(months=integer-1)
    day = calc_middle_thursday(offset.year, offset.month)
    date = datetime.date(year=offset.year, month=offset.month, day=day)
    return date


def next_ps_date():
    now = datetime.date.today() 
    return gen_ps_dates(start=now).next()


if __name__ == '__main__':
    generator = gen_ps_dates(start=FIRST_PUBSTANDARDS)
    for i in range(0,300):
        print generator.next()
