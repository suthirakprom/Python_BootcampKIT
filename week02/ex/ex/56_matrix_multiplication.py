def matrix_multiplication(m1,m2):
    res = [[0,0,0],[0,0,0],[0,0,0]]
    k = l = m = 1
    print("MATRIX 1:")
    for i in range(3):
        for j in range(3):
            print(m1[i][j], end=" ")
            if l % 3 == 0: 
                print("")
            l += 1
    print("")
    print("MATRIX 2:")
    for i in range(3):
        for j in range(3):
            print(m2[i][j], end=" ")
            if m % 3 == 0: 
                print("")
            m += 1
    print("")
    print("THE RESULT:")
    for i in range(3):
        for j in range(3):
            res[i][j] = m1[i][j] * m2[i][j]
            print(res[i][j], end=" ")
            if k % 3 == 0: 
                print("")
            k += 1

matrix_multiplication([[10,5,4],[5,10,9],[9,19,8]],[[12,11,5],[1,5,8],[7,13,15]])
