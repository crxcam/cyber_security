from datetime import datetime, timedelta
import locale
from time import time


import pytz

# locale.setlocale(locale.LC_TIME, 'fr_FR')
timezone = pytz.timezone('America/New_York')

day = datetime.now()
print(datetime.now())
print(datetime.today())
print(day.year)
print(day.minute)
print(day.strftime('%B'))


anniversaire  = datetime(1970,7,5)
print(anniversaire)
anniversaire_2 =  anniversaire + timedelta(days=2)
print(anniversaire_2)
print(anniversaire_2 >anniversaire )
difference = day -  anniversaire
print(difference.days )
print(timezone )
print(datetime.now(timezone))
print(time())

