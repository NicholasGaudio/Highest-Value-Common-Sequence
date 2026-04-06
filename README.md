# Highest-Value-Common-Sequence

## Q1 - Empirical Comparison
![Chart showing runtimes over 10 trials](/Images//Runtime.png)

## Q2 - Recurrence Equation

Def: OPT(j) finds the maximum value v of a subsequence of characters j, ..., len(A) in string A that also exists as a subsequence in string B
OPT = {0; OPT(j+1); max{value(j) + OPT(j+1), OPT(j+1)}}