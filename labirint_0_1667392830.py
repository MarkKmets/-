# Розроби свою гру в цьому файлі!
from pygame import *
white_blue=(210, 210, 255)
green=(0,255,0)
window=display.set_mode((700,500))
display.set_caption('Лабіринт')
play=True

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,width,height,name):
        super().__init__()
        self.image=transform.scale(image.load(name),(width,height))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
    def draw(self):

        window.blit(self.image,(self.x,self.y))
class Player(GameSprite):
    def __init__(self,x,y,width,height,x_speed,y_speed,name):
        GameSprite.__init__(self,x,y,width,height,name)
        self.x_speed=x_speed
        self.y_speed=y_speed
    def update(self):
        self.x+=self.x_speed
        self.y+=self.y_speed

        
ghost=Player(10,400,140,100,0,0,"ghost.png")
wall1=GameSprite(320,150,60,400,"wall1.png")
wall2=GameSprite(175,300,350,60,"wall2.png")
while play: 
    window.fill(white_blue)
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            play=False
        elif e.type==KEYDOWN:
            if e.key==K_LEFT:
                ghost.x_speed=-5
            elif e.key==K_RIGHT:
                ghost.x_speed=5
            elif e.key==K_UP:
                ghost.y_speed=-5
            elif e.key==K_DOWN:
                ghost.y_speed=5
        elif e.type==KEYUP:
            if e.key==K_LEFT:
                ghost.x_speed=0
            elif e.key==K_RIGHT:
                ghost.x_speed=0
            elif e.key==K_UP:
                ghost.y_speed=0
            elif e.key==K_DOWN:
                ghost.y_speed=0

    wall2.draw()
    wall1.draw()
    ghost.draw()

    ghost.update()


    display.update()
display.update()
