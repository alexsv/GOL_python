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
   
def test_next_state_is_grid():
   grid = Grid()
   grid = grid.next()
   assert isinstance(grid, Grid)

def test_next_state_empty():
   grid = Grid()
   grid = grid.next()
   assert len(grid.get_active()) == 0

def test_get_ranges_no_active():
   grid = Grid()
   x1, y1, x2, y2 = grid.get_ranges()
   assert (x1, y1, x2, y2) == (0, 0, 0, 0)
   
def test_get_ranges_some_active():
   grid = Grid()
   grid.set_active(-2, -1)
   grid.set_active(2, 1)
   x1, y1, x2, y2 = grid.get_ranges()
   assert (x1, y1, x2, y2) == (-2, -1, 2, 1)

def _test_3near_doesnt_change():
   grid = Grid()
   grid.set_active(self_x, self_y)
   grid.set_active(self_x + 1, self_y)
   grid.set_active(self_x, self_y + 1)
   grid.set_active(self_x + 1, self_y + 1)

   grid = grid.next()
   active = grid.get_active()
   assert len(active) == 4
   assert (self_x, self_y) in active 
   assert (self_x + 1, self_y) in active
   assert (self_x, self_y + 1) in active
   assert (self_x + 1, self_y + 1) in active      