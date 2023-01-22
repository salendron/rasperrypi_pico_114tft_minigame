import time, utime

class Clock():

    def __init__(self, fps):
        self.fps = fps
        self.time_per_frame = int(1000 / self.fps)
        self.last_tick = utime.ticks_ms()

    def tick(self):
        wait_time = self.time_per_frame - utime.ticks_ms() - self.last_tick

        if wait_time > 0:
            time.sleep_ms(wait_time)
            
        self.last_tick = utime.ticks_ms()