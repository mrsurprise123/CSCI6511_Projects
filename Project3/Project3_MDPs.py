# This is the Python project for CSCI66511
# @author Yihan chen
from copy import copy
class State:
    def __init__(self,x,y,terminal,value):
        self.x = x
        self.y = y
        self.terminal = terminal
        self.value = value
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
        for state in grid.values():
            if state.terminal:
                continue
            waiting_states = [copy(state), copy(state), copy(state), copy(state)]
            self.update(waiting_states[0], float(self.noises[0]), float(self.noises[1]), float(self.noises[3]), float(self.noises[2]), old_grid)
            self.update(waiting_states[1], float(self.noises[1]), float(self.noises[0]), float(self.noises[2]), float(self.noises[3]), old_grid)
            self.update(waiting_states[2], float(self.noises[3]), float(self.noises[1]), float(self.noises[0]), float(self.noises[2]), old_grid)
            self.update(waiting_states[3], float(self.noises[1]), float(self.noises[3]), float(self.noises[2]), float(self.noises[0]), old_grid)
            max_state = waiting_states[0]
            for waiting_state in waiting_states:
                if max_state.value < waiting_state.value:
                    max_state = waiting_state
            grid[(state.x, state.y)] = copy(max_state)
            del waiting_states
    def update(self,this_state, left, up, right, down,grid):
        up_row_index = this_state.x
        down_row_index = this_state.x
        left_col_index = this_state.y
        right_col_index = this_state.y
        final_result = 0
        if not up_row_index - 1 < 0:
            up_row_index -= 1
            final_result += (grid[(up_row_index, this_state.y)].value * up * self.discount)
        else:
            final_result += (this_state.value * up * self.discount)
        if down_row_index + 1 < self.gridsize:
            down_row_index += 1
            final_result += (grid[(down_row_index, this_state.y)].value * down * self.discount)
        else:
            final_result += (this_state.value * down * self.discount)
        if not left_col_index - 1 < 0:
            left_col_index -= 1
            final_result += (grid[(this_state.x, left_col_index)].value * left * self.discount)
        else:
            final_result += (this_state.value * left * self.discount)
        if right_col_index + 1 < self.gridsize:
            right_col_index += 1
            final_result += (grid[(this_state.x, right_col_index)].value * right * self.discount)
        else:
            final_result += (this_state.value * right * self.discount)
        this_state.value = final_result

def main():
    print("Proejct3_YihanChen")
    filename = input("Please input the file name ")
    k = input("Please input the value of k ")
    grid = Grid(filename,int(k))
    resultgrid = grid.value_iterations()
    grid.print_Grid(resultgrid)
if __name__ == '__main__':
    main()