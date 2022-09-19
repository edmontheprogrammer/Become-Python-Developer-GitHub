# Formatting Dates and Times: Days
# %a -- abbreviated day of the week: Mon, Tues and Wed
# %A -- full name of the day of the week: Monday, Tuesday, Wednesday
# %d -- day of month: number 10 for the 10th of January

# Formatting Dates and Times: Months
# %d -- abbreviated month name: Jan, Feb
# %B -- full month name: January

# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%A %B %d"))


# Formatting Dates and Times: Times
# %H - hours
# %M - minutes
# %S - seconds
# %p - a.m or p.m

print(now.strftime("%H : %M : %S %p"))


# Formatting Dates and Times: Years
# %y -- abbreviated year as two numbers
# %Y -- year as four numbers: 2022

print(now.strftime("%y %Y"))
