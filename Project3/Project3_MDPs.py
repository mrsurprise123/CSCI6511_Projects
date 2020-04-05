# This is the Python project for CSCI66511
# @author Yihan chen
class State:
    def __init__(self,x,y,terminal,value):
        self.x = x
        self.y = y
        self.terminalState = terminalState
        self.value = value
class Grid:
    def __init__(self,filename):
        file = open(filename)
        lines = file.readlines()
        self.gridsize = int(lines[0])
        self.discount = float(lines[1])
        self.noises = lines[2].split(', ')
        self.grid = {}
        if len(self.noises) < 4:
            noises.append(0)
        gridlines = lines[4:]
        for x,gridline in enumerate(gridlines):
            gridline = gridline.lstrip()
            gridstates = gridline.split(',')
            for y, grid_state in enumerate(gridstates):
                value = 0.0
                terminal = False
                if grid_state != 'X':
                    terminal = True
                    value = int(grid_state)
                self.grid[(x,y)] = State(x,y,terminal,value)
    def print_Grid(self):
        print("Size:" + str(self.gridsize))
        print("Discount" + str(self.discount))
        for x in range(0,self.gridsize):
            line = ''
            for y in range(0,self.gridsize):
                line = str(self.grid[(x,y)].value + 0.00) + ' '
            print(line)
def main():
    print("Proejct3_YihanChen")
if __name__ == '__main__':
    main()