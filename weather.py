#!/usr/bin/python
import sys
import math
import pyowm

beaufort = {0: 'calm',
        1: 'light air',
        2: 'light breeze',
        3: 'gentle breeze',
        4: 'moderate breeze',
        5: 'fresh breeze',
        6: 'strong breeze',
        7: 'near gale',
        8: 'gale',
        9: 'strong gale',
        10: 'storm',
        11: 'violent storm',
        12: 'hurricane'};

owm = pyowm.OWM('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

city = sys.argv[1] if len(sys.argv) > 1 else 'london'
pays = 'gb'
days = int(sys.argv[2]) if len(sys.argv) == 3 else 2

forecast = owm.daily_forecast(city + ',' + pays, limit=(days))

f = forecast.get_forecast()
for weather in f:
    o = weather.get_reference_time('date')
    i = weather.get_weather_icon_name()
    s = weather.get_detailed_status()
    t = weather.get_temperature(unit='celsius')
    w = weather.get_wind()
    m = int(w["speed"])
    b = int((( m/0.836)**2)**(1.0/3.0))
    o_str = str(o)
    d = o_str[5:10]
    date = d.replace("-","/")
    print "%s: %s, %s/%sC, Force %s, %s." % (date,  s, int(t["min"]), int(t["max"]), b, beaufort[b])
