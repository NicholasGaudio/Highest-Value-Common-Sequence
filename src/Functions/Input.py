import random

def InputHandling(filepath, charValues, stringA, stringB):
    with open(filepath, 'r') as input:
        lines = input.readlines()

    rows = []
    for line in lines:
        rows.append(line.strip().split())
    try:
        k = int(rows[0][0])
    except (IndexError, ValueError):
        print("Error: Invalid input format.")
        return
    
    # Ensure # rows matches
    if (len(rows) != k + 3):
        print("Error: Number of rows does not match the number of rows required in the input file.")
        return
    
    for i in range(1, k + 1):
        try:
            charValues[rows[i][0]] = int(rows[i][1])
        except (IndexError, ValueError):
            print("Error: Invalid input format for character values.")
            return
    stringA = rows[k + 1][0]
    stringB = rows[k + 2][0]
    
    return charValues, stringA, stringB


def InputGenerator(filename,):
    ## create input like the one in the inputTest.txt file but strings of at least 25 chars
    
    # set a random k (number of defined chars)
    k = random.randint(1, 25)
    print(f"k: {k}")

    with open(filename, "w") as f:
        f.write(f"{k}\n")

        # create a random amount of chars and values = to k
        charValues = {}
        while len(charValues) < k:
            char = chr(random.randint(97, 122)) # random lowercase letter
            if char in charValues:
                continue
            value = random.randint(1, 10) # random value between 1 and 10
            charValues[char] = value
            f.write(f"{char} {value}\n")
        
        # create two random strings of at least 25 chars using the defined chars
        chars = list(charValues.keys())
        stringA = ''.join(random.choice(chars) for _ in range(25))
        stringB = ''.join(random.choice(chars) for _ in range(25))
        f.write(f"{stringA}\n")
        f.write(f"{stringB}\n")



    
    
