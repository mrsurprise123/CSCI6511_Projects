# This is the Python project4 for CSCI66511
# @author Yihan chen
class Data:
    def __init__(self, keepDice, emissionProbs, emissions):
        self.keepDice = keepDice
        self.emissionProbs = emissionProbs
        self.emissions = emissions
        self.notkeepDice = (1 - self.keepDice) / 2
        self.changeDice = {}
        for i in range(0,3):
            for j in range(0,3):
                if i == j:
                    self.changeDice[(i,j)] = self.keepDice
                else:
                    self.changeDice[(i,j)] = self.notkeepDice
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
    data.DataPrint()
    dices = [0, 1, 2]
    start_prob = [1.0 / 3, 1.0 / 3, 1.0 / 3]
    Probs = {}
    path = [[],[],[]]
    prob = -1.0
    dice = 0
    sequence = []
    for dice in dices:
        Probs[(dice,0)] = start_prob[dice] * data.emissionProbs[(dice,data.emissions[0]-1)]
        path[dice].append(dice)
    for j in range(1,len(data.emissions)):
        temp = [[],[],[]]
        for i in dices:
            tempprob = - 1.0
            for x in dices:
                newProbs = Probs[(x, j -1)] * data.changeDice[(x, i)] * data.emissionProbs[(i,data.emissions[j]-1)]
                if newProbs > tempprob:
                    tempprob = newProbs
                    Probs[(i,j)] = tempprob
                    temp[i] = path[x][0:j]
                    temp[i].append(i)
        path = temp
    for i in dices:
        if Probs[(i,len(data.emissions) - 1)] > prob:
            prob = Probs[(i,len(data.emissions) - 1)]
            dice = i
    for i in path[dice]:
        sequence.append(i+1)
    print("Most possible dices sequence:")
    print(sequence)
    print("Probability of path:")
    print(prob)
if __name__ == '__main__':
    main()