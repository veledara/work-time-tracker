from datetime import datetime


class Session:
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.running = True
        self.day = self.start_time.day
        self.week = self.start_time.isocalendar()[1]

    def end_session(self):
        self.end_time = datetime.now()
        self.running = False

    @property
    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        else:
            return (datetime.now() - self.start_time).total_seconds()
