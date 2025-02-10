
class Event:
    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location.upper()

    def __eq__(self, other):
        if self.day == other.day:
            if self.time == other.time:
                if self.location == other.location:
                    return True
                return False
            return False
        return False


    def __str__(self):
        def format(time):
            return f"{time[0] // 100:0>2}:{time[0] % 100:0>2} - {time[1] // 100:0>2}:{time[1] % 100:0>2}"
        return "{} {}, {}".format(self.day, format(self.time), self.location)


