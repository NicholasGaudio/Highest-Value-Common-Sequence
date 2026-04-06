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
    evilMap = {0 : ""}

    def __init__(self, charValues, stringA, stringB):
        self.charValues = charValues
        self.stringA = stringA
        self.stringB = stringB

    def tester(self):
        print(f"Test Constructor:\nString A: {self.stringA} | String B: {self.stringB}\n")
        self.maxValue = self.OPT(0, 0)
        print(self.maxValue)


    # v is the running value that will be tracked throughout this
    # j is the index in stringA which we are looking
    def OPT(self, v, j):
        substring = self.evilMap[v]
        if j == len(self.stringA):
            #print(f"v: {v} | substring: {substring}")
            return 0

        # If the subsequence + the next character is a subsequence in stringB check whether to add it or not
        if findSubsequence(substring + self.stringA[j], self.stringB):
            self.evilMap[v + self.charValues[self.stringA[j]]] = substring + self.stringA[j]
            v =  max(self.charValues[self.stringA[j]] + self.OPT(v + self.charValues[self.stringA[j]], j+1),
                      self.OPT(v, j+1))
        else:
            v = self.OPT(v, j+1)

        return v

    def findHVLCS(self):
        #print(f"Maximum Value Longest Common Subsequence for - String A: {self.stringA} | String B: {self.stringB}")
        self.maxValue = self.OPT(0, 0)
        print(f"{self.maxValue}")
        print(f"{self.evilMap[self.maxValue]}")
        return