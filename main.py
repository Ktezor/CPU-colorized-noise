import pygame as pg
from pygame.locals import *
from square import Square

## Options
screen_options = {
  'screen_size':{
    1:(1920, 1080),
    2:(1280,720),
    3:(800,600)
  },
  'type_animation':{
    'random':0,
    'gradient':1
  }
}
COLORS = {
  "black":(255,255,255,255)
}

##SIZE 1 SQUARE
block = [50, 50]

screen_size = screen_options['screen_size'][2]
animation = screen_options['type_animation']['gradient']

class Application(object):
  def __init__(self):
    pg.init()
    self.screen = pg.display.set_mode(screen_size)
    self.screen.fill(COLORS['black']) ## If we want to use other RGB names

    ##Create POINTS

    points = [(200, 300, [255, 0, 0]), 500]
    
    ##CREATE GRID
    
    bias = (int(screen_size[0]/block[0]), int(screen_size[1]/block[1]))

    self.squares = pg.sprite.Group()

    selected_pos = [0,0]

    ##Create blocks squares
    Square.size = [block[0], block[1], screen_size, points, animation]
    Square.points = points

    for x in range(bias[0]):
      for y in range(bias[1]):

        self.squares.add(Square(selected_pos[0], selected_pos[1]))
        selected_pos[1] = selected_pos[1] + block[1]
      selected_pos[1] = 0
      selected_pos[0] = selected_pos[0] + block[0]

  def mainloop(self):
    while True:

      for e in pg.event.get():
        if e.type in [pg.QUIT, pg.MOUSEBUTTONDOWN]:
          exit()
        elif e.type == pg.KEYDOWN:
          key = e.key
          if key == K_q or key == K.ESCAPE:
            exit()

        self.squares.update()
        self.screen.fill(COLORS['black'])
        self.squares.draw(self.screen)
        pg.display.flip()

if __name__ == '__main__':
  app = Application()
  app.mainloop()
