import calendar

# prints week header. number stands for how many letters will be pritned
print(calendar.weekheader(3))
print("")

# tells what the first weekday is numerically (monday is 0, tuesday 1, etc)
print(calendar.firstweekday())
print("")

# prints full month based on year and month parameters (2020 = year, 3 = month)
print(calendar.month(2020, 3))

# prints calendar in matrix form ([0,0,0,0,0,0,1], [2,3,4,5,6,7,8], etc)
print(calendar.monthcalendar(2020, 3))

# print entire calendar
print(calendar.calendar(2020))

# prints out int of weekday
day_of_week = calendar.weekday(2020, 3, 10)
print(day_of_week)

# checks if the year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)

# prints how many leap days in the range given (exclusive)
how_many_leap_days = calendar.leapdays(2000,2021)
print(how_many_leap_days)