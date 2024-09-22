"""Datetime"""

from datetime import datetime, date

date_1 = date.today()
print(date_1)

time_1 = datetime.now()
print(time_1)

year = time_1.year
month = time_1.month
day = time_1.day

print(f"year: {year}, month: {month}, day: {day}")

"""Datetime. Get time (hours, minutes, seconds)"""
hour = time_1.hour
minute = time_1.minute
second = time_1.second

print(f"hour: {hour}, minutes: {minute}, seconds: {second}")
