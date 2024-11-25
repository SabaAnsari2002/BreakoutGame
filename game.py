# #py63
# import sys
# import pygame as pg
# import random

# class breakout():
#   def main(self):
#     xspeed_init=6
#     yspeed_init=6
#     max_lives=5
#     bat_speed=30
#     score=0
#     width=640
#     height=430
#     pg.init()
#     screen=pg.display.set_mode((width,height))
#     bat=pg.image.load("bat.jpg").convert()
#     batrect=bat.get_rect()
#     ball=pg.image.load("ball.jpg").convert()
#     ballrect=ball.get_rect()
#     pong=pg.mixer.Sound("Blip_1-Surround-147.wav")
#     pong.set_volume(10)
#     wall=Wall()
#     wall.build_wall(width)
#     batrect=batrect.move((width/2)-(batrect.right/2),height-20)
#     ballrect=ballrect.move(width/2,height/2)
#     xspeed=xspeed_init
#     yspeed=yspeed_init
#     lives=max_lives
#     clock=pg.time.Clock()
#     run=True
#     while run:
#       clock.tick(60)
#       for event in pg.event.get():
#         if event.type==pg.KEYDOWN:
#             if event.key==pg.K_LEFT:
#                 batrect=batrect.move(-bat_speed,0)
#                 if batrect.left<0:
#                   batrect.left=0
#             if event.key==pg.K_RIGHT:
#                batrect=batrect.move(bat_speed,0)
#                if batrect.right>width:
#                   batrect.right=width
#     ballrect=ballrect.move(xspeed,yspeed)
#     if ballrect.bottom>=batrect.top and\
#        ballrect.bottom<=batrect.bottom and\
#        ballrect.right>=batrect.left and\
#        ballrect.left<=batrect.right:
#        yspeed=-yspeed
#        pong.play(0)

#     if ballrect.left<0 or ballrect.right>width:
#        xspeed=-xspeed
#        pong.play(0)
#     if ballrect.top<0:
#        yspeed=-yspeed
#        pong.play(0)
#     if ballrect.top>height:
#        lives-=1
#        xspeed=xspeed_init
#        yspeed=yspeed_init
#        if random.random()>0.5:
#           xspeed=-xspeed
#        ballrect.center=width*random.random(),height/3
#        if lives==0:
#           msg=pg.font.Font(None,70).render("Game Over",True,(0,255,255))
#           msgrect=msg.get_rect()
#           msgrect=msgrect.move(width/2-(msgrect.center[0]),height/3)
#           screen.blit(msg,msgrect)
#           pg.display.flip()

#           while 1:
#              restart=False
#              for event in pg.event.get():
#                 if event.type==pg.KEYDOWN:
#                    if not (event.key==pg.K_LEFT) or (event.key==pg.K_RIGHT):
#                       restart=True
#              if restart:
#                 screen.fill((0,0,0))
#                 wall.build_wall(width)
#                 lives=max_lives
#                 score=0
#                 break
#     index=ballrect.collidelist(wall.brickrect)
#     if index!=-1:
#        if ballrect.center[0]>wall.brickrect[index].right or\
#           ballrect.center[0]<wall.brickrect[index].left:
#           xspeed=-xspeed
#        else:
#           yspeed=-yspeed
#        pong.play(0)
#        wall.brickrect[index:index+1]=[]
#        score+=10

#     if wall.brickrect==[]:
#           wall.build_wall(width)
#           xspeed=xspeed_init
#           yspeed=yspeed_init
#           ballrect.center=width/2,height/3
#     screen.fill((0,0,0))
#     for i in range(len(wall.brickrect)):
#        screen.blit(wall.brick,wall.brickrect[i])
#     screen.blit(ball,ballrect)
#     screen.blit(bat,batrect)
#     scoretext=pg.font.Font(None,40).render(str(score),True,(0,255,255))
#     scoretextrect=scoretext.get_rect()
#     scoretextrect=scoretextrect.move(width-scoretextrect.right,0)
#     screen.blit(scoretext,scoretextrect)
#     pg.display.flip()

# class Wall():
#    def __init__(self):
#       self.brick=pg.image.load("brick.jpg").convert()
#       brickrect=self.brick.get_rect()
#       self.bricka=brickrect.right-brickrect.left
#       self.brickb=brickrect.bottom-brickrect.top
#    def build_wall(self,width):
#       xpos=0
#       ypos=60
#       adj=0
#       self.brickrect=[]
#       for  i in range(0,52):
#          if xpos>width:
#             if adj==0:
#                adj=self.bricka/2
#             else:
#                adj=0
#             xpos=-adj
#             ypos+=self.brickb
#             self.brickrect.append(self.brick.get_rect())
#             self.brickrect[i]=self.brickrect[i].move(xpos,ypos)
#             xpos=xpos+self.bricka

