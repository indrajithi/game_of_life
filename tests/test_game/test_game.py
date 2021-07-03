import pytest
from game.life import Life

@pytest.fixture
def life():
  life = Life()
  life.matrix = [(0,0), (0,1), (0,2), (0,3)]
  return life


@pytest.fixture
def neighborhood():
  return {(0, 1), (1, 3), (1, 2), (0, 4), (-1, -1), (-1, 4), (0, 0), (-1, 1), (1, 1), (0, 3), (1, -1), (1, 4), (-1, 0), (0, 2), (-1, 3), (1, 0), (-1, 2), (0, -1)}

def test_get_neighbors(life):
  assert life.get_neighbors(0, 0) == [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  
def test_get_alive_neighbors(life):
  assert life.get_alive_neighbors((0,0)) == [(0,1)]

def test_is_alive(life):
  neighbors = life.get_neighbors(0, 0)
  assert life.is_alive((0,0), neighbors) == False

def test_reproduction(life, neighborhood):
  assert life.reproduction(neighborhood) == [(1, 2), (-1, 1), (1, 1), (-1, 2)]
  
  
def test_next_generation(life):
  life.next_generation()
  assert life.matrix == [(0, 1), (1, 2), (-1, 1), (1, 1), (0, 2), (-1, 2)]
  