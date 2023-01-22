from events import *
from laser import Laser
import utime

class Player():

    def __init__(self, display, position):
        self.display = display
        self.position = position
        self.velocity = 4
        self.health = 10
        self.lasers = []
        self.last_shot = utime.ticks_ms()

    def process_event(self, event):
        if event == EVENT_UP:
            self.move(True)
        
        if event == EVENT_DOWN:
            self.move(False)

        if event == EVENT_A:
            self.shoot()

    def draw(self):
        self.display.fill_rect(self.position[0],self.position[1],16,16,self.display.green)

        for laser in self.lasers:
            laser.draw()

    def move(self, up):
        if up:
            if self.position[1] > 0:
                self.position = (self.position[0], self.position[1] - self.velocity)
            else:
                self.position = (self.position[0], 0)
        else:
            if self.position[1] < 128 - 16:
                self.position = (self.position[0], self.position[1] + self.velocity)
            else:
                self.position = (self.position[0], 128-16)

    def shoot(self):
        if utime.ticks_ms() - self.last_shot > 1000:
            laser = Laser(self.display, (self.position[0] + 16, self.position[1] + 6), self.remove_laser)
            self.lasers.append(laser)
            self.last_shot = utime.ticks_ms()

    def remove_laser(self, laser):
        self.lasers.remove(laser)