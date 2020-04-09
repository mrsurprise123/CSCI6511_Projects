# This is the Python project for CSCI66511
# @author Yihan chen
from copy import copy
import itertools as it
class State:
    def __init__(self,x,y,terminal,value):
        self.x = x
        self.y = y
        self.terminal = terminal
        self.value = value
    def Setnoise(self,noises):
        self.noises = noises

class Grid:
    def __init__(self,filename,k):
        file = open(filename)
        lines = file.readlines()
        self.k = k
        self.gridsize = int(lines[0])
        self.discount = float(lines[1])
        self.noises = lines[2].split(', ')
        self.grid = {}
        if len(self.noises) < 4:
            self.noises.append(0)
        gridlines = lines[4:]
        for x,gridline in enumerate(gridlines):
            gridline = gridline.split('\n')[0]
            gridstates = gridline.split(',')
            for y, grid_state in enumerate(gridstates):
                value = 0.0
                terminal = False
                if grid_state != 'X':
                    terminal = True
                    value = int(grid_state)
                self.grid[(x,y)] = State(x,y,terminal,value)
    def print_Grid(self,grid):
        print("Size:" + str(self.gridsize))
        print("Discount" + str(self.discount))
        for x in range(0,self.gridsize):
            line = ''
            for y in range(0,self.gridsize):
                line += str(format(grid[(x,y)].value,'.2f')) + ' '
            print(line)
    def value_iterations(self):
        grid = copy(self.grid)
        for i in range(0,self.k):
            self.value_iteration(grid)
        return grid
    def value_iteration(self,grid):
        old_grid = grid.copy()
        noiseslist = list(it.permutations([float(self.noises[0]), float(self.noises[1]), float(self.noises[2]), float(self.noises[3])]))
        for state in grid.values():
            if state.terminal:
                continue
            waiting_states = []
            for i in range(0,24):
                waiting_states.append(State(state.x,state.y,state.terminal,state.value))
            for i in range(0,24):
                waiting_states[i].Setnoise(noiseslist[i])
                self.update(waiting_states[i],old_grid)
            max_state = waiting_states[0]
            for waiting_state in waiting_states:
                if max_state.value < waiting_state.value:
                    max_state = waiting_state
            grid[(state.x, state.y)] = copy(max_state)
            del waiting_states
    def update(self,state, grid):
        final_result = 0
        if not state.y - 1 < 0:
            final_result += (grid[(state.x, state.y - 1)].value * state.noises[0] * self.discount)
        else:
            final_result += (state.value * state.noises[0] * self.discount)
        if not state.x - 1 < 0:
            final_result += (grid[(state.x - 1, state.y)].value * state.noises[1] * self.discount)
        else:
            final_result += (state.value * state.noises[1] * self.discount)
        if state.y + 1 < self.gridsize:
            final_result += (grid[(state.x, state.y + 1)].value * state.noises[2] * self.discount)
        else:
            final_result += (state.value * state.noises[2] * self.discount)
        if state.x + 1 < self.gridsize:
            final_result += (grid[(state.x + 1, state.y)].value * state.noises[3] * self.discount)
        else:
            final_result += (state.value * state.noises[3] * self.discount)
        state.value = final_result

def main():
    print("Proejct3_YihanChen")
    filename = input("Please input the file name ")
    k = input("Please input the value of k ")
    grid = Grid(filename,int(k))
    resultgrid = grid.value_iterations()
    grid.print_Grid(resultgrid)
if __name__ == '__main__':
    main()