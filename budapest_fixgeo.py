# Import suntime via pip: `pip3 install suntime` 

import datetime
from suntime import Sun, SunTimeException


# Budapest, Hungary fix geodata:

latitude = 49.49
longitude = 19.04

sun = Sun(latitude, longitude)


# Get today's sunrise and sunset in UTC:

today_sr = sun.get_sunrise_time() 
today_ss = sun.get_sunset_time() 


# Get the morning/evening start and end times, no UTC ('hours=1' oct->march; 'hours=2' march->oct):

morning_start = sun.get_sunrise_time() - datetime.timedelta(minutes=24) + datetime.timedelta(hours=2)
morning_end = sun.get_sunrise_time() + datetime.timedelta(minutes=24) + datetime.timedelta(hours=2)

evening_start = sun.get_sunset_time() - datetime.timedelta(minutes=24) + datetime.timedelta(hours=2)
evening_end = sun.get_sunset_time() + datetime.timedelta(minutes=24) + datetime.timedelta(hours=2)


# Get the midday from sunrise and sunset, no UTC ('hours=1' oct->march; 'hours=2' march->oct):

sunrise = today_sr
sunset = today_ss
mid_minutes = (sunset - sunrise) / 2
mid = sunrise + mid_minutes 
sandhya = datetime.timedelta(minutes=24)
no_utc = datetime.timedelta(hours=2)


# Get the midday start and end times, no UTC:

mid_start = mid - sandhya + no_utc
mid_end = mid + sandhya + no_utc


# Print the results:

print('Reggel: \t{} - {}'.format(morning_start.strftime('%H:%M'), morning_end.strftime('%H:%M')))
print('Del: \t\t{} - {}'.format(mid_start.strftime('%H:%M'), mid_end.strftime('%H:%M')))
print('Este: \t\t{} - {}'.format(evening_start.strftime('%H:%M'), evening_end.strftime('%H:%M')))



