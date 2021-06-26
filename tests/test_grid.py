import unittest
from src.grid import Grid
from rich.layout import Layout

class TestCreateGrids(unittest.TestCase):
  
  def test_set_grid_dimension(self):
    """
    Make sure there is grid dimensions
    """
    grid = Grid()
    self.assertEqual(grid.grid_dimensions, [100, 100])
  
  def test_create_layout(self):
    """
    Create a layout using rich
    """
    grid = Grid()
    self.assertEqual(grid.create_layout(), True)