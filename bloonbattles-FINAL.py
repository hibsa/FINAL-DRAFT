# Hiba Hamad, hhamad
# Project Name: Bloon Battles

#importing all libraries
import math
import pygame
from pygame.locals import *
from pygame import mixer
from sys import exit 

#initiallizing pygame
pygame.init()

#initiallizing screen display, setting color to pink
screen = pygame.display.set_mode((890,735))
screen.fill('Pink')

#naming display screen, also name of the game, 'Bloon Battles'
pygame.display.set_caption('Bloon Battles')

#initiallizing clock
clock = pygame.time.Clock()

#loading map and game bar images
test_surface = pygame.image.load('graphics/game-map.png').convert_alpha()
game_bar = pygame.image.load('graphics/game-bar2.png').convert_alpha()

#loading main menu image
menuImg = pygame.transform.scale(
    pygame.image.load('graphics/menu.png').convert_alpha(),(900,750))

#loading balloon and popped balloon images
pinkBalloon = pygame.image.load('graphics/pinkballoon.png').convert_alpha()
blueBalloon = pygame.image.load('graphics/blueballoon.png').convert_alpha()
greenBalloon = pygame.image.load('graphics/greenballoon.png').convert_alpha()
yellowBalloon = pygame.image.load('graphics/yellowballoon.png').convert_alpha()
blackBalloon = pygame.image.load('graphics/itachii.png').convert_alpha()
airBalloon = pygame.transform.scale(
    pygame.image.load('graphics/airballoon.png').convert_alpha(),(70,96))
airBalloon2 = pygame.transform.scale(
    pygame.image.load('graphics/airballoon2.png').convert_alpha(),(70,96))
airBalloon3 = pygame.transform.scale(
    pygame.image.load('graphics/airballoon3.png').convert_alpha(),(70,96))
pop = pygame.image.load('graphics/popped-balloon.png').convert_alpha()

#Sound effects by https://picturetosound.com
#Youtube: https://www.youtube.com/c/picturetosound
popSound = pygame.mixer.Sound('graphics/pop-balloon.mp3')

#Sound Effect by: <a href="https://pixabay.com/users/modestas123123-7879278/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=125042">Modestas123123</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=125042">Pixabay</a>
cashSound = pygame.mixer.Sound('graphics/cash.mp3')

#initiallizing mixer
mixer.init()

#Music source: https://soundcloud.com/valen-go-568536229/bloons-td-battles-music
music = pygame.mixer.music.load('graphics/battle-music.mp3')

#plays background music 
pygame.mixer.music.play(-1)

#setting initial health to 20
healthBar = 20
#setting initial money to 300
currentMoney = 300
#setting initial window screen to menu
window = 'menu'

#initiallizing variables for resetting the game
restart = False
timePassed = 0
currentTimeReset = False

#creates returm menu 
#font from: https://www.dafont.com/hug-me-tight.font
returnMenu = pygame.font.Font('graphics/font.ttf', 15).render(
        ' MAIN MENU ', True, 'white','dark green')

returnMenuRect = returnMenu.get_rect(topleft=(38,640))


## Creates Balloon instances for 10 rounds
class Rounds():
    def __init__(self):

        self.currentTime = 0
        self.timer = 0
        self.release = False
        self.counting = False

        #frequency at which balloons are released
        self.frequency = 800

        self.pink = 0
        self.blue = 0
        self.green = 0
        self.yellow = 0
        self.black = 0
        self.air = 0

        
        balloonGroup.empty()

    #releases 20 pink balloons, slow speed
    def round1(self):

        if self.release and self.pink<20:
            balloonGroup.add(Balloon(0))
            self.release = False
            self.pink += 1

    #releases 10 pink balloons, 15 blue balloons, then 20 pink balloons
    #slow speed
    def round2(self):

        if self.release and self.pink<10:

            balloonGroup.add(Balloon(0))
            self.release = False
            self.pink += 1

        if self.release and self.blue<15:

            balloonGroup.add(Balloon(1))
            self.release = False
            self.blue += 1

        if self.release and self.pink<20:

            balloonGroup.add(Balloon(0))
            self.release = False
            self.pink += 1

    #releases 30 blue balloons, fast speed
    def round3(self):

        self.frequency = 400

        if self.release and self.blue<30:

            balloonGroup.add(Balloon(1))
            self.release = False
            self.blue += 1

    #releases 10 blue balloons then 10 green balloons, fast speed
    def round4(self):

        self.frequency = 400

        if self.release and self.blue<10:

            balloonGroup.add(Balloon(1))
            self.release = False
            self.blue += 1

        if self.release and self.green<10:

            balloonGroup.add(Balloon(2))
            self.release = False
            self.green += 1

    #releases 10 blue balloons then 30 green balloons, medium speed
    def round5(self):

        self.frequency = 600

        if self.release and self.blue<10:

            balloonGroup.add(Balloon(1))
            self.release = False
            self.blue += 1

        if self.release and self.green<30:

            balloonGroup.add(Balloon(2))
            self.release = False
            self.green += 1

    #releases 4 yellow balloons, then 15 green balloons, then 10 blue balloons
    #fast speed
    def round6(self):

        self.frequency = 400

        if self.release and self.yellow<4:

            balloonGroup.add(Balloon(3))
            self.release = False
            self.yellow += 1

        if self.release and self.green<15:

            balloonGroup.add(Balloon(2))
            self.release = False
            self.green += 1

        if self.release and self.blue<10:

            balloonGroup.add(Balloon(1))
            self.release = False
            self.blue += 1

    #releases 10 yellow balloons, slow speed
    def round7(self):

        self.frequency = 800

        if self.release and self.yellow<10:

            balloonGroup.add(Balloon(3))
            self.release = False
            self.yellow += 1

    #releases 20 black balloons, then 10 green balloons, slow speed
    def round8(self):

        self.frequency = 800

        if self.release and self.black<20:

            balloonGroup.add(Balloon(4))
            self.release = False
            self.black += 1

        if self.release and self.green<10:

            balloonGroup.add(Balloon(2))
            self.release = False
            self.green += 1

    #releases 10 yellow balloons, then 30 black balloons, fast speed
    def round9(self):

        self.frequency = 400

        if self.release and self.yellow<10:

            balloonGroup.add(Balloon(3))
            self.release = False
            self.yellow += 1

        if self.release and self.black<30:

            balloonGroup.add(Balloon(4))
            self.release = False
            self.black += 1

    #releases 2 black balloons, then an air balloons, slow speed
    def round10(self):

        self.frequency = 800

        if self.release and self.black<2:

            balloonGroup.add(Balloon(4))
            self.release = False
            self.black += 1

        if self.release and self.air<1:

            balloonGroup.add(Balloon(20))
            self.release = False
            self.air += 1

    #keeps track of how often balloons are sent out (speed)
    def updateBalloonTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.release == False and self.counting:
            self.counting = False
            self.timer = pygame.time.get_ticks()

        if self.currentTime - self.timer > self.frequency:
            self.release = True
            self.counting = True


