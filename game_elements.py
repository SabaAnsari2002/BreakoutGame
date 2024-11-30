# import sys
# import pygame as pg
# import time
# from wall import Wall


# class Breakout:
#     def __init__(self):
#         self.width = 730
#         self.height = 700
#         self.bat_speed = 50
#         self.xspeed_init = 6
#         self.yspeed_init = 6
#         self.max_lives = 5
#         self.score = 0
#         self.lives = self.max_lives
#         self.timer_start = None
#         self.final_time = 0  # زمان ثابت پایان بازی
#         self.game_active = False
#         self.game_won = False

#         pg.init()
#         self.screen = pg.display.set_mode((self.width, self.height))
#         pg.display.set_caption("Breakout Game")
#         self.clock = pg.time.Clock()
#         self.font = pg.font.Font(None, 40)
#         self.big_font = pg.font.Font(None, 70)

#         # Load assets and scale
#         self.bat = pg.image.load("bat.jpg").convert()
#         self.ball = pg.image.load("ball.png").convert_alpha()
#         self.brick = pg.image.load("brick.png").convert()

#         # Scale assets
#         self.bat = pg.transform.scale(self.bat, (self.width // 6, self.height // 40))
#         self.ball = pg.transform.scale(self.ball, (self.width // 10, self.width // 10))
#         self.brick = pg.transform.scale(self.brick, (self.width // 10, self.height // 25))

#         self.batrect = self.bat.get_rect()
#         self.ballrect = self.ball.get_rect()

#         self.pong_sound = pg.mixer.Sound("Blip_1-Surround-147.wav")
#         self.pong_sound.set_volume(10)

#         self.wall = Wall(self.brick)
#         self.reset_positions()

#     def reset_positions(self):
#         self.batrect.midbottom = (self.width / 2, self.height - 20)
#         self.ballrect.center = (self.width / 2, self.height / 2)
#         self.xspeed = self.xspeed_init
#         self.yspeed = self.yspeed_init

#     def show_start_screen(self):
#         self.screen.fill((0, 0, 0))
#         title_text = self.big_font.render("Breakout Game", True, (255, 255, 255))
#         start_text = self.font.render("Press ENTER to Start", True, (0, 255, 0))
#         self.screen.blit(title_text, (self.width / 2 - title_text.get_width() / 2, self.height / 3))
#         self.screen.blit(start_text, (self.width / 2 - start_text.get_width() / 2, self.height / 2))
#         pg.display.flip()

#     def show_end_screen(self):
#         self.screen.fill((0, 0, 0))
#         if self.game_won:
#             message = "You Win!"
#             color = (0, 255, 0)
#         else:
#             message = "Game Over!"
#             color = (255, 0, 0)

#         end_text = self.big_font.render(message, True, color)
#         score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
#         time_text = self.font.render(f"Time: {self.final_time}s", True, (255, 255, 255))  # استفاده از زمان ثابت
#         restart_text = self.font.render("Press R to Restart", True, (0, 255, 255))

#         self.screen.blit(end_text, (self.width / 2 - end_text.get_width() / 2, self.height / 3))
#         self.screen.blit(score_text, (self.width / 2 - score_text.get_width() / 2, self.height / 2))
#         self.screen.blit(time_text, (self.width / 2 - time_text.get_width() / 2, self.height / 2 + 40))
#         self.screen.blit(restart_text, (self.width / 2 - restart_text.get_width() / 2, self.height / 2 + 80))
#         pg.display.flip()

#     def run(self):
#         while True:
#             if not self.game_active:
#                 if self.timer_start is None:
#                     self.show_start_screen()
#                     self.handle_start_screen_events()
#                 else:
#                     self.show_end_screen()
#                     self.handle_end_screen_events()
#             else:
#                 self.handle_game_events()
#                 self.update_game()
#                 self.render_game()
#             self.clock.tick(60)

#     def handle_start_screen_events(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#             if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
#                 self.game_active = True
#                 self.score = 0
#                 self.lives = self.max_lives
#                 self.wall.build_wall(self.width)
#                 self.timer_start = time.time()
#                 self.reset_positions()

#     def handle_end_screen_events(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#             if event.type == pg.KEYDOWN and event.key == pg.K_r:
#                 self.timer_start = None
#                 self.game_active = False

#     def handle_game_events(self):
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT]:
#             self.batrect.x -= self.bat_speed
#             if self.batrect.left < 0:
#                 self.batrect.left = 0
#         if keys[pg.K_RIGHT]:
#             self.batrect.x += self.bat_speed
#             if self.batrect.right > self.width:
#                 self.batrect.right = self.width

#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()

#     def update_game(self):
#         self.ballrect.x += self.xspeed
#         self.ballrect.y += self.yspeed

#         # Ball collisions with walls
#         if self.ballrect.left <= 0 or self.ballrect.right >= self.width:
#             self.xspeed = -self.xspeed
#             self.pong_sound.play()
#         if self.ballrect.top <= 0:
#             self.yspeed = -self.yspeed
#             self.pong_sound.play()

