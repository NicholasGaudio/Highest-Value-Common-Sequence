from Functions.HelperFunctions import HVLCS
from Functions.HelperFunctions import findSubsequence
from Functions.Input import InputHandling
from Functions.Input import InputGenerator


def main():
    charValues = {}
    stringA = ""
    stringB = ""
    # charValues, stringA, stringB = InputHandling("src\\Inputs\\inputTest.txt", charValues, stringA, stringB)
    # print("String A: " + stringA)
    # print("String B: " + stringB)
    # test = HVLCS(charValues, stringA, stringB)
    # test.findHVLCS()
    InputGenerator("src\\Inputs\\inputTest1.txt")
    charValues, stringA, stringB = InputHandling("src\\Inputs\\inputTest1.txt", charValues, stringA, stringB)
    test = HVLCS(charValues, stringA, stringB)
    test.findHVLCS()
    return

if __name__ == "__main__":
    main()