# Displays a balloon
# When put in while loop, balloon moves to the end of the map
class Balloon(pygame.sprite.Sprite):
    def __init__(self,balloonColor,cord=(150,110)):

        #initiallizing sprite class
        super().__init__()

        #initiallizing variables
        self.x = cord[0]
        self.y = cord[1]

        self.balloonColor = balloonColor

        #assigns each number to a balloon color/image
        if self.balloonColor==0:
            self.image = pinkBalloon
            self.speed = 1
        if self.balloonColor==1:
            self.image = blueBalloon
            self.speed = 1.5
        if self.balloonColor==2:
            self.image = greenBalloon
            self.speed = 2
        if self.balloonColor==3:
            self.image = yellowBalloon
            self.speed = 2.5
        if self.balloonColor==4:
            self.image = blackBalloon
            self.speed = 1.5

        if self.balloonColor>15:
            self.image = airBalloon
            self.speed = 2

        elif self.balloonColor>9:
            self.image = airBalloon2
            self.speed = 1.5

        elif self.balloonColor>4:
            self.image = airBalloon3
            self.speed = 1

        #creating rectangle of current balloon image
        self.rect = self.image.get_rect(center=(self.x,self.y))

    #updates color/image of balloon regularly in main loop
    def updateColor(self):

        if self.balloonColor==0:
            self.image = pinkBalloon
            self.speed = 1
        if self.balloonColor==1:
            self.image = blueBalloon
            self.speed = 1.5
        if self.balloonColor==2:
            self.image = greenBalloon
            self.speed = 2
        if self.balloonColor==3:
            self.image = yellowBalloon
            self.speed = 2.5
        if self.balloonColor==4:
            self.image = blackBalloon
            self.speed = 1.5

        if self.balloonColor>15:
            self.image = airBalloon
            self.speed = 1.5

        elif self.balloonColor>9:
            self.image = airBalloon2
            self.speed = 1

        elif self.balloonColor>4:
            self.image = airBalloon3
            self.speed = 0.5    
        
    #moves balloon at a given speed when in main loop
    def update(self):
        global healthBar

        self.rect = self.image.get_rect(center=(self.x,self.y))

        if self.x<510:
            self.x += self.speed
            
        if self.x>=509 and self.y<280:
            self.y += self.speed
        
        if self.y>=279 and self.x<660:
            self.x += self.speed
            
        if self.x>=659 and self.y<800:
            self.y += self.speed

        if self.rect.top>735:
            healthBar -= (1 + self.balloonColor)
            self.kill()

    #returns true if balloon is colliding with given item,
    #otherwise, returns false
    def isColliding(self,item):

        if self.rect.colliderect(item):
            return True

        return False

    #returns current center position of balloon
    def balloonPos(self):

        return (self.rect.centerx,self.rect.centery)

    #returns the current color of a balloon
    def getColor(self):

        return self.balloonColor

    #change the color of a balloon
    def changeColor(self,balloon,color):

        self.balloonColor = color

                   
