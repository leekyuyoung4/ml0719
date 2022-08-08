from time import localtime
t = localtime()
print(t)
# time.struct_time(tm_year=2022, tm_mon=8, tm_mday=5, tm_hour=21, tm_min=27, tm_sec=34, tm_wday=4, tm_yday=217, tm_isdst=0)
weeks = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(weeks[t.tm_wday])