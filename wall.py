class Wall:
    def __init__(self, brick_image):
        self.brick = brick_image
        self.brickrect = []

    def build_wall(self, width):
        self.brickrect = []
        brick_width = self.brick.get_width()
        brick_height = self.brick.get_height()
        xpos, ypos = 0, 60
        for _ in range(50):
            if xpos + brick_width > width:
                xpos = 0
                ypos += brick_height
            rect = self.brick.get_rect(topleft=(xpos, ypos))
            self.brickrect.append(rect)
            xpos += brick_width