#Displays spikes on screen
#User can move spikes (only once) to the balloon path in the map
#Each bundle of spikes pops 6 balloons
class Spikes(pygame.sprite.Sprite):
    #initiallizes all variables, loads spikes images,
    #calls functions to display spikes on screen
    def __init__(self):

        #initiallizing sprite class
        super().__init__()

        #initiallizing variables
        self.count = 0
        self.spikesDamage = 0
        currentX = 0
        currentY = 0

        #initiallizing movement variables
        self.moving = False
        self.placed = False
        self.spikesCord = (80,470)

        #loading images of spikes
        self.spikesImg1 = pygame.image.load('graphics/spikes1.png').convert_alpha()
        self.spikesImg1 = pygame.transform.scale(self.spikesImg1,(55,50))
        
        self.spikesImg2 = pygame.image.load('graphics/spikes2.png').convert_alpha()
        self.spikesImg2 = pygame.transform.scale(self.spikesImg2,(55,50))
        
        self.spikesImg3 = pygame.image.load('graphics/spikes3.png').convert_alpha()
        self.spikesImg3 = pygame.transform.scale(self.spikesImg3,(55,50))

        #creating rect for spikes image
        self.rect = self.spikesImg1.get_rect(center=self.spikesCord)

    #displays spikes images on screen
    def update(self):
        
        #updates image of spikes displayed on screen
        #spikes appear to be less for every two balloons popped
        if self.spikesDamage==0 or self.spikesDamage==1:
            self.image = self.spikesImg1
            self.rect = self.image.get_rect(center=self.spikesCord)
        if self.spikesDamage==2 or self.spikesDamage==3:
            self.image = self.spikesImg2
            self.rect = self.image.get_rect(center=self.spikesCord)
        if self.spikesDamage>=4:
            self.image = self.spikesImg3
            self.rect = self.image.get_rect(center=self.spikesCord)

        #displays spikes on screen if they are still active
        #spikes are active if they've popped less than 6 balloons
        if self.spikesDamage!=6:
            screen.blit(self.image,self.rect)

        if len(spikesGroup)!=3:
            screen.blit((pygame.font.Font(None,30)).render(
            str(4-len(spikesGroup)), False, 'light green'),(73,505))

    #returns true is balloon is colliding with spikes
    #otherwise returns false
    def popBalloon(self,balloon):
        
        if balloon.isColliding(self.rect) and (
            self.spikesDamage<6 and not self.moving):
            self.spikesDamage += 1
            return True

        return False

    # source: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def moveSpikes(self,event,spikes):
        
        if event.type == pygame.MOUSEBUTTONDOWN and len(spikesGroup)>0:
            if self.rect.collidepoint(event.pos):
                self.moving = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving:
            if not collidePath(self.rect.centerx,self.rect.centery):
                spikesGroup.remove(spikes)
            self.moving = False
            self.placed = True
            if len(spikesGroup) < 3:
                spikesGroup.add(Spikes())

        elif event.type == pygame.MOUSEMOTION:
            if self.moving==True and self.placed==False:
                self.spikesCord = event.pos

