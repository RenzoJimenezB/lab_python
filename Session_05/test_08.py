"""
Time conversion
"""

from datetime import datetime

"""
timestamp
"""

time_now = datetime.strptime("2024/05/02 20:30:00", "%Y/%m/%d %H:%M:%S")
print(time_now)
print(time_now.timestamp())
