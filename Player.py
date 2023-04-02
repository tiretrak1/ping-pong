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

class Player(GameSprite):
	def update_r(self):
		keys = key.get_pressed()
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_DOWN] and self.rect.y < 620:
			self.rect.y += self.speed
	def update_l(self):
		keys = key.get_pressed()
		if keys[K_w] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_s] and self.rect.y < 620:
			self.rect.y += self.speed


game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            run = False
        

    display.update()