"""
Review Question 12
Create two base classes named clock and calendar. Based on these two
classes define a class calendarclock, which inherits from both the
classes which displays month details, date and time
"""


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def display_time(self):
        print(f"{self.hour}:{self.minute}:{self.second}")


class Calendar:
    def __init__(self, month, date):
        self.month = month
        self.date = date

    def display_date(self):
        print(f"{self.date} {self.month}")


class CalendarClock(Clock, Calendar):
    def __init__(self, month, date, hour, minute, second):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, month, date)

    def display_datetime(self):
        self.display_date()
        self.display_time()


def main():
    calendar_clock = CalendarClock("January", 30, 12, 32, 47)
    calendar_clock.display_datetime()


if __name__ == "__main__":
    main()
