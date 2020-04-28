# This is the Python project4 for CSCI66511
# @author Yihan chen
class Data:
    def __init__(self, keepDice, emissionProbs, emissions):
        self.keepDice = keepDice
        self.emissionProbs = emissionProbs
        self.emissions = emissions
        self.notkeepDice = (1 - self.keepDice) / 2
    def DataPrint(self):
        print(self.keepDice)
        print(self.emissionProbs)
        print(self.emissions)
def readData(filename):
    file = open(filename)
    lines = []
    for line in file.readlines():
        if line[0] == '#':
            continue
        lines.append(line)
    keepDice = float(lines[0])
    eProbs = lines[1:4]
    emissionsProbs = {}
    for x, eProbLine in enumerate(eProbs):
        eProbLine = eProbLine.split('\n')[0]
        p = eProbLine.split(' ')
        for y, prob in enumerate(p):
            emissionsProbs[(x,y)] = float(prob)
    emissions = []
    emissionsLine = lines[4].split('\n')[0]
    for em in emissionsLine.split(','):
        emissions.append(int(em))
    return Data(keepDice, emissionsProbs, emissions)
def main():
    print("Proejct4_YihanChen")
    # filename = input("Please input the file name: ")
    data = readData("./01.txt")
    # data.DataPrint()
    dices = [0, 1, 2]
    start_p = [1.0 / 3, 1.0 / 3, 1.0 / 3]
    trans_p = {}
    emis_p = {}
    for i in range(0,3):
        for j in range(0,3):
            if i == j:
                trans_p[(i,j)] = data.keepDice
            else:
                trans_p[(i,j)] = data.notkeepDice
            emis_p[(i,j)] = data.emissionProbs[(i,j)]
    maxProb = {}
    path = [[],[],[]]
    for dice in dices:
        maxProb[(dice,0)] = start_p[dice] * emis_p[(dice,data.emissions[0]-1)]
        path[dice].append(dice)
    
    for j in range(1,len(data.emissions)):
        temp = [[],[],[]]
        for i in dices:
            prob = - 1.0
            for x in dices:
                newProbs = maxProb[(x, j -1)] * trans_p[(x, i)] * emis_p[(i,data.emissions[j]-1)]
                if newProbs > prob:
                    prob = newProbs
                    curDice = x
                    maxProb[(i,j)] = prob
                    temp[i] = path[curDice][0:j]
                    temp[i].append(i)
        path = temp
    prob = -1.0
    dice = 0
    for i in dices:
        if maxProb[(i,len(data.emissions) - 1)] > prob:
            prob = maxProb[(i,len(data.emissions) - 1)]
            dice = i
    result = []
    for i in path[dice]:
        result.append(i+1)
    print("Most possible dices sequence:")
    print(result)
    print("Probability of path:")
    print(prob)
if __name__ == '__main__':
    main()