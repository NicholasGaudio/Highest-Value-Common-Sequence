# Highest-Value-Common-Sequence

## Q1 - Empirical Comparison
![Chart showing runtimes over 10 trials](/Images//Runtime.png)

## Q2 - Recurrence Equation

Def: OPT(i, j) finds the maximum value of the HVLCS between string A and string B from i, ..., len(A) - 1 where i is the current index in A and j, ..., len(B) - 1 where j is the current index in B

![OPT Equation](/Images/OPTEquation.png)

This OPT equation covers 3 cases: 
1) The base case for when the i or j reaches the end of A or B respectively and there can no longer be any additions to the subsequence.
2) The case where A[i] and B[j] match and the value of that matched character is added to the OPT of all following indexes
3) The case where A[i] != B[j] and the optimal value is the maximum value between OPT(i+1, j) and OPT(i, j+1)

This covers all potential cases. At each index pairing the value can be stored for future reference, meaning that the entire process doesn't need to be repeated once the pair has been reached once.

## Q3 - Big Oh

### Pseudocode:
//These all exist within a class that stores A, B, and dictionaries M for memoization and C for character values
//The user initializes those values with the given strings and calls HVLCS

OPT(i, j):
    if (i, j) in M:
            return M[(i, j)]
        
        if (i == len(A) or j == len(B)):
            return 0

        value = 0
        if (A[i] == B[j]):
            value = (C[A[i]] + OPT(i+1, j+1))
        
        else:
            v1 = OPT(i+1, j)
            v2 = OPT(i, j+1)
            value = (max(v1, v2))

        M[(i, j)] = value
        return value

backtrack():
    i = 0
    j = 0
    subsequence = ""
    while i < (len(A)) and j < (len(B)):
        if (A[i] == B[j]):
            subsequence += A[i]
            i+=1
            j+=1
        else:
            if i+1 < len(A) and j+1 < len(B):
                if M[(i+1, j)] > M[(i, j+1)]:
                    i+=1
                else:
                    j+=1
            else:
                if i+1 < len(A):
                    i+=1
                else:
                    if j+1 < len(B):
                        j+=1
                    else:
                        break
    return subsequence

findHVLCS(self):
        print(f"{OPT(0, 0)}\n{backtrack()}")
        return

### Runtime:
The Runtime for the algorithm would be O(n * m) where n is the length of string A and m is the length of string B. This is because in the worst case scenario where no characters are shared, the program will go through every index combination of A and B before realizing this making OPT(n * m). Backtracking is only O(n) since it is a single loop that runs through the memoization dictionary and is outscaled by the OPT function.