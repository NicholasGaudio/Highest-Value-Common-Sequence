def findSubsequence(subA, B):
    #print(f"subA = {subA}")
    index = 0
    if (len(subA) == 0):
        return True
    
    for i in range(len(B)):
        if B[i] == subA[index]:
            index += 1
            if index == len(subA):
                return True
    return False

class HVLCS:
    stringA = ""
    stringB = ""
    maxValue = 0

    #Test Dictionary for Character Values - Hardcoded for Now
    charValues = {}
    
    # Dictionary that is built during runtime
    # Store the values as keys and the subsequence correlated to that as a value
    evilMap = {}
    oldEvilMap = {0: ""}

    def __init__(self, charValues, stringA, stringB):
        self.charValues = charValues
        self.stringA = stringA
        self.stringB = stringB
        self.evilMap = {}
        self.sequences = {}

    def tester(self):
        print(f"Test Constructor:\nString A: {self.stringA} | String B: {self.stringB}\n")
        self.maxValue = self.OPT(0, 0)
        print(self.maxValue)

    # goes through to find HVLCS value but doesn't get actual HVLCS
    def OPT(self, i, j):
        if (i, j) in self.evilMap:
            return self.evilMap[(i, j)]
        
        if (i == len(self.stringA) or j == len(self.stringB)):
            return 0

        value = 0
        if (self.stringA[i] == self.stringB[j]):
            value = (self.charValues[self.stringA[i]] + self.OPT(i+1, j+1))
        
        else:
            v1 = self.OPT(i+1, j)
            v2 = self.OPT(i, j+1)
            value = (max(v1, v2))

        self.evilMap[(i, j)] = value
        return value
    
    # Runs after OPT to find the subsequence through backtracking
    def backtrack(self):
        i = 0
        j = 0
        subsequence = ""
        while i < (len(self.stringA)) and j < (len(self.stringB)):
            if (self.stringA[i] == self.stringB[j]):
                subsequence += self.stringA[i]
                i+=1
                j+=1
            else:
                if i+1 < len(self.stringA) and j+1 < len(self.stringB):
                    if self.evilMap[(i+1, j)] > self.evilMap[(i, j+1)]:
                        i+=1
                    else:
                        j+=1
                else:
                    if i+1 < len(self.stringA):
                        i+=1
                    else:
                        if j+1 < len(self.stringB):
                            j+=1
                        else:
                            break
        return subsequence


    def findHVLCS(self):
        print(f"{self.OPT(0, 0)}\n{self.backtrack()}")
        return