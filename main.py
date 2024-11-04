from google.colab import files
import sys


# Add the current directory to the Python path
sys.path.append('/content')
import game_function as gf

def main():
    grid = gf.initialize_grid()
    prev = grid
    gf.print_grid(grid)
    keep_going = True
    while keep_going:
      print("w: Move up, s: Move down, a: Move left, d: Move right")
      ans = input("Please enter your move(w/s/a/d): ").lower()
      try:
        if ans == "w":
          grid = gf.move_up(grid)
          
        elif ans == "s":
          grid = gf.move_down(grid)
          
        elif ans == "a":
          grid = gf.move_left(grid)
          
        elif ans == "d":
          grid = gf.move_right(grid)
          
        else:
          raise ValueError
        gf.print_grid(grid)
      except ValueError:
        print("Invalid input. Please enter 'w', 's', 'a', or 'd'.")
        continue
      
      Result = gf.check_win(grid)
      if Result == True:
        print("Congraduation! You've won the game")
        while True:
          ans = input("Would you like to play again? (y/n): ").lower()
          try:
            if ans != "y" and ans != "n":
              raise ValueError
          except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
          if ans == "y":
            keep_going = True
            grid = gf.initialize_grid()
            gf.print_grid(grid)
          else:
            keep_going = False
            print("Thanks for playing!")
            break
      
      lose = gf.check_lose(grid, prev)
      if lose == True:
        print("Game Over")
        while True
          ans = input("Would you like to play again? (y/n): ").lower()
          try:
            if ans != "y" and ans != "n":
              raise ValueError
          except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
          if ans == "y":
            keep_going = True
            grid = gf.initialize_grid()
            gf.print_grid(grid)
          else:
            print("Thanks for playing!")
            keep_going = False
            break

      prev = grid.copy()
      grid = gf.add_new(grid)
      print("new 2 add:")
      gf.print_grid(grid)
main()
