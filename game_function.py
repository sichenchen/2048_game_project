import random
def initialize_grid():
    grid = [[0]*4 for _ in range(4)] #4x4 matrix
    row1 = random.randint(0,3) # generate 2 "2" randomly in the matrix
    col1 = random.randint(0,3)
    row2 = random.randint(0,3)
    col2 = random.randint(0,3)
    grid[row1][col1]=2
    while row1==row2 and col1==col2:
        row2 = random.randint(0,3)
        col2 = random.randint(0,3)
    grid[row2][col2]=2
    return grid

def print_grid(grid): # show matrix
    for row in grid:
        print(" ".join(map(str,row)))
def add_new(grid): #add a new "2" at empty position
    empty = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty:  # Ensure there is an empty cell
      row, col = random.choice(empty)
      grid[row][col] = 2
    return grid

def move_left(grid): #move titles left
    new = []
    for row in range(4):
      nonemp = [grid[row][i] for i in range(4) if grid[row][i] != 0] #extract nonempty numbers
      new_row = []
      skip = False
      for col in range(len(nonemp)):
        if skip:
          skip = False
          continue
        if col < len(nonemp)-1 and nonemp[col] == nonemp[col+1] and not skip: #if they are same, merge them
          new_row.append(nonemp[col]*2)
          skip = True
        else:
          new_row.append(nonemp[col])
      new_row += [0]*(4-len(new_row)) #add 0 to get a vector with 4 numbers
      new.append(new_row) #update row

    return new
  
def move_right(grid): #move right with the same logic with move_left
    new = []
    for row in range(4):
      nonemp = [grid[row][i] for i in range(4) if grid[row][i] != 0]
      new_row = []
      skip = False
      for col in range(len(nonemp)-1,-1,-1):
        
        if skip:
          
          skip = False
          continue
        elif col > 0 and nonemp[col] == nonemp[col-1] and not skip:
          new_row = [nonemp[col]*2] + new_row
          skip = True
        else:
          new_row = [nonemp[col]] + new_row
      new_row = [0]*(4-len(new_row))+new_row
      new.append(new_row)

    return new

def move_up(grid): move up with the same logic with move_left
    new = [[0]*4 for i in range(4)]
    for col in range(4):
      nonemp = [grid[row][col] for row in range(4) if grid[row][col] != 0]
      new_col = []
      skip = False

      for row in range(len(nonemp)):
        if skip:
          skip = False
          continue
        elif row < len(nonemp)-1 and nonemp[row] == nonemp[row+1] and not skip:
          new_col.append(nonemp[row]*2)
          skip = True
        else:
          new_col.append(nonemp[row])
      new_col += [0]*(4-len(new_col))
      for row in range(4):
        new[row][col] = new_col[row]
    return new

def move_down(grid): #move down with the same logic with move_left
    new = [[0]*4 for i in range(4)]
    for col in range(4):
      nonemp = [grid[row][col] for row in range(4) if grid[row][col] != 0]
      
      new_col = []
      skip = False
      for row in range(len(nonemp)-1,-1,-1):
        
        if skip:
          skip = False
          continue
        elif row > 0 and nonemp[row] == nonemp[row-1] and not skip:
          new_col=[nonemp[row]*2] + new_col
          skip = True
        else:
          new_col = [nonemp[row]] + new_col
          

      new_col = [0]*(4-len(new_col))+new_col
     
        

      for row in range(4):
          new[row][col] = new_col[row]
    return new

def check_win(grid): #check if one of numbers achieve 2048 
    for row in grid:
        if 2048 in row:
            return True
    return False

def check_lose(grid, prev): #check if there is a "dead" road
    emp = [grid[row][col] for row in range(4) for col in range(4) if grid[row][col] == 0]
    if grid == prev and len(emp)==0:
        return True
    return False
          
