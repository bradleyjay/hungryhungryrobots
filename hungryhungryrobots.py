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

import os
import copy
import random

class Robot:
    '''
    Path finding, robot's knowledge of the map (aka grid),
    and new turn initialization for the robot.
    '''
    def __init__(self,grid):
        self.grid = grid
        self.movelist = []
        self.update_grid(grid)
        

    def update_grid(self,grid):
        ## gives the ability to set the robot's grid (for the move
        ## about to be made) from the outside
        # copy in new grid
        self.grid = copy.deepcopy(grid)

        # length of each row = x
        self.max_x = len(grid)-1

        # length of each column (# of rows) = y
        self.max_y = len(grid[0])-1
      
    def new_turn(self):
        # wipe movelist, rmove clean
        self.movelist = []
        rmove = (False, None)

    def find_path(self,x,y):

        '''
        Solve for the path between the robot and player. Once found,
        record the sequence of moves you WOULD take to self.move_list via
        self.print_pos.
        '''
        ##### CHECK CURRENT TILE: 
               
        ## if (x, y outside maze) return False
                #print(' outside maze?')
        if x > self.max_x or x < 0 or y > self.max_y or y < 0:
            return False

        ## if (x, y is goal) return True
        #print(' goal?')
        #print(x,y)
        if self.grid[x][y] == 'P': # if you catch player
            return self.print_pos(x,y) # if this isn't here, cant move onto player
            # when one square away

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

        ## if (find_path(South of x,y) == True) return True
        if y+1 <= self.max_y and self.find_path(x,y+1) == True: return self.print_pos(x,y)

        ## if (find_path(East of x,y) == True) return True
        if x+1 <= self.max_x and self.find_path(x+1,y) == True: return self.print_pos(x,y)
        
        ## if (find_path(West of x,y) == True) return True
        if x-1 >= 0 and self.find_path(x-1,y) == True: return self.print_pos(x,y)

        ### Whelp, this tile's clean, but also a deadend
        ## unmark x,y as part of solution path
        self.grid[x][y] == 'x'

        ## return false
        return False

    def print_pos(self,x,y):
        ## once findpath succeeds, each recursive step back to the robot is
        ## saved here in order, as movelist

        #print(x, y)
        self.movelist.append((x,y))
        return True

def print_maze(grid):
        # print maze
        for row in grid:
            print(row)

def valid_move(x,y): #takes a location tuple
    if x > R.max_x or y > R.max_y or grid[x][y] in ['#','+','x']: #safe because out of bounds fails before xy evaluation 
        return False, (x,y)
    if grid[x][y] == 'R':
        return True, ('robot')
    return True, (x,y)

def generate_grid():
    # maps #
   
    grid0 =[['R','#','#','#','.'],
            ['.','#','.','.','.'],
            ['.','.','.','#','.'],
            ['.','#','#','#','P']]

    grid1 =[['R','#','.','.','.','#','.'],
            ['.','#','#','#','.','#','.'],
            ['.','.','.','.','.','.','.'],
            ['#','#','.','#','#','#','.'],
            ['.','#','.','#','.','.','.'],
            ['.','#','.','#','.','#','#'],
            ['.','.','.','.','.','.','P']]

    grid_list = [grid0, grid1]

    grid_choice = random.randint(0,0)
    return grid_list[grid_choice]


### ok, works. So now, gotta make robot more logically built  #####

## overall initalization

# the grid. This will later be a randomly selected map, or procedural, etc

grid = generate_grid()

# R: robot
# P: player
# #: wall
# .: open space

R = Robot(grid)

captured = False

# starting positions: generalize this later to be callable maybe

for i in range(0,len(grid)):
    for j in range(0, len(grid[i])):
        #print(grid[i][j],(i,j))
        if grid[i][j] == 'R': r_xy = (i,j)  # save robot current pos
        if grid[i][j] == 'P': p_xy = (i,j)  # save player current pos

  
# r_xy = (0,0)
# p_xy = (3,4)

# def want to have grid gen here: theres the map the player sees,
# and the robot's own map. (necessary? maybe not. although it'd be good to show
# me for debug that the algo works

## for now, run once! uncomment after
while not captured:
    os.system('clear')
    print_maze(grid)

## a turn:

# initialize: 
##wipe movelist, Update map for search
    
    R.new_turn()    # wipe robot movelist
    R.update_grid(grid)

# do findpath from current spot, save next move

    R.find_path(*r_xy)  # i think this means unpack tuple, holy shit did that work?
    
    if len(R.movelist)>1:
        rmove = (True, R.movelist[-2]) # robot next move (first step on path to player)
    else: 
        rmove = (True, R.movelist[0])

# get player input, check if valid: yes? move on. No? try again.
    
    pmove = (False, None) # initialize player input as invalid, and nothing.

    while pmove[0] == False:

        os.system('clear')
        print_maze(grid)
        #print(R.movelist)
        p_input = input('\n Enter move, then press enter: \n' + 'u: Up \n' 
            + 'd: Down \n' + 'l: Left \n' + 'r: Right \n' + '>>')
    ## holy shit this is complicated. Curses seems to do it, pygame needs a window....
    ## anything else needs low level keyboard/thead access, its really hard.

        if p_input == 'u': 
            pmove = valid_move(p_xy[0]-1, p_xy[1]) # these x and y are swapped for some reason
        elif p_input == 'd':
            pmove = valid_move(p_xy[0]+1,p_xy[1])
        elif p_input == 'l':
            pmove = valid_move(p_xy[0],p_xy[1]-1)
        elif p_input == 'r': 
            pmove = valid_move(p_xy[0],p_xy[1]+1)
        
        if pmove[0] == False:
            input('Invalid entry, press any key.')

    
# set current robot location = first step of move list, player location (their choice),
# AND blank their old spots
    
    #print(rmove[1][1])
    #break
    
    # death check: you lose if you're where the robot is about to be
    if pmove[1] == 'robot' or pmove[1] == rmove[1]: # if you moved into the robot, or it moved into you
        print('*CLUNK* \n \n The robot ate you!')
        captured = True

    else:
        grid[r_xy[0]][r_xy[1]] = '.' # replace robot spot
        grid[p_xy[0]][p_xy[1]] = '.' # replace player spot
        
        grid[rmove[1][0]][rmove[1][1]] = 'R' # set robot location from rmove
        grid[pmove[1][0]][pmove[1][1]] = 'P' # set player location from pmove

        r_xy = rmove[1]
        p_xy = pmove[1]
       # this is the next move, gotta use it instead of print it
# check win condition - robot on your spot? Gotcha bitch

# end loop






    '''
    Day 1
    Robot needs to calc move, (I think it does that at the tuple unpack above)
    Once done, need to figure out how to actually take the step. Grab the step
    from the movelist, then figure out xy of that new spot. Wipe the old spot as
    '.', then write robot to new spot. 

    Mixed in there, get player motion via input(), then do both moves, then check 
    if they stand on the same square.

    Generalization - might be good to generalize the "find R, find P" routine 
    so I can use it to check palyer and robot position instead of JUST find 
    start pos. Also, printgrid should be a general function. 

    AFter that, get some graphics up in here, maybe make the map pick from a few 
    generated maps, maybe have more robots spawn (would have to make robot location
    more local to that robot, would need to make sure robots clear move with each other (oh!
    one moves, then other gets to calc move, that avoids moving on top of each other)


    Day 2:
    Ok, robot gets stuck on left right loops. Should maybe calc the SHORTEST path, given
    a left first, right first approach? Swap order of udlr logic, see if that fixes.
    '''