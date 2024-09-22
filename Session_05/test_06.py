from datetime import datetime

str_date = "2/6/2024"

convert_to_date = datetime.strptime(str_date, "%m/%d/%Y")
print(convert_to_date)

convert_month = datetime.strftime(convert_to_date, "%d %b del %Y")
print(convert_month)
