import subprocess
import curses

class Grid:
  def __init__(self):
    self.rows, self.columns = map(int, subprocess.check_output(['stty', 'size']).split())
    self.marker = u"\u2584"
    self._stdscr = None
    
  def setup(self, stdscr):
    self._stdscr = stdscr
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.border(0)
    
  def draw_a_glider(self):
    middle_row = int(self.rows/2)
    middle_column = int(self.columns/2)
    coordinates = [(middle_row, middle_column),
                   (middle_row + 1, middle_column + 1),
                   (middle_row + 2, middle_column - 1), (middle_row + 2, middle_column), (middle_row + 2, middle_column + 1)]
    
    for coordinate in coordinates:
      print(coordinates)
      self.insert_charactor(coordinate[0], coordinate[1], self.marker)
    self.display(2000)

  def display(self, m_seconds):
      self._stdscr.refresh()
      curses.napms(m_seconds)

  def main(self, stdscr):
    self.setup(stdscr)
    self.draw_a_glider()

  def insert_charactor(self, row, column, character):
    self._stdscr.addstr(row, column, character)
    
  
  def run(self):
    curses.wrapper(self.main)

if __name__ == "__main__":
  Grid().run()
