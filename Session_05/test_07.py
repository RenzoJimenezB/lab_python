"""
Convert dates
"""

import datetime

date_1 = datetime.datetime(2024, 4, 23)
date_2 = datetime.datetime(2024, 4, 20)

if date_1 == date_2:
    print("Born the same day")
elif date_1 > date_2:
    print("Boy 2 is older")
else:
    print("Boy 1 is older")
