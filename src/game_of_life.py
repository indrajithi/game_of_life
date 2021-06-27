from grid import Grid

class GameOfLife(Grid):
    def __init__(self):
      Grid.__init__(self)
      self.matrix = self.random_matrix()

    def get_neighbors(self, row, col):
      neighbors = [(row - 1, col -1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1), (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1) ]


      return neighbors
    
    def get_alive_neighbors(self, life):
      return [n for n in self.get_neighbors(*life) if n in self.matrix]
    
    def is_alive(self, life, neighbors):
      if len(neighbors) < 2: # under population
        return False
      if len(neighbors) > 3: # over population
        return False
      return True
    
    def reproduction(self, neighborhood):
      births = []
      for life in neighborhood:
        if len(self.get_alive_neighbors(life)) == 3:
         births.append(life)
      return births
      
    def next_generation(self):
      _matrix = []
      neighborhood = set(self.matrix)
      for life in self.matrix:
        neighbors = self.get_neighbors(*life)
        alive_neighbors = [n for n in neighbors if n in self.matrix]
        neighborhood.update(neighbors)
        
        if self.is_alive(life, alive_neighbors):
          _matrix.append(life)
        
      _matrix += self.reproduction(neighborhood)
      self.matrix = list(set(_matrix))

def main():
  game = GameOfLife()
  try:
    while True:
      game.draw_matrix()
      game.next_generation()
  except KeyboardInterrupt:
    pass # end game
  
if __name__ == "__main__":
  main()