def findSubsequence(subA, B):
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
    charValues = {
        'a' : 2, 
        'b' : 4,
        'c' : 5,
        'd' : 17,
        'e' : 1,
        'f' : 3 
        }
    
    # Dictionary that is built during runtime
    # Store the values as keys and the subsequence correlated to that as a value
    evilMap = {0 : ""}

    def __init__(self, stringA, stringB):
        self.stringA = stringA
        self.stringB = stringB

    def tester(self):
        print(f"Test Constructor:\nString A: {self.stringA} | String B: {self.stringB}\n")
        self.maxValue = self.OPT(0, 0, "")
        print(self.maxValue)


    # v is the running value that will be tracked throughout this
    # j is the index in stringA which we are looking
    def OPT(self, v, j, substring):
        if j == len(self.stringA):
            return 0

        # If the subsequence + the next character is a subsequence in stringB check whether to add it or not
        if findSubsequence(substring + self.stringA[j], self.stringB):
            v =  max(v + self.charValues[self.stringA[j]] + self.OPT(v, j+1, substring + self.stringA[j]),
                      v + self.OPT(v, j+1, substring))
            substring += self.stringA[j]
            self.evilMap[v] = substring
            print(f"TRUE | j: {j} | Value V: {v} | Map: {self.evilMap[v]} | Substring: {substring}")

        else:
            v = self.OPT(v, j+1, substring)
            # self.evilMap[v] = substring
            print(f"FALSE | j: {j} | Value V: {v} | Map: {self.evilMap[v]} | Substring: {substring}")

        return v

    def findHVLCS(self):
        print(f"Maximum Value Common Subsequence for - String A: {self.stringA} | String B: {self.stringB}\n")
        self.maxValue = self.OPT(0, 0, "")
        print(f"Max Value: {self.maxValue}\nHVCLS: {self.evilMap[self.maxValue]}")
        return