from pygame import *

window = display.set_mode((700,500))
display.set_caption('ping-pong')
back = (255,255,200)
window.fill(back)

class GameSprite(sprite.Sprite):

   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            run = False
        
    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    racket2.reset()
    ball.reset     


    display.update()