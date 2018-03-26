#!/usr/bin/python3
#-*- coding:utf-8 -*-
from seatHhit import SeatHhit
from datetime import *

s = SeatHhit()
user = '*'
s.login(user, user)
next_day = datetime.now() + timedelta(days=1)

labname = '一楼'
roomname = '西104'
seat_number = '116'
date = next_day.strftime('%Y-%m-%d')

while True:
    rstr = ''
    if next_day.isoweekday() is not 3:
        # not wednesday
        r = s.set_seat(labname, roomname, seat_number, date, '08:00', '21:00')
        rstr += r
    else:
        # wednesday
        r = s.set_seat(labname, roomname, seat_number, date, '08:00', '14:00')
        rstr += r
        r = s.set_seat(labname, roomname, seat_number, date, '17:20', '21:00')
        rstr += r
    print(rstr)
    if rstr.find('成功') >= 0:
        break;






# vim: ts=4 sw=4 et :
