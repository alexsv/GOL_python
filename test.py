from .main import Grid

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
   