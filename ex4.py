def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)

def gen_years(start=2019):
    year = start
    yearend = 2024
    for i in range(start, yearend):
        yield i

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    return days_in_month[month]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def gen_date():
    for year in gen_years():
        for month in gen_months():
            leap_year = is_leap_year(year)
            days = gen_days(month, leap_year)
            for day in range(1, days):
                for time in gen_time():
                    yield f"{day:02d}/{month:02d}/{year} {time}"

def main():
    date_gen = gen_date()
    count = 0
    while True:
        next(date_gen)
        count += 1
        if count % 1000000 == 0:
            print(next(date_gen))

main()
