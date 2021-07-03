import subprocess
import curses
import random

class Grid:
  def __init__(self):
    self._marker = u"\u2022"
    self.delay = 100
    self.screen = curses.initscr()
    self.set_screen_dimensions()
  
  def set_screen_dimensions(self):
    self._rows, self._columns = self.screen.getmaxyx()
    
  def is_cord_positive(self, cord):
      return cord[0] >= 0 and cord[1] >= 0
    
  def is_below_last_cord(self, cord):
      if cord[0] >= self._rows - 1:
        return False
      if cord[1] >= self._columns - 1:
        return False
      return True
         
  def is_life_in_grid(self, cord):
    return self.is_cord_positive(cord) and self.is_below_last_cord(cord)
  
  def teardown(self):
    self.screen.keypad(True)
    curses.curs_set(True)
    curses.endwin()

  def glider(self):
    middle_row = int(self._rows/2)
    middle_column = int(self._columns/2)

    return [(middle_row, middle_column),
            (middle_row + 1, middle_column + 1),
            (middle_row + 2, middle_column - 1), (middle_row + 2, middle_column), (middle_row + 2, middle_column + 1)]
    
  def draw_matrix(self):
    curses.curs_set(False)
    self.screen.erase()
    self.draw()
    curses.napms(self.delay)
    self.screen.refresh()

  def random_matrix(self):
    _matrix = []
    for _ in range(random.randint(500, 1500)):
      _matrix.append((random.randint(0, self._rows - 1), random.randint(0, self._columns - 1)))
    return list(set(_matrix))

  def glider(self):
    middle_row = int(self._rows/2)
    middle_column = int(self._columns/2)

    return [(middle_row, middle_column),
            (middle_row + 1, middle_column + 1),
            (middle_row + 2, middle_column - 1), (middle_row + 2, middle_column), (middle_row + 2, middle_column + 1)]
    
  def draw(self):
    for coordinate in self.matrix:
      if(curses.is_term_resized(self._rows, self._columns)):
        self.set_screen_dimensions()
      if self.is_life_in_grid(coordinate):
        try:
          self.screen.addstr(coordinate[0], coordinate[1], self._marker)
        except:
          raise(Exception('Insert error on:' + str([self._rows, self._columns, coordinate])))
