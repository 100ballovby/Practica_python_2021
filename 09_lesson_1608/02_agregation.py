class AlarmSetView:
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m

    def get_alarm_time(self):
        return f'{self.hours}:{self.minutes}'


class AlarmListView:
    def __init__(self):
        morning1 = AlarmSetView(7, 43)
        morning2 = AlarmSetView(7, 50)
        self.list = []
        self.list.append(morning1.get_alarm_time())
        self.list.append(morning2.get_alarm_time())
        print('Ваши будильники')
        for alarm in self.list:
            print(alarm)


alarm = AlarmListView()

