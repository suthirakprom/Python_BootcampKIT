def matrix_multiplication(m1,m2):
    if len(m1) != len(m2):
        print("Error")
    else:
        res = [[0,0,0],[0,0,0],[0,0,0]]
        temp = 0
        sum = 0 
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
        k = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    res[i][j] += m1[i][k] * m2[k][j]
                print(res[i][j], end=' ')
                
                if l % 3 == 0:
                    print('')
                l += 1

matrix_multiplication([[3,7,5],[2,6,7],[4,3,2]],[[6,5,4],[3,2,1],[1,2,3]])
