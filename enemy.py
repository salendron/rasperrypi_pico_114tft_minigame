from events import *
from laser import Laser
import utime
import random

class Enemy():

    def __init__(self, display, position):
        self.display = display
        self.position = position
        self.velocity = 4
        self.lasers = []
        self.last_shot = utime.ticks_ms() - 3000
        self.last_direction_change = utime.ticks_ms()
        self.move_up = False

    def move(self):
        if self.move_up:
            if self.position[1] > 0:
                self.position = (self.position[0], self.position[1] - self.velocity)
            else:
                self.position = (self.position[0], 0)
                self.move_up = False
                self.last_direction_change = utime.ticks_ms()
        else:
            if self.position[1] < 128 - 16:
                self.position = (self.position[0], self.position[1] + self.velocity)
            else:
                self.position = (self.position[0], 128-16)
                self.move_up = True
                self.last_direction_change = utime.ticks_ms()

        if utime.ticks_ms() - self.last_direction_change > 800:
            self.move_up = random.choice([True, False])
            self.last_direction_change = utime.ticks_ms()

    def shoot(self):
        if utime.ticks_ms() - self.last_shot > 5000 and random.choice([False, False, True, False, False, False]):
            laser = Laser(self.display, (self.position[0] - 16, self.position[1] + 6), self.remove_laser, is_enemy=True)
            self.lasers.append(laser)
            self.last_shot = utime.ticks_ms()

    def remove_laser(self, laser):
        self.lasers.remove(laser)

    def draw(self):
        self.move()
        self.shoot()

        self.display.fill_rect(self.position[0],self.position[1],8,16,self.display.red)

        for laser in self.lasers:
            laser.draw()