class Statusbar():

    def __init__(self, display, position, player):
        self.display = display
        self.position = position
        self.points = 0
        self.player = player

    def process_event(self, event):
        pass

    def draw(self):
        self.display.text("Score: " + str(self.points) + " Health: " + str(self.player.health),self.position[0] + 8,self.position[1],self.display.white)
