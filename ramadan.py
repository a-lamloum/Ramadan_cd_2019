
# import modules
import time
from datetime import datetime

# spacify ramadan starting date and the time right now
ramadan = datetime(2019, 5, 6)
delta = ramadan - datetime.now()

# convert datetime formate to to_integer
def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

dt_ram = to_integer(datetime(2019, 5, 6))
dt_now = to_integer(datetime.now())

#print the time remaing for ramadan
while dt_ram > dt_now:
    datetime_object = datetime.strptime(str(delta), '%d %H:%M:%S')
    print(datetime_object)
    pass