# br=breakout()
# br.main()
    
          
import sys
import pygame as pg
import random

class Breakout:
    def main(self):
        xspeed_init = 6
        yspeed_init = 6
        max_lives = 5
        bat_speed = 50
        score = 0
        width = 730
        height = 700
        
        pg.init()
        screen = pg.display.set_mode((width, height))
        bat = pg.image.load("bat.jpg").convert()
        batrect = bat.get_rect()
        ball = pg.image.load("ball.jpg").convert()
        ballrect = ball.get_rect()
        pong = pg.mixer.Sound("Blip_1-Surround-147.wav")
        pong.set_volume(10)
        
        wall = Wall()
        wall.build_wall(width)
        
        batrect = batrect.move((width/2) - (batrect.right/2), height - 20)
        ballrect = ballrect.move(width/2, height/2)
        xspeed = xspeed_init
        yspeed = yspeed_init
        lives = max_lives
        clock = pg.time.Clock()
        run = True

        while run:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        batrect = batrect.move(-bat_speed, 0)
                        if batrect.left < 0:
                            batrect.left = 0
                    if event.key == pg.K_RIGHT:
                        batrect = batrect.move(bat_speed, 0)
                        if batrect.right > width:
                            batrect.right = width

            ballrect = ballrect.move(xspeed, yspeed)
            if ballrect.bottom >= batrect.top and \
               ballrect.bottom <= batrect.bottom and \
               ballrect.right >= batrect.left and \
               ballrect.left <= batrect.right:
                yspeed = -yspeed
                pong.play(0)

            if ballrect.left < 0 or ballrect.right > width:
                xspeed = -xspeed
                pong.play(0)
            if ballrect.top < 0:
                yspeed = -yspeed
                pong.play(0)
            if ballrect.top > height:
                lives -= 1
                xspeed = xspeed_init
                yspeed = yspeed_init
                if random.random() > 0.5:
                    xspeed = -xspeed
                ballrect.center = (width * random.random(), height/3)
                if lives == 0:
                    msg = pg.font.Font(None, 70).render("Game Over", True, (0, 255, 255))
                    msgrect = msg.get_rect()
                    msgrect = msgrect.move(width/2 - (msgrect.center[0]), height/3)
                    screen.blit(msg, msgrect)
                    pg.display.flip()

                    waiting = True
                    while waiting:
                        for event in pg.event.get():
                            if event.type == pg.KEYDOWN:
                                waiting = False
                    screen.fill((0, 0, 0))
                    wall.build_wall(width)
                    lives = max_lives
                    score = 0

            index = ballrect.collidelist(wall.brickrect)
            if index != -1:
                if ballrect.center[0] > wall.brickrect[index].right or \
                   ballrect.center[0] < wall.brickrect[index].left:
                    xspeed = -xspeed
                else:
                    yspeed = -yspeed
                pong.play(0)
                wall.brickrect[index:index+1] = []
                score += 10

            if not wall.brickrect:
                wall.build_wall(width)
                xspeed = xspeed_init
                yspeed = yspeed_init
                ballrect.center = (width/2, height/3)

            screen.fill((0, 0, 0))
            for i in range(len(wall.brickrect)):
                screen.blit(wall.brick, wall.brickrect[i])
            screen.blit(ball, ballrect)
            screen.blit(bat, batrect)
            scoretext = pg.font.Font(None, 40).render(str(score), True, (0, 255, 255))
            scoretextrect = scoretext.get_rect()
            scoretextrect = scoretextrect.move(width - scoretextrect.right, 0)
            screen.blit(scoretext, scoretextrect)
            pg.display.flip()

        pg.quit()

class Wall:
    def __init__(self):
        self.brick = pg.image.load("brick.jpg").convert()
        brickrect = self.brick.get_rect()
        self.bricka = brickrect.right - brickrect.left
        self.brickb = brickrect.bottom - brickrect.top

    def build_wall(self, width):
        xpos = 0
        ypos = 60
        adj = 0
        self.brickrect = []
        for i in range(0, 52):
            if xpos > width:
                if adj == 0:
                    adj = self.bricka / 2
                else:
                    adj = 0
                xpos = -adj
                ypos += self.brickb
            self.brickrect.append(self.brick.get_rect())
            self.brickrect[i] = self.brickrect[i].move(xpos, ypos)
            xpos = xpos + self.bricka

if __name__ == "__main__":
    br = Breakout()
    br.main()
