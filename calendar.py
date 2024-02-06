import calendar
month, day, year = list(map(int,input('enter a mm dd yyy').split()))
ans = calendar.weekday(year, month, day)
print((calendar.day_name[ans]).upper())