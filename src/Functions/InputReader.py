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