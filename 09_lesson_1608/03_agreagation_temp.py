class AlarmSetView:
    def __init__(self):
        print('Заведите будильник')
        self.alarm = ''

    def set_alarm(self, h, m):
        self.alarm = h, m

    def get_alarm_time(self):
        return self.alarm


class AlarmListView:
    def __init__(self):
        print('Ваши будильники')
        self.a_list = []

    def save_alarm(self, time):
        self.a_list.append(time)
        print(f'Ваши будельиники {self.a_list}')


alarm1 = AlarmSetView()
alarm1.set_alarm(7, 15)

alarm2 = AlarmSetView()
alarm2.set_alarm(7, 30)

list_alarms = AlarmListView()
list_alarms.save_alarm(alarm1.get_alarm_time())
list_alarms.save_alarm(alarm2.get_alarm_time())
