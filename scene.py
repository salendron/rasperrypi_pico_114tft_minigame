from player import Player
from statusbar import Statusbar
from enemy import Enemy
import utime
from events import *

class Scene():

    def __init__(self, display, bg_color):
        self.display = display
        self.bg_color = bg_color
        self.enemy_postions = (240 - 16, 240 - 32, 240 - 48)

        self.init_game()

    def init_game(self):
        self.children = []
        self.enemies = []
        
        self.player = Player(self.display,(16, 16))
        self.status_bar = Statusbar(self.display,(0, 128), self.player)

        self.children.append(self.player)
        self.children.append(self.status_bar)

        self.gameover = False

    def process_event(self, event):
        if self.gameover and event == EVENT_B:
            self.init_game()

        for child in self.children:
            child.process_event(event)

    def draw(self):
        self.check_enemy_hit()
        self.check_player_hit()

        self.display.fill(self.bg_color)
        for child in self.children:
            child.draw()

        if self.gameover == False:
            for enemy in self.enemies:
                enemy.draw()

            self.spawn_enemy()
        else:
            self.display.text("Game Over!",90,60,self.display.red)

    def spawn_enemy(self):
        if len(self.enemies) <= 3:
            pos = 240 - (16 * len(self.enemies))

            enemy = Enemy(self.display, (pos,16))
            self.enemies.append(enemy)

    def check_enemy_hit(self):
        for laser in self.player.lasers:
            for enemy in self.enemies:
                if laser.position[0] >= enemy.position[0] - 16 and laser.position[0] < enemy.position[0] + 16:
                    if laser.position[1] >= enemy.position[1] and laser.position[1] < enemy.position[1] + 16:
                        enemy.position = (enemy.position[0], 16)
                        self.player.remove_laser(laser)
                        self.status_bar.points += 1

    def check_player_hit(self):
        for enemy in self.enemies:
            for laser in enemy.lasers:
                if laser.position[0] <= self.player.position[0] + 16 and laser.position[0] > self.player.position[0] - 16:
                    if laser.position[1] >= self.player.position[1] and laser.position[1] < self.player.position[1] + 16:
                        self.player.health -= 1
                        enemy.lasers.remove(laser)

                        if self.player.health <= 0:
                            self.gameover = True
                            self.children.remove(self.player)