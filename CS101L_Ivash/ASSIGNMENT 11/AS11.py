import time
class Clock:
    # init method takes hour, minute and second
    # clock_type with default value 0
    # 0 - 24 HR format
    # 1 - 12 HR Format
    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    # tick method to increase time by one second
    def tick(self):
        # add one second
        self.second += 1
        # if second is 60
        if self.second == 60:
            # reset second
            self.second = 0
            # increase minute
            self.minute += 1
            # if minute is 60
            if self.minute == 60:
                # reset minute
                self.minute = 0
                # increase hour
                self.hour += 1
                # if 24 hours passed
                if self.hour == 25:
                    # reset hour
                    self.hour = 0

    # str method returns the string representation of current clock
    def __str__(self):
        # if 24 hour mode, return HH:MM:SS format
        # {:02} in format creates two digit numbers eg 1 will be 01 ..etc
        if self.clock_type == 0:
            return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
        # else 12 hour mode, return HH:MM:SS am/pm format
        # {:02} in format creates two digit numbers eg 1 will be 01 ..etc
        else:
            # for 0 to 11 will be am, print as it is
            if self.hour <= 11:
                # 0 represents 12
                if self.hour == 0:
                    return "{:02}:{:02}:{:02} am".format(12, self.minute, self.second)
                # else normally print in the format
                else:
                    return "{:02}:{:02}:{:02} am".format(self.hour, self.minute, self.second)
            # for 12 - 24, we have to subtract 12 in order to get hours
            else:
                return "{:02}:{:02}:{:02} pm".format(self.hour - 12, self.minute, self.second)
hour=int(input("What is the current hour ==>"))
minute=int(input("What is the current minute==>"))
second=int(input("What is the current second==>"))
clock=Clock(hour,minute,second,clock_type=1)
while True:
    print(clock)
    clock.tick()
    time.sleep(1)