#Displays character, Bibbo, on screen
#User can drag Bibbo on screen
#Bibbo shoots feather darts to pop balloons
class Bibbo(pygame.sprite.Sprite):

    def __init__(self,cord):

        #initiallizing sprite class
        super().__init__()

        #loading Bibbo image, creating rect for image
        self.default_bird = pygame.image.load('graphics/bibbo.png').convert_alpha()
        self.default_bird = pygame.transform.rotate(self.default_bird, 180)
        self.rect = self.default_bird.get_rect(center=cord)

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-100,self.rect.top-100)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+100,self.rect.bottom+100)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)
        

        #bibbo's initial angle rotation is 0
        self.angle = 0

        #initiallizing variables for angle of player
        self.quad = None
        self.angleTaken = False

        #initiallizing variable for shooting status of bibbo
        self.canShoot = True
        self.frequency = 1000

        #initiallizing variables for tracking time
        self.currentTime = 0
        self.dartTime = 0
        self.counting = True

        #initiallizing variables to move bibbo
        self.moving = False
        self.placed = False
        self.showUpgrade = False
        self.showDesc = False
        self.upgradeComplete = False

    #if given balloon is colliding with bibbo's range,
    #gets angle bibbo needs to rotate at to face the balloon,
    #also calls function to shoot at balloon
    def getAngleCallShoot(self,balloon,bibbo):

        #saving current balloon's center position
        self.balloonPos = balloon.balloonPos()

        #checks if balloon is colliding with bibbo's range
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and (
                self.balloonPos[1]<self.rangeFin[1]):
                #calculating angle using arc tangent 
                self.diffX = self.rangeMid[0]-self.balloonPos[0]
                self.diffY = self.rangeMid[1]-self.balloonPos[1]
                if self.diffY==0:
                    self.angleTemp = 0
                else: self.angleTemp = abs(math.degrees(math.atan(
                                                self.diffX/self.diffY)))
                #calls functions to change angle according to..
                #quadrant of the balloon collision
                self.checkQuad()
                #if shooting is valid,
                #calls function to shoot a dart at the balloon,
                #saves dart to a group
                if self.canShoot and self.placed:
                    self.dartAngle = self.angle
                    dartGroup.add(bibbo.createDart(balloon,
                            self.dartAngle,self.balloonPos[0],self.balloonPos[1]))

    #changes the angle depending on which quadrant...
    #..the balloon is colliding with bibbo's range
    def checkQuad(self):

        quad00 = self.rangeStr
        quad01 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeStr[1])
        quad02 = (self.rangeFin[0],self.rangeStr[1])

        quad10 = (self.rangeStr[0],(self.rangeStr[1]+self.rangeFin[1])//2)
        quad11 = ((self.rangeStr[0]+self.rangeFin[0])//2,
                  (self.rangeStr[1]+self.rangeFin[1])//2)
        quad12 = (self.rangeFin[0],(self.rangeStr[1]+self.rangeFin[1])//2)

        quad20 = (self.rangeStr[0],self.rangeFin[1])
        quad21 = ((self.rangeStr[0]+self.rangeFin[0])//2,self.rangeFin[1])
        quad22 = self.rangeFin

        #hold balloon's center position
        x = self.balloonPos[0]
        y = self.balloonPos[1]

        if y>quad00[1] and y<quad10[1]:
            #quad 1
            if x>quad01[0] and x<quad02[0]:
                self.quad = 1
                self.angle = -self.angleTemp

            #quad 2
            elif x>quad00[0] and x<quad01[0]:
                self.quad = 2
                self.angle = self.angleTemp

        elif y>quad10[1] and y<quad20[1]:

            #quad 3
            if x>quad00[0] and x<quad01[0]:
                self.quad = 3
                self.angle = 180 - self.angleTemp

            #quad 4
            elif x>quad01[0] and x<quad02[0]:
                self.quad = 4
                self.angle = 180 + self.angleTemp

    # source: https://www.youtube.com/watch?v=_TU6BEyBieE
    #diplays image of bibbo on screen
    #and rotates according to balloon collisions
    #and updates bibbo's range
    def blitRotateUpdateRange(self):

        #top left of bibbo's range
        self.rangeStr = (self.rect.left-100,self.rect.top-100)
        #bottom right of bibbo's range
        self.rangeFin = (self.rect.right+100,self.rect.bottom+100)
        #middle of bibbo's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        if not self.moving:
            self.img = pygame.transform.rotate(self.default_bird,self.angle)
                
        screen.blit(self.img,(self.rect.centerx-int(self.img.get_width()/2),
                              self.rect.centery-int(self.img.get_height()/2)))
        if currentMoney>=200:
            color = "light green"
        else: color = "red"
        screen.blit((pygame.font.Font(None,25)).render(
        '$200', False, color),(59,395))

        if currentMoney>=150:
            upColor = "light green"
        else: upColor = "red"
        
        if self.showUpgrade and not self.upgradeComplete:
            screen.blit(pygame.font.Font('graphics/font.ttf', 15).render(
        'upgrade: $150', True, upColor,'dark green'),self.rect)

        if self.showDesc:
            #font from: https://www.dafont.com/hug-me-tight.font
            displayText(screen," BIBBO \n Ability: shoots feathers that pop two balloons"+
            " \n Accuracy: not so good, he's a little blind \n"+
            ' Upgrade: shoots darts faster \n Range: medium',
            (115,340),pygame.font.Font('graphics/font.ttf', 15),'light green','dark green')


    #creates a dart that shoots at given balloon at given angle
    def createDart(self,balloon,angle,balloonX,balloonY):

        self.canShoot = False

        return Darts(angle,self.quad,balloon,self.rangeMid[0],self.rangeMid[1],
                        balloonX,balloonY)

    #restricts bibbo to only shoot one dart per second
    def updateDartTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > self.frequency:
            self.counting = True
            self.canShoot = True

    # referenced and edited from: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor
    #shows description of character in menu when mouse hovers over
    #shows update if it has not been updates already
    #when clicked, if bibbo has not been updated, he is updated to shoot faster
    def moveBibbo(self,event,bibbo):
        global currentMoney
        
        if event.type == pygame.MOUSEBUTTONDOWN and currentMoney>=150 and (
            window!='menu') and window!='over':
            if self.rect.collidepoint(event.pos) and currentMoney>=200:
                self.moving = True
                if self.placed and not self.upgradeComplete:
                    cashSound.play()
                    self.frequency = 1000
                    currentMoney -= 150
                    self.upgradeComplete = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving:
            if collideMany(self.rect.centerx,self.rect.centery):
                bibboGroup.remove(bibbo)
                
            if not self.placed and not collideMany(
                self.rect.centerx,self.rect.centery):
                currentMoney -= 200
                cashSound.play()
                
            self.placed = True
            self.moving = False
            
            bibboGroup.add(Bibbo((80,360)))

        elif event.type == pygame.MOUSEMOTION:
            self.showDesc = False
            if self.moving==True and self.placed==False:
                self.rect.center = event.pos
                
            if not self.moving and not self.placed and (
                self.rect.collidepoint(event.pos)):
                self.showDesc = True
                
            if self.placed and self.rect.collidepoint(event.pos):
                self.showUpgrade = True
                
            else: self.showUpgrade = False
            

## character polly shoots at all directions when placed
class Polly(pygame.sprite.Sprite):
    def __init__(self):
    
        #initiallizing sprite class
        super().__init__()

        self.image = pygame.image.load('graphics/polly.png').convert_alpha()
        self.rect = self.image.get_rect(center=(78,263))

        #top left of polly's range
        self.rangeStr = (self.rect.left-50,self.rect.top-50)
        #bottom right of polly's range
        self.rangeFin = (self.rect.right+50,self.rect.bottom+50)
        #middle of polly's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        #initiallizing variable for shooting status of polly
        self.canShoot = True

        #initiallizing variables for tracking time
        self.currentTime = 0
        self.dartTime = 0
        self.counting = True
        self.frequency = 1500

        #initiallizing variables to move polly
        self.moving = False
        self.placed = False
        self.showUpgrade = False
        self.showDesc = False
        self.upgradeComplete = False

    def blitUpdateRange(self):

        #top left of polly's range
        self.rangeStr = (self.rect.left-50,self.rect.top-50)
        #bottom right of polly's range
        self.rangeFin = (self.rect.right+50,self.rect.bottom+50)
        #middle of polly's range
        self.rangeMid = ((self.rangeStr[0]+self.rangeFin[0])/2,
                         (self.rangeStr[1]+self.rangeFin[1])/2)

        screen.blit(self.image,(self.rect.centerx-int(self.image.get_width()/2),
                              self.rect.centery-int(self.image.get_height()/2)))
        #displays cost of polly
        if currentMoney>=150:
            color = "light green"
        else: color = "red"
        #font from: https://www.dafont.com/hug-me-tight.font
        screen.blit(pygame.font.SysFont('graphics/font.ttf', 25).render(
        '$150', False, color),(59,297))

        #displays cost of polly's upgrade
        if currentMoney>=200:
            upColor = "light green"
        else: upColor = "red"
        #font from: https://www.dafont.com/hug-me-tight.font
        if self.showUpgrade and not self.upgradeComplete:
            screen.blit(pygame.font.Font('graphics/font.ttf', 15).render(
        'upgrade: $200', True, upColor,'dark green'),self.rect)

        #displays polly's description
        #font from: https://www.dafont.com/hug-me-tight.font
        if self.showDesc:
            displayText(screen," POLLY \n Ability: shoots pollen at all "+
            "directions to pop balloons \n"+
            ' Upgrade: shoots pollen faster \n Range: bad ',
            (115,240),pygame.font.Font('graphics/font.ttf', 15),'light green','dark green')
            

    #when called polly shoots pollen at all directions
    #each pollen pops one balloon
    def callShoot(self,balloon):

        #saving current balloon's center position
        self.balloonPos = balloon.balloonPos()

        #checks if balloon is colliding with bibbo's range
        if self.balloonPos[0]>self.rangeStr[0] and self.balloonPos[0]<self.rangeFin[0]:
            if self.balloonPos[1]>self.rangeStr[1] and (
                self.balloonPos[1]<self.rangeFin[1]):
                if self.canShoot and not self.moving:
                    self.canShoot = False
                    self.allSides = [(0,-1),(0,1),(1,0),(-1,0),
                                     (1,1),(-1,-1),(1,-1),(-1,1)]
                    for increase in self.allSides:
                        pollenGroup.add(Pollen(balloon,self.rect.center,increase))

    #restricts polly to only one pollen attack per second
    def updatePollenTime(self):

        self.currentTime = pygame.time.get_ticks()

        if self.canShoot == False and self.counting == True:
            self.counting = False
            self.dartTime = pygame.time.get_ticks()

        elif self.currentTime - self.dartTime > self.frequency:
            self.counting = True
            self.canShoot = True

    # referenced and edited from: https://pygame.readthedocs.io/en/latest/3_image/image.html
    #moves an image, which user holds mouse button on, alongside cursor 
    def movePolly(self,event,polly):
        global currentMoney
        
        if event.type == pygame.MOUSEBUTTONDOWN and (
            window!='menu') and window!='over':
            if self.rect.collidepoint(event.pos) and currentMoney>=150:
                self.moving = True
                if self.placed and currentMoney>=200 and not self.upgradeComplete:
                    cashSound.play()
                    self.frequency = 1000
                    currentMoney -= 200
                    self.upgradeComplete = True
                
        elif event.type == pygame.MOUSEBUTTONUP and self.moving: 
            if collideMany(self.rect.centerx,self.rect.centery):
                pollyGroup.remove(polly)
                
            if not self.placed and not collideMany(
                    self.rect.centerx,self.rect.centery):
                currentMoney -= 150
                cashSound.play()
                
            self.placed = True
            self.moving = False
            pollyGroup.add(Polly())

        elif event.type == pygame.MOUSEMOTION:
            self.showDesc = False
            if self.moving==True and self.placed==False:
                self.rect.center = event.pos

            if not self.moving and not self.placed and (
                self.rect.collidepoint(event.pos)):
                self.showDesc = True
                
            if self.placed and self.rect.collidepoint(event.pos):
                self.showUpgrade = True
                
            else: self.showUpgrade = False

class Pollen(pygame.sprite.Sprite):
    def __init__(self,balloon,cord,incXY):
    
        #initiallizing sprite class
        super().__init__()

        self.image = pygame.image.load('graphics/pollen.png').convert_alpha()
        self.rect = self.image.get_rect(center=cord)

        self.incX = incXY[0]
        self.incY = incXY[1]

        self.numPopped = 0
        self.distance = 0

    def update(self):

        self.distance += 1
        self.rect.centerx += self.incX
        self.rect.centery += self.incY

        if self.distance>50:
            self.kill()

    #kills pollen if it has popped 1 balloon
    #returns True if balloon collides with pollen
    #otherwise returns False
    def popBalloon(self,balloon,pollen):

        if pygame.sprite.collide_mask(balloon,pollen) and self.numPopped<1:
            self.numPopped += 1
            return True

        if self.numPopped >= 1:
            self.kill()

        return False
        
        

#Creates a dart that shoots at given balloon
#Dart pops balloons at collision
class Darts(pygame.sprite.Sprite):
    def __init__(self,angle,quad,balloon,x1,y1,x2,y2):
        
        #initiallizing sprite class
        super().__init__()

        #loading images and change angle according to direction of balloon
        self.feather_dart = pygame.image.load('graphics/feather.png').convert_alpha()
        self.feather_dart = pygame.transform.rotate(self.feather_dart, 180)

        #self.angle = math.degrees(math.atan((y2-y1)/(x2-x1)))
        self.image = pygame.transform.rotate(self.feather_dart, angle)

        #initiallizing variables that hold dart and balloon position
        self.x1 = x1
        self.y1 = y1
        
        self.originalX = x1
        self.originalY = y1

        self.angle = angle

        #initiallizing variables for dart angle and position
        self.quad = quad

        #initializing variable to track number of balloons dart pops
        self.numPopped = 0

        #making a rect of the dart
        self.rect = self.image.get_rect(center=(self.x1,self.y1))

    #updates position of dart
    def update(self):
        
        if self.quad == 1:
            if self.angle==0:
                self.y1 += 0
                self.x1 += 3
            else:
                self.y1 += math.sin(math.radians(self.angle))*3
                self.x1 += math.cos(math.radians(self.angle))*3
        if self.quad == 2:
            if self.angle==0:
                self.y1 -= 3
                self.x1 -= 0
            else:
                self.y1 -= math.sin(math.radians(self.angle))*3
                self.x1 -= math.cos(math.radians(self.angle))*3
            #print(self.m)
        if self.quad == 3:
            if self.angle==0:
                self.y1 -= 0
                self.x1 += 3
            else:
                self.y1 -= math.sin(math.radians(self.angle))*3
                self.x1 += math.cos(math.radians(self.angle))*3
        if self.quad == 4:
            if self.angle==0:
                self.y1 -= 0
                self.x1 -= 3
            else:
                self.y1 -= math.sin(math.radians(self.angle))*3
                self.x1 -= math.cos(math.radians(self.angle))*3

        self.rect = self.image.get_rect(center=(self.x1,self.y1))

        #kills dart if it passes the map borders
        if self.rect.x>1000 or self.rect.y>1000:
            self.kill()

        if abs(self.originalX-self.x1) > 100:
            self.kill()

        if abs(self.originalY-self.y1) > 100:
            self.kill()

    #kills dart if it has popped 2 balloons
    #returns True if balloon collides with dart
    #otherwise returns False
    def popBalloon(self,balloon):

        if balloon.isColliding(self.rect) and self.numPopped<2:
            self.numPopped += 1
            return True

        if self.numPopped >= 2:
            self.kill()

        return False

#returns true if an object collides with the path
def collidePath(posX,posY):

    if posX>150 and posY>90 and posX<550 and posY<150:
        return True
    if posX>480 and posY>100 and posX<550 and posY<320:
        return True
    if posX>550 and posY>240 and posX<690 and posY<320:
        return True
    if posX>620 and posY>320 and posX<690 and posY<740:
        return True

    return False

#returns true if an object collides with the game bar
def collideGameBar(posX,posY):

    if posX>0 and posY>0 and posX<180:
        return True
    
    return False

def collideWater(posX,posY):

    if posX>0 and posY>180 and posX<340:
        return True

    return False

def collideMany(x,y):

    if collideGameBar(x,y) or collidePath(x,y) or collideWater(x,y):
        return True

    return False

#taken from https://github.com/pickry/programmingknowledge for
#splitting words in lines
def displayText(surface,text,pos,font,color,background):
   collection= [word.split('\n') for word in text.splitlines()]
   space=font.size(' ')[0]
   x,y=pos
   for lines in collection:
       for words in lines:
           word_surface=font.render(words,True,color,background)
           wordW,wordH=word_surface.get_size()
           if x+wordW>=600:
               x=pos[0]
               y+=wordH
           surface.blit(word_surface,(x,y))
           x+=wordW+space
       x=pos[0]
       y+=wordH
       

    

#creates spikes group for Spikes instance
spikesGroup = pygame.sprite.Group()
spikesGroup.add(Spikes())

#creates a player group for Bibbo instance
bibboGroup = pygame.sprite.Group()
bibboGroup.add(Bibbo((80,360)))

#creates dart group
dartGroup = pygame.sprite.Group()

#creates a player group for Polly instance
pollyGroup = pygame.sprite.Group()
pollyGroup.add(Polly())

#creates group for polly's pollen attacks
pollenGroup = pygame.sprite.Group()

updateMoneyTime = 0

#creates balloon group containing all balloons
balloonGroup = pygame.sprite.Group()

round1Ins = Rounds()
round2Ins = Rounds()
round3Ins = Rounds()
round4Ins = Rounds()
round5Ins = Rounds()
round6Ins = Rounds()
round7Ins = Rounds()
round8Ins = Rounds()
round9Ins = Rounds()
round10Ins = Rounds()

def resetGame():
    global healthBar, restart, currentTime, currentMoney,round1Ins,round2Ins,round3Ins
    global round4Ins,round5Ins,round6Ins,round7Ins, round8Ins, currentTimeReset
    global balloonGroup
    
    healthBar = 20
    bibboGroup.empty()
    bibboGroup.add(Bibbo((80,360)))
    pollyGroup.empty()
    pollyGroup.add(Polly())
    dartGroup.empty()
    pollenGroup.empty()
    spikesGroup.empty()
    spikesGroup.add(Spikes())
    balloonGroup.empty()
    balloonGroup = pygame.sprite.Group()

    restart = True
    currentTime = 0
    currentMoney = 300
    #print(round1Ins.round2
    round1Ins = Rounds()
    round2Ins = Rounds()
    round3Ins = Rounds()
    round4Ins = Rounds()
    round5Ins = Rounds()
    round6Ins = Rounds()
    round7Ins = Rounds()
    round8Ins = Rounds()
    round9Ins = Rounds()
    round10Ins = Rounds()

    currentTimeReset = False

#displays balloons of each round
#returns current round number and instance in a tuple
def displayBalloonRounds(mode,currentTime):
    global window

    currentRound = 0

    ## EASY DIFFICULTY: 5 rounds
    if mode==1:
        #displays round 1 balloons
        if currentTime>4:
            round1Ins.round1()
            round1Ins.updateBalloonTime()
            currentRound = 1

        #displays round 2 balloons
        if currentTime>30:
            round2Ins.round2()
            round2Ins.updateBalloonTime()
            currentRound = 2

        #displays round 3 balloons
        if currentTime>60:
            round3Ins.round3()
            round3Ins.updateBalloonTime()
            currentRound = 3

        #displays round 4 balloons
        if currentTime>90:
            round4Ins.round4()
            round4Ins.updateBalloonTime()
            currentRound = 4

        #displays round 5 balloons
        if currentTime>120:
            round5Ins.round5()
            round5Ins.updateBalloonTime()
            currentRound = 5

        if currentTime>150:
            window = 'victory'
            return

    ## MEDIUM DIFFICULTY: 6 rounds
    if mode==2:
        #displays round 1 balloons
        if currentTime>4:
            round3Ins.round3()
            round3Ins.updateBalloonTime()
            currentRound = 1

        #displays round 2 balloons
        if currentTime>30:
            round4Ins.round4()
            round4Ins.updateBalloonTime()
            currentRound = 2

        #displays round 3 balloons
        if currentTime>60:
            round5Ins.round5()
            round5Ins.updateBalloonTime()
            currentRound = 3

        #displays round 4 balloons
        if currentTime>90:
            round6Ins.round6()
            round6Ins.updateBalloonTime()
            currentRound = 4

        #displays round 5 balloons
        if currentTime>120:
            round7Ins.round7()
            round7Ins.updateBalloonTime()
            currentRound = 5

        #displays round 6 balloons
        if currentTime>150:
            round8Ins.round8()
            round8Ins.updateBalloonTime()
            currentRound = 6

        if currentTime>180:
            window = 'victory'
            return

    ## HARD DIFFICULTY: 6 rounds
    if mode==3:
        #displays round 1 balloons
        if currentTime>4:
            round5Ins.round5()
            round5Ins.updateBalloonTime()
            currentRound = 1

        #displays round 2 balloons
        if currentTime>30:
            round6Ins.round6()
            round6Ins.updateBalloonTime()
            currentRound = 2

        #displays round 3 balloons
        if currentTime>60:
            round7Ins.round7()
            round7Ins.updateBalloonTime()
            currentRound = 3

        #displays round 4 balloons
        if currentTime>90:
            round8Ins.round8()
            round8Ins.updateBalloonTime()
            currentRound = 4

        #displays round 5 balloons
        if currentTime>120:
            round9Ins.round9()
            round9Ins.updateBalloonTime()
            currentRound = 5

        #displays round 6 balloons
        if currentTime>150:
            round10Ins.round10()
            round10Ins.updateBalloonTime()
            currentRound = 6

        if currentTime>180:
            window = 'victory'
            return

    return currentRound

def popBalloon(balloon):

    color = round(balloon.getColor())

    if color==0:
        balloonGroup.remove(balloon)
        screen.blit(pop,balloon)
    if color==4:
        balloon.changeColor(balloon,3)
        balloonGroup.add(Balloon(3,balloon.balloonPos()))
    if color==5:
        balloon.changeColor(balloon,4)
        balloonGroup.add(Balloon(4,balloon.balloonPos()))
        balloonGroup.add(Balloon(3,balloon.balloonPos()))
        balloonGroup.add(Balloon(4,balloon.balloonPos()))
        balloonGroup.add(Balloon(3,balloon.balloonPos()))
        balloonGroup.add(Balloon(4,balloon.balloonPos()))
    else:
        balloon.changeColor(balloon,color-1)

    popSound.play()

# displays everything on game window
def drawPlayWindow(mode,event=None):    
    global healthBar,currentMoney,updateMoneyTime,restart,timePassed,currentTimeReset
    
    screen.blit(test_surface,(0,0)) #displays map

    totalTime = pygame.time.get_ticks()

    currentTime = totalTime - timePassed
    
    roundNum = displayBalloonRounds(mode,currentTime//1000)

    if not currentTimeReset:
        currentTime = 0
        currentTimeReset = True
    
    if restart:
        timePassed = totalTime #tracks time in seconds
        restart = False
        roundNum = displayBalloonRounds(mode,currentTime//1000)
        spikesGroup.add(Spikes())

    if totalTime - updateMoneyTime > 10000:
        updateMoneyTime = pygame.time.get_ticks()
        currentMoney += 50

    if healthBar>0:
        balloonGroup.draw(screen)
        balloonGroup.update()

    for dart in dartGroup:
        dartGroup.draw(screen) #displays darts

    dartGroup.update() #updates darts' positions
        
    screen.blit(game_bar,(0,0)) #displays game bar on left

    spikesGroup.update() #updates spikes bundle image

    for bibbo in bibboGroup:
        #updates frequency at which bibbo can shoot darts
        bibbo.updateDartTime() 
        bibbo.blitRotateUpdateRange() #rotates bibbo to face balloons

    pollenGroup.draw(screen)
    pollenGroup.update()

    for polly in pollyGroup:
        polly.blitUpdateRange()
        polly.updatePollenTime()

    #checks if rounds started
    #calls functions to pop balloons or not
    for balloon in balloonGroup:
        
        balloon.updateColor()
        
        for bibbo in bibboGroup:
            bibbo.getAngleCallShoot(balloon,bibbo)

        for spikes in spikesGroup:
            if spikes.popBalloon(balloon):
                popBalloon(balloon)
                
        for dart in dartGroup:
            if dart.popBalloon(balloon):
                popBalloon(balloon)

        for pollen in pollenGroup:
            if pollen.popBalloon(balloon,pollen):
                popBalloon(balloon)

        for polly in pollyGroup:
            polly.callShoot(balloon)

    #displays current round number
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 25).render(
        'ROUND: '+ str(roundNum), True, 'white'),(25,26))
    #displays current health of player
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 25).render(
        'HEALTH: '+ str(healthBar), False, 'white'),(25,45))
    #displays current money
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 25).render(
        'BANK: $'+ str(currentMoney), False, 'white'),(25,63))

    screen.blit(returnMenu,returnMenuRect)

