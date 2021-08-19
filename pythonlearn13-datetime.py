import datetime
import pytz

#hours, minutes, seconds, microseconds
t = datetime.time(9,30,45,1000)

print(t.hour)

#.date gives day, month, year
#datetime gives everything, including time
t = datetime.datetime(2016,7,26,12,30,45,100000)

print(t)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_str = str(dt_mtn)
print("dt string: "+dt_str)
#dt = datetime.datetime.strptime(dt_mtn, '%B %d, %Y')
#print(dt)