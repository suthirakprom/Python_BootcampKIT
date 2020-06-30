def eight_queen(N):  
    try:

        def show_full_board(positions):  
            for i in range(N):
                row = ""
                for j in range(N):
                    if positions[i] == j:
                        row += "Q "
                    else:
                        row += "- "
                print(row)
            print("")
            

        def toPlaceOrNotToPlace(location, row, col): 
            for i in range(row):
                if location[i] - i == col - row or location[i] + i == col + row or location[i] == col:
                    return False
            return True
        
        def place_queen(location, row):  
            
            if row == N: 
                show_full_board(location)
            
            else:
                for col in range(N): 
                    if toPlaceOrNotToPlace(location, row, col):   
                        location[row] = col
                        
                        # print(location)
                        # print('1')
                        place_queen(location, row + 1)

        def boardSolver():
            location = [0] * N 
            place_queen(location, 0) 

        boardSolver()

        return 1        
        
    except: 
        return 0


eight_queen(4)

