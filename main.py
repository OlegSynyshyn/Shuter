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
bullets = []



class Bulet(Hero):
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y > -60:
            self.kill()  


             
class Player(Hero): 
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <620:
            self.rect.x += self.speed


    def fire(self):
        bullet = Bulet(self.rect.centerx, self.rect.y , 10,10,10, "bullet.png")
        bullets.append(bullet)
counter = 0 
monster_kill = 0



class Enemy (Hero):
    def move(self):
        
        self.rect.y += self.speed
        global counter
        if self.rect.y >560:
            counter+=1
            self.rect.x = random.randint(100,565)
            self.speed = random.randint(1,4)
            self.rect.y = -100




        


rocket1=Player(300, 340 , 80,130,5)


enemys = []

for i in range(5):
    Enemy1= Enemy(random.randint(100,565), -100, 100, 50, random.randint(1,4), "ufo.png" )
    enemys.append(Enemy1)


font.init()

font1 = font.Font(None, 50)
font2= font.Font(None, 50)
Game = True
while Game:
    window.blit(background, (0, 0))
    rocket1.reset()
    Enemy1.reset()
    rocket1.move()
    Enemy1.move()
   
    window.blit(font1.render(f"Лічильник: {counter}", True, (255,255,255)), (15,10))
    window.blit(font2.render(f"Збито: {monster_kill}", True, (255,255,255)), (15,50))




    for i in enemys:
        i.reset()
        i.move()



    for b in bullets:
        b.reset()
        b.move()

    for e in event.get():
        if e.type == QUIT:
            Game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket1.fire()



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