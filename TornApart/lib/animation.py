import datetime

class Animation:
    def __init__(self, speed=10, frames=[]):
        self.speed = speed
        self.frames = frames
        self.index = 0

        self.nt = datetime.datetime.now()
        self.dt = datetime.timedelta(seconds=1/self.speed)

    def restart(self):
        self.index = 0
        self.nt = datetime.datetime.now()
        self.dt = datetime.timedelta(seconds=1/self.speed)

    def update(self):
        p = datetime.datetime.now()
        if p >= self.nt:
            if self.index >= len(self.frames)-1:
                self.index = 0
            else:
                self.index += 1
            self.nt += self.dt

    def get_current_frame(self):
        return self.frames[self.index]