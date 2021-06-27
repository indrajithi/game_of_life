import subprocess
import curses

class Grid:
  _rows, _columns = map(int, subprocess.check_output(['stty', 'size']).split())

  def __init__(self):
    self._marker = u"\u2584"
    self.matrix = self.glider()
    self.delay = 500
    
  def is_cord_positive(self, cord):
      return cord[0] >= 0 and cord[1] >= 0
    
  def is_below_last_cord(self, cord):
      return cord[0] < self._rows and cord[1] < self._columns
         
  def is_life_in_grid(self, cord):
    return self.is_cord_positive(cord) and self.is_below_last_cord(cord)
  
  def set_matrix(self, matrix):
      self.matrix = [life for life in matrix if self.is_life_in_grid(life)]

  def draw_matrix(self):
    curses.wrapper(self.run)
  
  def setup(self, stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.clear()
    stdscr.border(0)
    
  def run(self, stdscr):
    self.stdscr = stdscr
    self.setup(stdscr)
    self.draw(stdscr)
    stdscr.refresh()
    curses.napms(self.delay)
  
  def glider(self):
    middle_row = int(self._rows/2)
    middle_column = int(self._columns/2)

    return [(middle_row, middle_column),
            (middle_row + 1, middle_column + 1),
            (middle_row + 2, middle_column - 1), (middle_row + 2, middle_column), (middle_row + 2, middle_column + 1)]
  
  def draw(self, stdscr):
    for coordinate in self.matrix:
      stdscr.addstr(coordinate[0], coordinate[1], self._marker)

if __name__ == "__main__":
  grid = Grid()
  grid.draw_matrix()
