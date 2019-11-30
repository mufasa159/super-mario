'''
Super Mario | Built with PyGame

This game is a combination of multiple mario games. Most things are similar to Super Mario Bros. However, the controls and the way to score points might be different.

Note: 
Use arrow keys to move Mario. 
Press > to move right
Press < to move  left
Press ^ to jump
In order to kill Goomba, you have to find the Fire-flower first. Once mario collides with the Fire-flower, Goomba will become invisible and then you may move to the next level. And watch out for that poisonous mushroom!

'''
# imports gamlib.py file
from gamelib import *

# creates a 800 x 600 window
game = Game(800,600,'Super Mario | Built with PyGame')

# imports the sprites and other images
mario = Image('images/mario.gif', game)
coin = Image('images/power_up/coin.png', game)
coin2 = Image('images/power_up/coin.png', game)
coin3 = Image('images/power_up/coin.png', game)
coin4 = Image('images/power_up/coin.png', game)
leaf = Image('images/power_up/super_leaf.png', game)
fireFlower = Image('images/power_up/fire_flower.png', game)
fireBall = Image('images/power_up/fireBall.png', game)
angryMush = Image('images/enemy/angry_mush.png', game)
poisonMush = Image('images/enemy/poison_mush.png', game)
heart1 = Image('images/heart.png', game)
heart2 = Image('images/heart.png', game)
heart3 = Image('images/heart.png', game)
heart4 = Image('images/heart.png', game)
background = Image('images/back.jpg', game)
bl_1 = Image('images/blocks/bl_1.png', game)
bl_2 = Image('images/blocks/bl_2.png', game)
bl_3 = Image('images/blocks/bl_3.png', game)
bl_4 = Image('images/blocks/bl_4.png', game)
bl_5 = Image('images/blocks/bl_5.png', game)
bl_6 = Image('images/blocks/bl_6.png', game)
pipe = Image('images/blocks/pipe.png', game)
bl_41 = Image('images/blocks/bl_1.png', game)
door = Image('images/door.png', game)

# resizes the object
mario.resizeTo(50,50)
coin.resizeTo(20,20)
coin2.resizeTo(20,20)
coin3.resizeTo(20,20)
coin4.resizeTo(20,20)
leaf.resizeTo(30,30)
fireFlower.resizeTo(40,40)
angryMush.resizeTo(25,25)
poisonMush.resizeTo(25,25)
background.resizeTo(800,600)
bl_1.resizeTo(40,40)
bl_2.resizeTo(40,40)
bl_3.resizeTo(40,40)
bl_4.resizeTo(40,40)
bl_5.resizeTo(40,40)
bl_6.resizeTo(40,40)
pipe.resizeTo(70,70)
bl_41.resizeTo(40,40)
heart1.resizeTo(30,30)
heart2.resizeTo(30,30)
heart3.resizeTo(30,30)
heart4.resizeTo(30,30)
fireBall.resizeTo(20,20)
door.resizeTo(20,70)

# Positioning the objects
mario.moveTo(10,510)
pipe.moveTo(540,485)
bl_1.moveTo(300,350)
bl_2.moveTo(340,350)
bl_4.moveTo(380,350)
bl_3.moveTo(420,350)
bl_5.moveTo(520,220)
bl_6.moveTo(560,220)
angryMush.moveTo(400,510)
bl_41.moveTo(480,220)
poisonMush.moveTo(600,512)
fireFlower.moveTo(380,350)
coin.moveTo(420,100)
coin2.moveTo(450,100)
coin3.moveTo(480,100)
coin4.moveTo(700,500)
heart1.moveTo(30,25)
heart2.moveTo(70,25)
heart3.moveTo(110,25)
heart4.moveTo(150,25)
fireBall.moveTo(0,0)
door.moveTo(796,490)

# sets moving speed and direction
mario.setSpeed(2,0)
angryMushSpeed = 4

#values
coinCount = 0
score = 0
timer = 0
minutes = 0
visible = 1