def goToMenu(event):
    global window

    if event.type == MOUSEBUTTONDOWN and window != 'menu' and window != 'victory':
        if returnMenuRect.collidepoint(event.pos):
            resetGame()
            window = 'menu'


#displays GAME OVER window
def gameOverWind():

    screen.blit(test_surface,(0,0)) #display map

    #displays words 'GAME OVER'
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 150).render(
        'GAME OVER', False, 'red'),(200,300))

    #displays words 'click to start over'
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 30).render(
        'click to start over', False, 'red'),(400,400))

def victoryWind():

    screen.blit(test_surface,(0,0)) #display map

    #displays words 'VICTORY'
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 150).render(
        'VICTORY', False, 'green'),(200,300))

    #displays words 'click to start over'
    #font from: https://www.dafont.com/hug-me-tight.font
    screen.blit(pygame.font.SysFont('graphics/font.ttf', 30).render(
        'return to menu', True, 'white','green'),(400,400))

def drawMenuWind(event=None):
    global window

    screen.blit(menuImg,(0,0))

    #blit title
    #font from: https://www.dafont.com/hug-me-tight.font
    title = pygame.font.Font('graphics/font.ttf', 100).render(
        'BLOON BATTLES', False, 'white')

    titleRect = title.get_rect(topleft=(80,50))

    screen.blit(title,titleRect)

    #blit easy button
    #font from: https://www.dafont.com/hug-me-tight.font
    easyBut = pygame.font.Font('graphics/font.ttf', 80).render(
        'play easy', False, 'white')

    easyButRect = easyBut.get_rect(topleft=(80,200))

    screen.blit(easyBut,easyButRect)

    #blit medium button
    #font from: https://www.dafont.com/hug-me-tight.font
    medBut = pygame.font.Font('graphics/font.ttf', 80).render(
        'play medium', False, 'white')

    medButRect = medBut.get_rect(topleft=(80,300))

    screen.blit(medBut,medButRect)

    #blit hard button
    #font from: https://www.dafont.com/hug-me-tight.font
    hardBut = pygame.font.Font('graphics/font.ttf', 80).render(
        'play hard', False, 'white')

    hardButRect = hardBut.get_rect(topleft=(80,400))

    screen.blit(hardBut,hardButRect)

    if event != None:
        if event.type == pygame.MOUSEBUTTONDOWN and window == 'menu':
            if easyButRect.collidepoint(event.pos):
                resetGame()
                window = 'play easy'
            if medButRect.collidepoint(event.pos):
                resetGame()
                window = 'play med'
            if hardButRect.collidepoint(event.pos):
                resetGame()
                window = 'play hard'
    
