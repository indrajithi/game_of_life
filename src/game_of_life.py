from grid import Grid

class GameOfLife(Grid):
    def __init__(self):
      Grid.__init__(self)
      self.matrix = self.glider()
      
    def is_cord_positive(self, cord):
      return cord[0] >= 0 and cord[1] >= 0
    
    def is_below_last_cord(self, cord):
      return cord[0] < self._rows and cord[1] < self._columns
         
    def is_life_in_grid(self, cord):
      return self.is_cord_positive(cord) and self.is_below_last_cord(cord)
    
      
    def get_neighbors(self, row, col):
      neighbors = [(row - 1, col -1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1), (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1) ]


      return neighbors
    
    def set_matrix_in_grid(self, matrix):
      self.matrix = [life for life in matrix if self.is_life_in_grid(life)]
    
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
        a = self.get_alive_neighbors(life)
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
      self.set_matrix_in_grid(_matrix)
      


game = GameOfLife()
# game.run()
print(game.next_generation())
game.run(game.setup)
game.draw(game.matrix)
game.display(3000)
