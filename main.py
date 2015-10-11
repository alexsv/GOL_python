
AROUND = [(-1, -1), (-1, 0), (-1, 1), 
          (0, -1),           (0, 1), 
          (1, -1),  (1, 0),  (1, 1)]

class Grid(object):
   def __init__(self):
      self.cells = {}
      
   def get_state(self, x, y):
      return self.cells.get((x, y), 0)

   def set_active(self, x, y):
      self.cells[(x, y)] = 1
   
   def get_new_state(self, x, y):
      around = [self.get_state(x + dx, y + dy) for dx, dy in AROUND]
      count = sum(around)
      state = self.get_state(x, y)
      
      if state and count in [0, 1]:
         return 0
      
      if count in [2, 3]:
         return state
      
      if state and count > 3:
         return 0
         
      if not state:
         return 0 
         
      raise Exception("!")
      
   def next():
      pass


self_x = 1
self_y = 1

def test_empty_grid():
   grid = Grid()
   assert grid.get_state(1, 1) == 0
   assert grid.get_state(-100, -100) == 0
   assert grid.get_state(100, 100) == 0

def test_no_neightbors():
   grid = Grid()
   grid.set_active(1, 1)
   state = grid.get_new_state(1, 1)
   assert state == 0
   
def test_one_neighbor():
   grid = Grid()
   grid.set_active(self_x, self_y)
   grid.set_active(self_x, self_y + 1)
   state = grid.get_new_state(self_x, self_y)
   assert state == 0

def test_two_neighbors():
   grid = Grid()
   grid.set_active(self_x, self_y)
   grid.set_active(self_x - 1, self_y)
   grid.set_active(self_x + 1, self_y)
   state = grid.get_new_state(self_x, self_y)
   assert state == 1
   
def test_active_with_three_neighbors():
   grid = Grid()
   
   grid.set_active(self_x, self_y)
   grid.set_active(self_x, self_y + 1)
   grid.set_active(self_x + 1, self_y)
   grid.set_active(self_x + 1, self_y + 1)
   state = grid.get_new_state(self_x, self_y)
   assert state == 1
   
def test_not_active_with_three_neighbors():
   grid = Grid()
   grid.set_active(self_x, self_y + 1)
   grid.set_active(self_x + 1, self_y)
   grid.set_active(self_x + 1, self_y + 1)
   state = grid.get_new_state(self_x, self_y)
   assert state == 0

def test_more_three_neightbors():
   grid = Grid()
   grid.set_active(self_x, self_y)
   grid.set_active(self_x - 1, self_y - 1)
   grid.set_active(self_x, self_y - 1)
   grid.set_active(self_x + 1, self_y - 1)
   grid.set_active(self_x - 1, self_y)
   state = grid.get_new_state(self_x, self_y)
   assert state == 0

   grid.set_active(self_x + 1, self_y)
   state = grid.get_new_state(self_x, self_y)
   assert state == 0

   grid.set_active(self_x - 1, self_y + 1)
   grid.set_active(self_x, self_y + 1)
   grid.set_active(self_x + 1, self_y + 1)
   state = grid.get_new_state(self_x, self_y)
   assert state == 0

def test_empty_cell():
   grid = Grid()
   state = grid.get_new_state(self_x, self_y)
   assert state == 0
   