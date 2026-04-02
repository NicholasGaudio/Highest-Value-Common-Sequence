def findSubsequence(subA, B):
    index = 0
    for i in range(len(B)):
        if B[i] == subA[index]:
            index += 1
            if index == len(subA):
                return True

    return False

