import subprocess
import curses

class Grid:
  def __init__(self):
    self._rows, self._columns = map(int, subprocess.check_output(['stty', 'size']).split())
    self._marker = u"\u2584"
    self._stdscr = None
    curses.wrapper(self.setup)

  
  def setup(self, stdscr):
    self._stdscr = stdscr
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.border(0)
  
  def glider(self):
    middle_row = int(self._rows/2)
    middle_column = int(self._columns/2)

    return [(middle_row, middle_column),
            (middle_row + 1, middle_column + 1),
            (middle_row + 2, middle_column - 1), (middle_row + 2, middle_column), (middle_row + 2, middle_column + 1)]
    
  def draw_a_glider(self):
    coordinates = self.glider()
    
    for coordinate in coordinates:
      self.insert_charactor(coordinate[0], coordinate[1], self._marker)
    self.display(1000)
  
  def draw(self, coordinates):
    for coordinate in coordinates:
      self.insert_charactor(coordinate[0], coordinate[1], self._marker)

  def display(self, m_seconds):
      self._stdscr.refresh()
      curses.napms(m_seconds)

  def main(self, stdscr):
    self.setup(stdscr)
    self.draw_a_glider()

  def insert_charactor(self, row, column, character):
    self._stdscr.addstr(row, column, character)
    

  def run(self, func):
    curses.wrapper(func)

if __name__ == "__main__":
  Grid().run()
