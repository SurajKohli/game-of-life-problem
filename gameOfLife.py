import numpy as np

def fateOfCell(i,j,n):
    # print("i " + str(i) + " j " + str(j))
    neighAliveCount = 0
    # limits for the value of neighbouring cells
    a = i-1 if i-1 >= 0 else i
    b = i+1 if i+1 < n else i
    c = j-1 if j-1 >= 0 else j
    d = j+1 if j+1 < n else j

    for x in range(a,b+1):
        for y in range(c,d+1):
            if ( x==i ) and ( y==j ):
                pass
            elif ( Matrix[x][y] == '*' ):
                # print("incrementing neighbour")
                neighAliveCount = neighAliveCount + 1

    if (( Matrix[i][j] == '0' ) and ( neighAliveCount == 3 )): # cell is dead
        Matrix[i][j] = '*' # cell becomes alive
    elif (( Matrix[i][j] == '*' ) and ( (neighAliveCount == 2) or (neighAliveCount == 3) )): # cell alive and neigh 2 or 3
        pass # cell lives
    elif (( Matrix[i][j] == '*' ) and ( (neighAliveCount < 2) or (neighAliveCount > 3) )): # cell alive and neigh < 2 or > 3
        Matrix[i][j] = '0' # cell dies
    else:
        pass



def runSingleGeneration(Matrix):
    n = len(Matrix)
    for i in range(n):
        for j in range(n):
            fateOfCell(i,j,n)


    # print(Matrix)
    # print(np.matrix(Matrix))

def runGenerations(Matrix,g):
    for x in range(g):
        runSingleGeneration(Matrix)
        print("Matrix After Generation " + str(x+1) + ": ")
        print(np.matrix(Matrix))


if __name__ =='__main__':
    print("----- Welcome To The Game Of Life -----")
    # Orthogonal Matrix
    print("Please Enter Size of The Universe/Matrix/Grid: ")
    n = int(input())
    Matrix = [ [ '0' for i in range(n)] for i in range(n) ]
    # Matrix[5][5] = '*'
    # Matrix[5][6] = '*'
    # Matrix[6][5] = '*'
    # Matrix[6][6] = '*'
    # Matrix[6][7] = '*'
    # Matrix[5][8] = '*'
    # Matrix[8][5] = '*'
    # Matrix[6][8] = '*'
    # Matrix[6][9] = '*'
    # Matrix[2][2] = '*'
    # Matrix[1][1] = '*'
    # Matrix[1][0] = '*'
    # Matrix[0][0] = '*'
    print("Please Enter the values in the Universe/Matrix where you want a cell to live (rest all cells would be empty/dead): ")
    print("Enter 'done' to start generation!")
    while(True):
        inp = input()
        if( inp == "done" ):
            break
        else:
            Mx,My = inp.split()
            Matrix[int(Mx)][int(My)] = '*'
            print(np.matrix(Matrix))

    print("Please Enter number of generations: ")
    g = int(input())

    print("\n")
    print("---Initial Universe/seed system---")
    print(np.matrix(Matrix))
    print("\n")
    runGenerations(Matrix,g)
    # print(np.matrix(Matrix))
