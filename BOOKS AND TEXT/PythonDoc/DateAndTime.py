"""
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.
"""
from datetime import date
now = date.today()
print(now)
# %m - represents number of month
# %d - represents day number of the month
# %y - represents year number
# %B - represents full text of the month
#%A - represents full text of the Day
#%a - represents short text of the Day
dateNow = now.strftime('"%m-%d-%y. %d %B %Y is a %a on the %d day of %B."')
print(dateNow)

birthday = date(2000,8,1)
age = now - birthday
print(age.days)