#         # Ball collision with paddle
#         if self.ballrect.colliderect(self.batrect):
#             self.yspeed = -self.yspeed
#             self.pong_sound.play()

#         # Ball goes out of screen
#         if self.ballrect.top > self.height:
#             self.lives -= 1
#             self.reset_positions()
#             if self.lives == 0:
#                 self.game_active = False
#                 self.game_won = False
#                 self.final_time = int(time.time() - self.timer_start)  # زمان پایان بازی

#         # Ball collision with bricks
#         index = self.ballrect.collidelist(self.wall.brickrect)
#         if index != -1:
#             brick_hit = self.wall.brickrect[index]
#             if self.ballrect.centerx < brick_hit.left or self.ballrect.centerx > brick_hit.right:
#                 self.xspeed = -self.xspeed
#             else:
#                 self.yspeed = -self.yspeed
#             self.pong_sound.play()
#             del self.wall.brickrect[index]
#             self.score += 10

#         # Check if all bricks are cleared
#         if not self.wall.brickrect:
#             self.game_active = False
#             self.game_won = True
#             self.final_time = int(time.time() - self.timer_start)  # زمان پایان بازی

#     def render_game(self):
#         self.screen.fill((0, 0, 0))
#         # Draw bricks
#         for brick in self.wall.brickrect:
#             self.screen.blit(self.brick, brick)

#         # Draw paddle and ball
#         self.screen.blit(self.bat, self.batrect)
#         self.screen.blit(self.ball, self.ballrect)

#         # Draw score and lives
#         score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
#         lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
#         timer_text = self.font.render(f"Time: {int(time.time() - self.timer_start)}s", True, (255, 255, 255))
#         self.screen.blit(score_text, (10, 10))
#         self.screen.blit(lives_text, (10, 40))
#         self.screen.blit(timer_text, (10, 70))

#         pg.display.flip()


# if __name__ == "__main__":
#     game = Breakout()
#     game.run()


import sys
import pygame as pg
import time
from wall import Wall

