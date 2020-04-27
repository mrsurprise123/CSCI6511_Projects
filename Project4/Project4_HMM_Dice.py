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
def readData(file):
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
        emissions.append(float(em))
    return Data(keepDice, emissionsProbs, emissions)
def main():
    print("Proejct4_YihanChen")
    filename = input("Please input the file name: ")
if __name__ == '__main__':
    main()