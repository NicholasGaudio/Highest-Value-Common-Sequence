from Functions.HelperFunctions import HVLCS
from Functions.HelperFunctions import findSubsequence
from Functions.Input import InputHandling
from Functions.Input import InputGenerator
import time


def main():
    charValues = {}
    stringA = ""
    stringB = ""
    Q1 = False
    ManualTest = True

    if ManualTest:
        charValues, stringA, stringB = InputHandling("src\\Inputs\\manualTest.txt", charValues, stringA, stringB)
        test = HVLCS(charValues, stringA, stringB)
        test.findHVLCS()

    if Q1: 
        fileTimes = []
        Q1_start = time.time()
        for i in range(1, 11):
            filename = f"src\\Inputs\\input{i}.txt"
            InputGenerator(filename)
            charValues, stringA, stringB = InputHandling(filename, charValues, stringA, stringB)
            test = HVLCS(charValues, stringA, stringB)
            start_time = time.time()
            test.findHVLCS()
            end_time = time.time()
            fileTimes.append(end_time - start_time)
        Q1_end = time.time()
        print(f"Total time taken for Q1: {Q1_end - Q1_start} seconds")
        for i in range(1, 11):
            print(f"Time taken for file {i}: {fileTimes[i-1]} seconds")
        
    return

if __name__ == "__main__":
    main()