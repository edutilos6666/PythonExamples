import time
import calendar
import arrow
import datetime


def example9():
    'datetime, date, time'
    dt = datetime.datetime(2010, 10, 10, 20, 30, 40)
    d = datetime.date(2010, 10, 10)
    t = datetime.time(10, 20, 30)
    print("dt = ", dt)
    print("d = ", d)
    print("t = ", t)
    year, month , day , hour , minute , second = dt.year, dt.month , dt.day, dt.hour, dt.minute, dt.second
    pattern = "{0}/{1}/{2} Time: {3}:{4}:{5}"
    print(pattern.format(year, month , day, hour , minute, second))
    print()





def example8():
    'arrow'
    utc = arrow.utcnow()
    utc = utc.shift(hours=-1)
    local = utc.to('US/Pacific')
    print("local.format() = ", local.format())
    print("local.timestamp = ", local.timestamp)
    pattern = "YYYY-MM-DD HH:mm:ss ZZ"
    print("local.format(pattern) = ", local.format(pattern))
    print("local.humanize() = ", local.humanize())
    print()
    t2 = arrow.get(2010 , 10, 10)
    t3 = arrow.get(2010, 10, 10, 20, 30, 40)
    print("t2 = " , t2.format())
    print("t3 = ", t3.format())

    t2 = arrow.Arrow(2010, 10, 10)
    t3 = arrow.Arrow(2010, 10, 10, 20, 30, 40)
    t2 = arrow.Arrow(2010, 10, 10, 20, 30, 40)
    print("t2 = ", t2.format())
    print("t3 = ", t3.format())
    d = t2.date()
    t = t2.time()
    dt = t2.datetime
    print("d = ", d)
    print("t = ", t)
    print("dt = ", dt)

    year, month , day, hour , minute , second ,  = t2.year, t2.month , t2.day , t2.hour , t2.minute , t2.second
    print("year = ", year)
    print("month = ", month)
    print("day = ", day)
    print("hour = ", hour)
    print("minute = ", minute)
    print("second = ", second)
    print()



def example7():
    res = calendar.month(2010, 10)
    print(res)
    res = calendar.calendar(2010)
    print(res)
    print()

def example6():
    'time.sleep(seconds)'
    print("Hello")
    # time.sleep(1)
    print("World")

def example5():
    'time.strftime(pattern , struct)'
    t = time.gmtime(time.time())
    pattern = "%Y-%m-%d Time: %H:%M:%S"
    res = time.strftime(pattern, t)
    print("time = ", res)

def example4():
    'time.mktime(tuple)'
    year = 2017
    month = 9
    mday = 11
    hour = 16
    minute = 30
    second = 23
    wday = 0
    yday = 254
    isdst = 0
    time_tuple = (year, month, mday, hour , minute, second, wday, yday , isdst)
    ticks = time.mktime(time_tuple)
    print("ticks = ", ticks)
    print("asctime = ", time.asctime(time.localtime(ticks)))
    print()


def example3():
    'time.gmtime(ticks)'
    ticks = time.time()
    gmtime = time.gmtime(ticks)
    print("gmtime = ", gmtime)
    year = gmtime.tm_year
    month = gmtime.tm_mon
    mday = gmtime.tm_mday
    wday = gmtime.tm_wday
    yday = gmtime.tm_yday
    hour = gmtime.tm_hour
    minute = gmtime.tm_min
    second = gmtime.tm_sec
    isdst = gmtime.tm_isdst
    print("year = ", year)
    print("month = ", month)
    print("mday = ", mday)
    print("yday = ", yday)
    print("wday = ", wday)
    print("hour = ", hour)
    print("minute = ", minute)
    print("second = ", second)
    print("isdst = ", isdst)
    print("%d/%d/%d Time: %d:%d:%d" %(year, month , mday, hour,minute, second))
    print()



def example2():
    'time.asctime(tuple)'
    ticks = time.time()
    localtime = time.localtime(ticks)
    asctime = time.asctime(localtime)
    print("asctime = ", asctime)
    print()

def example1():
    'time.localtime(ticks)'
    ticks = time.time()
    localtime = time.localtime(ticks)
    print("localime = ", localtime)
    year = localtime.tm_year
    month = localtime.tm_mon
    mday = localtime.tm_mday
    hour = localtime.tm_hour
    minute = localtime.tm_min
    second = localtime.tm_sec
    wday = localtime.tm_wday
    yday = localtime.tm_yday
    isdst = localtime.tm_isdst
    print("year = %d" % (year))
    print("month = ", month)
    print("mday = ", mday)
    print("wday = ", wday)
    print("yday = ", yday)
    print("hour = ", hour)
    print("minute = ", minute)
    print("second = ", second)
    print("isdst = ", isdst)
    pattern = "{0}/{1}/{2} {3}:{4}:{5}"
    print(pattern.format(year, month , mday,hour, minute, second))
    print()
