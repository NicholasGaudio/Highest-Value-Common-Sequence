from Functions.HelperFunctions import HVLCS
from Functions.HelperFunctions import findSubsequence
from Functions.InputReader import InputHandling


def main():
    InputHandling("inputTest.txt")
    test = HVLCS("baac", "bcaa")
    test.findHVLCS()
    return

if __name__ == "__main__":
    main()