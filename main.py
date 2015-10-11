
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

   def get_active(self):
      return self.cells.keys()

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
         
   def next(self):
      grid = Grid()
      all_x = {x for x, _ in self.get_active()}
      all_y = {y for _, y in self.get_active()}
      return grid

   