def linearSearchCount(myArray, targetValue):
    comparisonsMade = 0
    sizeArray = len(myArray)

    for indexPos in range(sizeArray):
        comparisonsMade += 1
        if myArray[indexPos] == targetValue:
            return comparisonsMade
    return comparisonsMade

dataArray = [12, 45, 23, 51, 19, 8, 33]
searchFor = 19
print("Comparaciones realizadas:", linearSearchCount(dataArray, searchFor))
 