'''

Chaser Program - 

Based off of backtracking_robot_maze_printer.py. 

Robot chases you, has a 50% chance to move every turn. You move every turn.

Each turn, robot computes path to you, then does the first move in list.

Each turn, you can move. That's it.


'''

# http://www.cs.bu.edu/teaching/alg/maze/

'''
So, backtracking. It's called backtracking, because when it finds a dead end, 
it walks back up, marking those solutions as checked. I.e., if a step was legit,
but there's no next answer that works, reverse back up to the last known, and
keep going.

1) Check current tile
2) Mark current as a step
3) Check all possible next steps 
4) If none of those worked, remark this step as bad, return False (which simply
doesn't stop that recursive instance from working other single direction steps. 
Ultimately, you get a True at the GOAL, and every step leading up to it sends 
a TRUE.

'''

### find_path(x,y):
class pathfinder(grid):
    
    max_x = len(grid[0])-1
    max_y = len(grid)-1

    def new_turn(self):
        # wipe movelist clean
        self.movelist = []

    def find_path(self,x,y):
       
        
##### CHECK CURRENT TILE: 
       
## if (x, y outside maze) return False
        #print(' outside maze?')
        if x > self.max_x or x < 0 or y > self.max_y or y < 0:
            return False

## if (x, y is goal) return True
        #print(' goal?')
        print(x,y)
        if self.grid[x][y] == 'P': # if you catch player
            return True

## if (x,y not open) return False
       #print(' blocked?')
        if self.grid[x][y] in ['#','+','x']:
            return False

### THIS TILE IS CLEAN, and not the end
## mark x, y as part of solution path ##
        self.grid[x][y] = '+'




##### CHECK ADJACENT TILES 

## if (find_path(North of x,y) == True) return True
        if y-1 >= 0 and self.find_path(x,y-1) == True: return self.print_pos(x,y)

## if (find_path(East of x,y) == True) return True
        if x+1 <= self.max_x and self.find_path(x+1,y) == True: return self.print_pos(x,y)
## if (find_path(South of x,y) == True) return True
        if y+1 <= self.max_y and self.find_path(x,y+1) == True: return self.print_pos(x,y)
## if (find_path(West of x,y) == True) return True
        if x-1 >= 0 and self.find_path(x-1,y) == True: return self.print_pos(x,y)

### Whelp, this tile's clean, but also a deadend
## unmark x,y as part of solution path
        self.grid[x][y] == 'x'
## return false
        return False

    def print_maze(self):
        for row in self.grid:
            print(row)

    def print_pos(self,x,y):
        print(x, y)
        self.movelist.append(x,y)
        return True

p = pathfinder()
p.print_maze()
print(p.grid[0][0])
p.find_path(0,0)
p.print_maze()

''
## overall initalization

import os

captured = False

grid = [['R','#','#','#','.'],
        ['.','#','.','.','.'],
        ['.','.','.','#','.'],
        ['.','#','#','#','P']]

# R: robot
# P: player
# #: wall
# .: open space

# def want to have grid gen here: theres the map the player sees,
# and the robot's own map. (necessary? maybe not. although it'd be good to show
# me for debug that the algo works

while not captured:
    os.system('clear')
    print('Screen goes here')


## a turn:

# initialize: wipe movelist, have current location ready. Update map for search
# with player position.

# do findpath from current spot
# get player input, check if valid: yes? move on. No? try again.
# set current robot location = first step of move list, player location (their choice)
# check win condition - robot on your spot? Gotcha bitch
# end loop
