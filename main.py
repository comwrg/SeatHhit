from seatHhit import SeatHhit
from datetime import *

s = SeatHhit()
s.login('2015122137', '2015122137')
next_day = datetime.now() + timedelta(days=1)

labname = '一楼'
roomname = '西104'
seat_number = '116'
date = next_day.strftime('%Y-%m-%d')

if datetime.now().isoweekday() is not 3:
    # not wednesday
    r = s.set_seat(labname, roomname, seat_number, date, '08:00', '21:00')
    print(r)
else:
    # wednesday
    r = s.set_seat(labname, roomname, seat_number, date, '08:00', '14:00')
    print(r)
    r = s.set_seat(labname, roomname, seat_number, date, '17:20', '21:00')
    print(r)
