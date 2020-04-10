# This is the Python project for CSCI66511
# @author Yihan chen
from copy import copy
import itertools as it
import math

class State:
    def __init__(self,x,y,terminal,value,noises):
        self.x = x
        self.y = y
        self.terminal = terminal
        self.value = value
        self.noises = noises

    def Setnoise(self,noises):
        for i in range(0,4):
            self.noises[i] = noises[i]


class Grid:
    def __init__(self,filename,k):
        file = open(filename)
        lines = file.readlines()
        self.k = k
        self.gridsize = int(lines[0])
        self.discount = float(lines[1])
        self.noises = lines[2].split(', ')
        self.difference = 0.0001
        self.grid = {}
        if len(self.noises) < 4:
            self.noises.append(0)
        gridlines = lines[4:]
        for x, gridline in enumerate(gridlines):
            gridline = gridline.split('\n')[0]
            gridstates = gridline.split(',')
            for y, grid_state in enumerate(gridstates):
                value = 0.0
                terminal = False
                if grid_state != 'X':
                    terminal = True
                    value = int(grid_state)
                self.grid[(x,y)] = State(x,y,terminal,value,[float(self.noises[0]), \
                    float(self.noises[1]), float(self.noises[2]), float(self.noises[3])])
    
    def print_Grid(self,grid):
        print("Size:", str(self.gridsize))
        print("Discount:", str(self.discount))
        for x in range(0, self.gridsize):
            line = ''
            for y in range(0,self.gridsize):
                line += str(format(grid[(x,y)].value,'.2f')) + "\t"
            print(line)

    def iterations(self):
        ValueiterationGrid = copy(self.grid)
        PolicyiterationGrid = copy(self.grid)
        for i in range(0, self.k):
            self.value_iteration(ValueiterationGrid)
            self.policy_iteration(PolicyiterationGrid)
        return ValueiterationGrid,PolicyiterationGrid

    def policy_iteration(self,grid):
        old_grid = grid.copy()
        max_difference = 0
        for state in grid.values():
            if state.terminal:
                continue
            self.Equation(state,old_grid)
            max_difference = max(max_difference, abs(state.value - old_grid[state.x,state.y].value))
        if max_difference < self.difference:
            self.Policy_improvement(grid)

    def Policy_improvement(self,grid):
        old_grid = grid.copy()
        for state in grid.values():
            if state.terminal:
                continue
            temp_states = []
            for i in range(4):
                temp_states.append(State(state.x,state.y,state.terminal,state.value,[0,0,0,0]))
                for j in range(4):
                    temp_states[i].noises[(i+j)%4] = float(self.noises[j])
                self.Equation(temp_states[i],old_grid)
            max_state = self.Maxstates(temp_states)
            grid[(state.x, state.y)] = copy(max_state)
            del temp_states

    def Maxstates(self,states):
        max_state = states[0]
        for state in states:
            if max_state.value < state.value:
                max_state = state
        return max_state

    def value_iteration(self,grid):
        old_grid = grid.copy()
        noiseslist = list(it.permutations([float(self.noises[0]), float(self.noises[1]), float(self.noises[2]), float(self.noises[3])]))
        for state in grid.values():
            if state.terminal:
                continue
            temp_states = []
            for i in range(0,24):
                temp_states.append(State(state.x,state.y,state.terminal,state.value,noiseslist[i]))
                self.Equation(temp_states[i],old_grid)
            max_state = self.Maxstates(temp_states)
            grid[(state.x, state.y)] = copy(max_state)
            del temp_states
    def Equation(self,state, grid):
        final_result = 0
        if not state.y - 1 < 0:
            final_result += (grid[(state.x, state.y - 1)].value * state.noises[0] * self.discount)
        else:
            final_result += (state.value * state.noises[0] * self.discount)
        if not state.x - 1 < 0:
            final_result += (grid[(state.x - 1, state.y)].value * state.noises[1] * self.discount)
        else:
            final_result += (state.value * state.noises[1] * self.discount)
        if state.x + 1 < self.gridsize:
            final_result += (grid[(state.x + 1, state.y)].value * state.noises[2] * self.discount)
        else:
            final_result += (state.value * state.noises[2] * self.discount)
        if state.y + 1 < self.gridsize:
            final_result += (grid[(state.x, state.y + 1)].value * state.noises[3] * self.discount)
        else:
            final_result += (state.value * state.noises[3] * self.discount)
        state.value = final_result
        return final_result

def main():
    print("Proejct3_YihanChen")
    filename = input("Please input the file name ")
    k = input("Please input the value of k ")
    grid = Grid(filename,int(k))
    resultgrid = grid.iterations()
    valueiterationResult = resultgrid[0]
    policyiterationResult = resultgrid[1]
    grid.print_Grid(valueiterationResult)
    grid.print_Grid(policyiterationResult)

if __name__ == '__main__':
    main()