# creates a loop to keep the game playing until you lose
while not game.over:

  game.processInput()
  keys=pygame.key.get_pressed()

  # draws the objects on the screen
  background.draw()
  mario.draw()
  coin.draw()
  coin2.draw()
  coin3.draw()
  coin4.draw()
  fireFlower.draw()
  heart1.draw()
  heart2.draw()
  heart3.draw()
  heart4.draw()
  angryMush.draw()
  poisonMush.draw()
  bl_1.draw()
  bl_2.draw()
  bl_3.draw()
  bl_4.draw()
  bl_5.draw()
  bl_6.draw()
  pipe.draw()
  bl_41.draw()
  fireBall.draw()
  door.draw()

  # timer | I feel proud :)
  timer += 1
  sec = timer/20
  if (sec>59):
    timer = 0
    minutes +=1

  # key controls to move mario (right, left and jump)
  if (keys[K_RIGHT]):
    mario.moveX(+40)

  if (keys[K_LEFT]):
    mario.moveX(-40)

  if (keys[K_UP]):
    mario.moveY(-40)
  mario.moveY(15)
  if (mario.y > 500):
    mario.y = 500

  # keeps mario inside the window
  if (mario.x > 800 or mario.x<0):
    mario.x = 20
  if (mario.y>600 or mario.y<0):
    mario.y = 485

  # makes the object move
  angryMush.move(True)

  # limits Goomba's animation to a certain area
  angryMush.moveX(angryMushSpeed)
  if (angryMush.x>500 or angryMush.x<190):
    angryMushSpeed = -angryMushSpeed

  # collision of mario with enemies
  if (mario.collidedWith(angryMush) or mario.collidedWith(poisonMush)):
    mario.health -=20
    mario.moveTo(20,500)

  # collision of mario with coins
  if (mario.collidedWith(coin) or mario.collidedWith(coin2) or mario.collidedWith(coin3) or mario.collidedWith(coin4)):
    coinCount += 1
    score += 20
  if (mario.collidedWith(coin)):
    coin.makeVisible(visibility = 0)
  if (mario.collidedWith(coin2)):
    coin2.makeVisible(visibility = 0)
  if (mario.collidedWith(coin3)):
    coin3.makeVisible(visibility = 0)
  if (mario.collidedWith(coin4)):
    coin4.makeVisible(visibility = 0)

  # collision of mario with Mystery box
  if (mario.collidedWith(bl_4)):
    bl_4.makeVisible(visibility = 0)
    fireFlower.moveTo(380,250)
    score += 50
  if (mario.collidedWith(fireFlower)):
    fireFlower.makeVisible(visibility = 0)
    angryMush.makeVisible(visibility = 0)
    visible -= 1
    score += 60
  
  # collision of mario with the blocks
  if (mario.collidedWith(bl_1) or mario.collidedWith(bl_2) or mario.collidedWith(bl_3)):
    mario.y = 305

  if (mario.collidedWith(bl_5) or mario.collidedWith(bl_6) or mario.collidedWith(bl_41)):
    mario.y = 175
  
  # collision of mario with pipe
  if (mario.collidedWith(pipe)):
    mario.y = 430

  # mario health displayed on top-left corner
  if (mario.health == 80):
    heart4.makeVisible(visibility = 0)  
  if (mario.health == 60):
    heart3.makeVisible(visibility = 0)
  if (mario.health == 40):
    heart2.makeVisible(visibility = 0)
  if (mario.health == 20):
    heart1.makeVisible(visibility = 0)
  
  # quits the game once health <= 0
  if (mario.health <= 0):
    game.over = True
    game.clearBackground(color = (135,206,235))
    game.drawText("Game Over!", 200, 200, Font(white, 96))
    game.drawText('Score: ' + str(score) + '         Coins: ' + str(coinCount) + '        Time: ' + str(round(minutes)) +' m ' + str(round(sec))+' s', 130, 300, Font(white,40))
    game.update(20)
    game.wait(K_SPACE)
  
  # takes to next level once Goomba is defeated
  if (visible <= 0 and mario.collidedWith(door)):
    game.over = True
    game.clearBackground(color = (135,206,235))
    game.drawText("Level Complete!", 150, 200, Font(white, 96))
    game.drawText('Score: ' + str(score) + '         Coins: ' + str(coinCount) + '        Time: ' + str(round(minutes)) +' m ' + str(round(sec))+' s', 130, 300, Font(white,40))
    game.update(20)
    game.wait(K_SPACE)
  
  # Displays coins
  game.drawText('Score: ' + str(score), 280, 10, Font(white,40))
  game.drawText(('Coins: ' + str(coinCount)), 450, 10, Font(white,40))
  game.drawText(('Time: ' + str(round(minutes))+' m ' + str(round(sec))+' s'), 600, 10, Font(white, 40))

  # frames per second
  game.update(20)