from Functions.HelperFunctions import HVLCS
from Functions.HelperFunctions import findSubsequence
from Functions.InputReader import InputHandling


def main():
    charValues = {}
    stringA = ""
    stringB = ""
    charValues, stringA, stringB = InputHandling("src\\Inputs\\inputTest.txt", charValues, stringA, stringB)
    print("String A: " + stringA)
    print("String B: " + stringB)
    test = HVLCS(charValues, stringA, stringB)
    test.findHVLCS()
    return

if __name__ == "__main__":
    main()