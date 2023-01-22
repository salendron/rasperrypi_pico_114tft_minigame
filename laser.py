class Laser():

    def __init__(self, display, position, remove_func, is_enemy=False):
        self.display = display
        self.position = position
        self.velocity = 4
        self.remove_func = remove_func
        self.is_enemy = is_enemy

    def process_event(self, event):
        pass

    def draw(self):
        if self.is_enemy:
            self.position = (self.position[0] - self.velocity, self.position[1])
            self.display.fill_rect(self.position[0],self.position[1],16,4,self.display.red)
        else:
            self.position = (self.position[0] + self.velocity, self.position[1])
            self.display.fill_rect(self.position[0],self.position[1],16,4,self.display.green)

        if self.position[0] > 240 + 16 or self.position[0] < -16:
            self.remove_func(self)