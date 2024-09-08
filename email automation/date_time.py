import datetime as dt

now = dt.datetime.now()
year =now.year
month=now.month
day_of_week = now.weekday()

print(year)
print(day_of_week)


#create your own

date_of_birth =dt.datetime(year=2005, month=12, day=15)

print(date_of_birth)