class Breakout:
    def __init__(self):
        self.width = 730
        self.height = 700
        self.bat_speed = 50
        self.xspeed_init = 6
        self.yspeed_init = 6
        self.max_lives = 5
        self.score = 0
        self.lives = self.max_lives
        self.timer_start = None
        self.final_time = 0
        self.game_active = False
        self.game_won = False
        self.difficulty = "Normal"
        self.power_ups = []

        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Breakout Game")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 40)
        self.big_font = pg.font.Font(None, 70)

        # Load assets and scale
        self.bat = pg.image.load("bat.jpg").convert()
        self.ball = pg.image.load("ball.png").convert_alpha()
        self.brick = pg.image.load("brick.png").convert()
        self.power_up_img = pg.image.load("power_up.png").convert_alpha()

        # Scale assets
        self.bat = pg.transform.scale(self.bat, (self.width // 6, self.height // 40))
        self.ball = pg.transform.scale(self.ball, (self.width // 10, self.width // 10))
        self.brick = pg.transform.scale(self.brick, (self.width // 10, self.height // 25))
        self.power_up_img = pg.transform.scale(self.power_up_img, (30, 30))

        self.batrect = self.bat.get_rect()
        self.ballrect = self.ball.get_rect()

        self.pong_sound = pg.mixer.Sound("Blip_1-Surround-147.wav")
        self.pong_sound.set_volume(10)

        self.wall = Wall(self.brick)
        self.reset_positions()

    def reset_positions(self):
        self.batrect.midbottom = (self.width / 2, self.height - 20)
        self.ballrect.center = (self.width / 2, self.height / 2)
        self.xspeed = self.xspeed_init
        self.yspeed = self.yspeed_init

    def show_start_screen(self):
        self.screen.fill((0, 0, 0))
        title_text = self.big_font.render("Breakout Game", True, (255, 255, 255))
        start_text = self.font.render("Press ENTER to Start", True, (0, 255, 0))
        difficulty_text = self.font.render(f"Difficulty: {self.difficulty}", True, (255, 255, 0))
        controls_text = self.font.render("D: Change Difficulty", True, (255, 255, 255))
        
        self.screen.blit(title_text, (self.width / 2 - title_text.get_width() / 2, self.height / 3))
        self.screen.blit(start_text, (self.width / 2 - start_text.get_width() / 2, self.height / 2))
        self.screen.blit(difficulty_text, (self.width / 2 - difficulty_text.get_width() / 2, self.height / 2 + 50))
        self.screen.blit(controls_text, (self.width / 2 - controls_text.get_width() / 2, self.height / 2 + 100))
        
        pg.display.flip()

    def show_end_screen(self):
        self.screen.fill((0, 0, 0))
        if self.game_won:
            message = "You Win!"
            color = (0, 255, 0)
        else:
            message = "Game Over!"
            color = (255, 0, 0)
        
        end_text = self.big_font.render(message, True, color)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        time_text = self.font.render(f"Time: {self.final_time}s", True, (255, 255, 255))
        restart_text = self.font.render("Press R to Restart", True, (0, 255, 255))
        
        self.screen.blit(end_text, (self.width / 2 - end_text.get_width() / 2, self.height / 3))
        self.screen.blit(score_text, (self.width / 2 - score_text.get_width() / 2, self.height / 2))
        self.screen.blit(time_text, (self.width / 2 - time_text.get_width() / 2, self.height / 2 + 40))
        self.screen.blit(restart_text, (self.width / 2 - restart_text.get_width() / 2, self.height / 2 + 80))
        
        pg.display.flip()

    def run(self):
        while True:
            if not self.game_active:
                if self.timer_start is None:
                    self.show_start_screen()
                    self.handle_start_screen_events()
                else:
                    self.show_end_screen()
                    self.handle_end_screen_events()
            else:
                self.handle_game_events()
                self.update_game()
                self.render_game()
            self.clock.tick(60)

    def handle_start_screen_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.start_game()
                elif event.key == pg.K_d:
                    self.change_difficulty()

    def change_difficulty(self):
        difficulties = ["Easy", "Normal", "Hard"]
        current_index = difficulties.index(self.difficulty)
        self.difficulty = difficulties[(current_index + 1) % len(difficulties)]
        if self.difficulty == "Easy":
            self.xspeed_init = 4
            self.yspeed_init = 4
            self.max_lives = 7
        elif self.difficulty == "Normal":
            self.xspeed_init = 6
            self.yspeed_init = 6
            self.max_lives = 5
        else:  # Hard
            self.xspeed_init = 8
            self.yspeed_init = 8
            self.max_lives = 3

    def start_game(self):
        self.game_active = True
        self.score = 0
        self.lives = self.max_lives
        self.wall.build_wall(self.width)
        self.timer_start = time.time()
        self.reset_positions()
        self.power_ups = []

    def handle_end_screen_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                self.timer_start = None
                self.game_active = False

    def handle_game_events(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.batrect.x -= self.bat_speed
            if self.batrect.left < 0:
                self.batrect.left = 0
        if keys[pg.K_RIGHT]:
            self.batrect.x += self.bat_speed
            if self.batrect.right > self.width:
                self.batrect.right = self.width
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update_game(self):
        self.ballrect.x += self.xspeed
        self.ballrect.y += self.yspeed

        # Ball collisions with walls
        if self.ballrect.left <= 0 or self.ballrect.right >= self.width:
            self.xspeed = -self.xspeed
            self.pong_sound.play()
        if self.ballrect.top <= 0:
            self.yspeed = -self.yspeed
            self.pong_sound.play()

        # Ball collision with paddle
        if self.ballrect.colliderect(self.batrect):
            self.yspeed = -self.yspeed
            self.pong_sound.play()

        # Ball goes out of screen
        if self.ballrect.top > self.height:
            self.lives -= 1
            self.reset_positions()
            if self.lives == 0:
                self.game_active = False
                self.game_won = False
                self.final_time = int(time.time() - self.timer_start)

        # Ball collision with bricks
        index = self.ballrect.collidelist(self.wall.brickrect)
        if index != -1:
            brick_hit = self.wall.brickrect[index]
            if self.ballrect.centerx < brick_hit.left or self.ballrect.centerx > brick_hit.right:
                self.xspeed = -self.xspeed
            else:
                self.yspeed = -self.yspeed
            self.pong_sound.play()
            del self.wall.brickrect[index]
            self.score += 10
            
            # Chance to spawn power-up
            if pg.time.get_ticks() % 5 == 0:  # 20% chance
                self.power_ups.append(pg.Rect(brick_hit.centerx, brick_hit.centery, 30, 30))

        # Update power-ups
        for power_up in self.power_ups[:]:
            power_up.y += 2
            if power_up.colliderect(self.batrect):
                self.apply_power_up()
                self.power_ups.remove(power_up)
            elif power_up.top > self.height:
                self.power_ups.remove(power_up)

        # Check if all bricks are cleared
        if not self.wall.brickrect:
            self.game_active = False
            self.game_won = True
            self.final_time = int(time.time() - self.timer_start)

    def apply_power_up(self):
        power_up_type = pg.time.get_ticks() % 3
        if power_up_type == 0:
            self.bat_speed += 10  # Increase paddle speed
        elif power_up_type == 1:
            self.lives += 1  # Extra life
        else:
            self.batrect = self.batrect.inflate(20, 0)  # Wider paddle

    def render_game(self):
        self.screen.fill((0, 0, 0))
        
        # Draw bricks
        for brick in self.wall.brickrect:
            self.screen.blit(self.brick, brick)
        
        # Draw paddle and ball
        self.screen.blit(self.bat, self.batrect)
        self.screen.blit(self.ball, self.ballrect)
        
        # Draw power-ups
        for power_up in self.power_ups:
            self.screen.blit(self.power_up_img, power_up)
        
        # Draw score, lives, and timer
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        timer_text = self.font.render(f"Time: {int(time.time() - self.timer_start)}s", True, (255, 255, 255))
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))
        self.screen.blit(timer_text, (10, 70))
        
        pg.display.flip()

if __name__ == "__main__":
    game = Breakout()
    game.run()