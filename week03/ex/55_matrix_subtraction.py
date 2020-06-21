def matrix_subtraction(m1,m2): 
    k = l = m = 1
    res = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print("MATRIX 1:")
    for i in range(4):
        for j in range(4):
            print(m1[i][j], end=' ')
            if l % 4 == 0: 
                print("")
            l += 1
    print("")
    print("MATRIX 2:")
    for i in range(4):
        for j in range(4):
            print(m2[i][j], end=' ')
            if m % 4 == 0: 
                print("")
            m += 1
    print("")
    print("THE RESULT:")
    for i in range(4):
        for j in range(4):
            res[i][j] = m1[i][j] - m2[i][j]
            print(res[i][j], end=" ")
            if k % 4 == 0: 
                print("")
            k += 1

matrix_subtraction([[10,5,4,2],[5,10,9,55],[9,19,69,8],[7,8,4,75]],[[12,65,34,2],[1,5,8,45],[7,21,63,8],[0,78,4,65]])
