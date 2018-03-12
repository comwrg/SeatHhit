import requests
import time

class SeatHhit:
    def __init__(self):
        self.sess = requests.session()

    def login(self, id, pwd):
        r = self.sess.get(
            'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/login.aspx?'
            'act=login&id={id}&pwd={pwd}&role=512&_nocache=1520821128524'
            .format(id=id, pwd=pwd))
        print(r.text)

    def get_room(self):
        """

        :return: json
        """
        date = time.strftime('%Y-%m-%d', time.localtime())
        r = self.sess.get(
            'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/room.aspx?act=get_rm_sta&classkind=8&date={date}'
            .format(date=date)
        )
        return r.json()

    def find_roomid(self, labname, roomname):
        """

        :param labname: 一楼
        :param roomname: 西104
        :return: roomid if find else None
        """
        json = self.get_room()
        data = json['data']
        for item in data:
            if item['labName'] == labname and item['name'] == roomname:
                return item['id']
        return None

    def get_seat(self, labname, roomname, date):
        room_id = self.find_roomid(labname, roomname)
        r = self.sess.get(
            'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/device.aspx?act=get_rsv_sta&classkind=8'
            '&right=detail&fr_all_day=false&room_id={room_id}&date={date}'
            .format(room_id=room_id, date=date)
        )
        return r.json()

    def find_seat(self, labname, roomname, seat, date):
        json = self.get_seat(labname, roomname, date)
        data = json['data']
        name = '{0}-{1}'.format(roomname, seat)
        for item in data:
            if item['devName'] == name:
                return item['devId']
        return None

    def set_seat(self, labname, roomname, seat_number, date, start, end):
        seat_id = self.find_seat(labname, roomname, seat_number, date)
        r = self.sess.get(
            'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/reserve.aspx?act=set_resv'
            '&dev_id={seat_id}&start={start}&end={end}'
            .format(seat_id=seat_id, start='{0} {1}'.format(date, start), end='{0} {1}'.format(date, end))
        )
        return r.text


if __name__ == '__main__':
    pass