#stores main loop of game
def main():
    global healthBar, restart, currentTime, currentMoney,window

    #infinite while loop 
    while True:
        #checking all events
        for event in pygame.event.get():

            #if players quits game, exit program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #if player clicks on screen in game over window,
            #game resets
            for bibbo in bibboGroup:
                bibbo.moveBibbo(event,bibbo)

            for spikes in spikesGroup:
                spikes.moveSpikes(event,spikes)

            for polly in pollyGroup:
                polly.movePolly(event,polly)                
                
            if event.type == pygame.MOUSEBUTTONDOWN and healthBar <= 0:#window=='over':
                resetGame()
                window = 'menu'

            if event.type == pygame.MOUSEBUTTONDOWN and window=='victory':
                resetGame()
                window = 'menu'

            if window == 'menu':
                drawMenuWind(event)

            goToMenu(event)

        if window == 'play easy':
            drawPlayWindow(1)
            
        if window == 'play med':
            drawPlayWindow(2)

        if window == 'play hard':
            drawPlayWindow(3)

        if window == 'victory':
            victoryWind()

        if window == 'menu':
            drawMenuWind()

        if healthBar <= 0:# and window != 'menu':
            #displays words 'GAME OVER'
            #font from: https://www.dafont.com/hug-me-tight.font
            screen.blit(pygame.font.SysFont('graphics/font.ttf', 150).render(
                'GAME OVER', False, 'red'),(200,300))

            #displays words 'click to start over'
            #font from: https://www.dafont.com/hug-me-tight.font
            screen.blit(pygame.font.SysFont('graphics/font.ttf', 30).render(
                'click to start over', False, 'red'),(400,400))
            #window = 'over'

        #updates display every loop        
        pygame.display.update()
        clock.tick(60) #makes while loop run 60 times per second

#calling main loop
main()







    

