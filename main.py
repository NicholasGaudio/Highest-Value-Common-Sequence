from HelperFunctions import findSubsequence
from HelperFunctions import HVLCS


def main():
    test = HVLCS("acbdbef", "dcfebbfca")
    test.findHVLCS()
    return

if __name__ == "__main__":
    main()