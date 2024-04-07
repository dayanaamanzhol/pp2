import pygame, sys
from pygame.locals import*
import random

#window
width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car Game')

gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

gameover = False
speed = 2
score = 0

#marker and road
markerW = 10
markerH = 50

road = (100, 0, 300, height)
left_edge = (95, 0, markerW, height)
right_edge = (395, 0, markerW, height)

#coordinates of lanes
leftlane = 150
center = 250
rightlane = 350
lanes = [leftlane, center, rightlane]

lanemove = 0

class Vehicle(pygame.sprite.Sprite):

  def __init__(self, image, x, y):
    pygame.sprite.Sprite.__init__(self)

    image_scale = 45 / image.get_rect().width
    new_width = image.get_rect().width * image_scale
    new_height = image.get_rect().height * image_scale
    self.image = pygame.transform.scale(image, (new_width, new_height))

    self.rect = self.image.get_rect()
    self.rect.center = [x, y]

class PlayerCar(Vehicle):
  def __init__(self, x, y):
    image = pygame.image.load('images/car.png')
    super().__init__(image, x, y)

#players coordinates
playerx = 250
playery = 400

#players car
player_group = pygame.sprite.Group()
player = PlayerCar(playerx, playery)
player_group.add(player)

#other vehicles
image_list = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_image = []
for im in image_list:
  image = pygame.image.load('images/' + im) 
  vehicle_image.append(image)

#sprite for vehicles
vehicle_group = pygame.sprite.Group()

#crash image
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

#game loop
clock = pygame.time.Clock()
fps = 120
while True:
  clock.tick(fps)

  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()



    if event.type == KEYDOWN:
      if event.key == K_LEFT and player.rect.center[0] > leftlane:
        player.rect.x -= 100
      if event.key == K_RIGHT and player.rect.center[0] < rightlane:
        player.rect.x += 100


      for vehicle in vehicle_group:
        if pygame.sprite.collide_rect(player, vehicle):

          gameover = True


          if event.key == K_LEFT:
            player.rect.left = vehicle.rect.right
            crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]

          elif event.key == K_RIGHT:
            player.rect.right = vehicle.rect.left
            crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
  screen.fill(green)
  
  #draw road  

  pygame.draw.rect(screen, gray, road)
  pygame.draw.rect(screen, yellow, left_edge)
  pygame.draw.rect(screen, yellow, right_edge)

  #lane markers
  lanemove += speed * 2
  if lanemove >= markerH * 2:
    lanemove = 0
  for y in range(markerH * -2, height, markerH * 2):
    pygame.draw.rect(screen, white, (leftlane + 45, y + lanemove, markerW, markerH))
    pygame.draw.rect(screen, white, (center + 45, y + lanemove, markerW, markerH))
  #playercar
  player_group.draw(screen)

  if len(vehicle_group) < 2:

    add_vehicle = True
    for v in vehicle_group:
      if vehicle.rect.top < v.rect.height * 1.5:
        add_vehicle = False
    if add_vehicle:
      lane = random.choice(lanes)
      image = random.choice(vehicle_image)
      vehicle = Vehicle(image, lane, height / -2)
      vehicle_group.add(vehicle)

  #vehicle move
  for v in vehicle_group:
    vehicle.rect.y += speed
    if v.rect.top >= height:
      vehicle.kill()
      score += 1

      if score > 0 and score % 5 == 0:
        speed += 1

  vehicle_group.draw(screen)

  #score
  pygame.font.init()

  font = pygame.font.Font(pygame.font.get_default_font(), 16)
  text = font.render('Score: ' + str(score), True, white)
  text_rect = text.get_rect()
  text_rect.center = (50, 400)
  screen.blit(text, text_rect)

   # check if there's a head on collision
  if pygame.sprite.spritecollide(player, vehicle_group, True):
    gameover = True        
    crash_rect.center = [player.rect.center[0], player.rect.top]

    # display game over
  if gameover:
    screen.blit(crash, crash_rect)

    pygame.draw.rect(screen, red, (0, 50, width, 100))

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Game over. Play again? (Enter Y or N)', True, white)
    text_rect = text.get_rect()
    text_rect.center = (width / 2, 100)
    screen.blit(text, text_rect)

  pygame.display.update()


    # wait for user's input to play again or exit
  while gameover:

    clock.tick(fps)

    for event in pygame.event.get():

      if event.type == QUIT:
        gameover = False
        running = False

# get the user's input (y or n)
      if event.type == KEYDOWN:
        if event.key == K_y:
          # reset the game
          gameover = False
          speed = 2
          score = 0
          vehicle_group.empty()
          player.rect.center = [player_x, player_y]
        elif event.key == K_n:
          # exit the loops
          gameover = False
          running = False
