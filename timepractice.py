import calendar
from datetime import date
from datetime import datetime
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)	
# print(dt_string[0:3])
print(now[10:])