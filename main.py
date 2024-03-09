from pygame import *
import random
window = display.set_mode((700, 500))
clock = time.Clock()
mixer.init()

space = mixer.Sound("space.ogg")
space.play()
background = image.load("galaxy.jpg")
background = transform.scale(background, (700,500))

class Hero(sprite.Sprite):
    def __init__(self, x, y, width, height, speed, image_name="rocket.png"):
        super().__init__()

        self.image = image.load(image_name)
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Hero):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <700:
            self.rect.x += self.speed


class Enemy (Hero):
    def move(self):
        
        self.rect.y += self.speed
        if self.rect.y >560:
            self.rect.x = random.randint(100,600)
            self.rect.y = -100


Enemy1= Enemy(350, -100, 150, 50, 3, "ufo.png" )

rocket1=Player(300, 340 , 100,150,5)

Game = True
while Game:
    window.blit(background, (0, 0))
    rocket1.reset()
    Enemy1.reset()
    rocket1.move()
    Enemy1.move()



    for e in event.get():
        if e.type == QUIT:
            Game = False



    clock.tick(60)
    display.update()



# class GameSprite():
#     def __init__(self, img, speed, x, y):
#         self.img = transform.scale(image.load(img), (65, 65))
#         self.rect = self.img.get_rect()
#         self.speed = speed
#         self.rect.x = x
#         self.rect.y = y
#         self.move_right=False
#         self.move_left=False
#         self.move_up=False
#         self.move_down=False
#         self.direction="right"