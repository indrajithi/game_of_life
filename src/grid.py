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
    self._rows, self._columns = map(int, subprocess.check_output(['stty', 'size']).split())
    
  def is_cord_positive(self, cord):
      return cord[0] >= 0 and cord[1] >= 0
    
  def is_below_last_cord(self, cord):
      return cord[0] < self._rows and cord[1] < self._columns
         
  def is_life_in_grid(self, cord):
    return self.is_cord_positive(cord) and self.is_below_last_cord(cord)
  
  def draw_matrix(self):
    curses.curs_set(0)
    self.screen.erase()
    self.draw()
    curses.napms(self.delay)
    self.screen.refresh()
  
  def random_matrix(self):
    _matrix = []
    for _ in range(random.randint(500, 1000)):
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
      if self.is_life_in_grid(coordinate):
        if(curses.is_term_resized(self._rows, self._columns)):
          self.set_screen_dimensions()
        try:
          self.screen.addstr(coordinate[0], coordinate[1], self._marker)
        except:
          print(coordinate, self._rows, self._columns)


if __name__ == "__main__":
  grid = Grid()
  grid.draw_matrix()
