#Chawarat Iampramoon 5980028
#Tommy Egnehall 5980011
from decimal import *
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return float(n * multiplier) / multiplier
def displayFunc(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

def gauss(A):
    n = len(A)
    for i in range(0, n):
        # Search for max value in the column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap max row with the  current row (one column at a time)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below the current column = 0
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve for upper triangle
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


if __name__ == "__main__":
    n = eval(input())
    A = [[0 for j in range(n+1)] for i in range(n)]

    # Read the input
    for i in range(0, n):
        line = list(map(Decimal, input().split(" ")))
        for j, el in enumerate(line):
            A[i][j] = el
    input()

    line = input().split(" ")
    lastLine = list(map(Decimal, line))
    for i in range(0, n):
        A[i][n] = lastLine[i]

    # Display the input
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

    # Calculation
    #x = gauss(A)
    n = len(A)

    for i in range(0, n):
        # Search for max value in the column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap max row with the  current row (one column at a time)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below the current column = 0
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve for upper triangle
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    #return x
    # Print final result
    line = "Answer:\t"
    for i in range(0, n):
        line += str(truncate(x[i],5)) + " \t"
    print (line)
