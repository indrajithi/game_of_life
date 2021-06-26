from rich import print
from rich.layout import Layout

class Grid:
  def __init__(self):
    self.grid_dimensions = [100, 100]
  
  def create_layout(self):   
    layout = Layout()
    print(layout)
    return True
    
    
    