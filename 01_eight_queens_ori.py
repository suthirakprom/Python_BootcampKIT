class NQueens:
    def __init__(self, N):
        self.N = N    #4
        self.solutions = 0
        self.boardSolver()

    def toPlaceOrNotToPlace(self, location, row, col): #4 0 0/1/2/3
        for i in range(row):
            if location[i] - i == col - row or location[i] + i == col + row or location[i] == col:
                return False
        return True


    def place_queen(self, location, row):    #4 0
        if row == self.N: #0 != 4
            self.show_full_board(location)
            self.solutions += 1
        else:
            for col in range(self.N): #4
                if self.toPlaceOrNotToPlace(location, row, col):  #4 0 0/1/2/3    #loop 4 times 
                    location[row] = col
                    self.place_queen(location, row + 1)

    def boardSolver(self):
            location = [-1] * self.N #4
            self.place_queen(location, 0)   #4 0
            print("Found", self.solutions, "solutions.")

    def show_full_board(self, positions):
        for i in range(self.N):
            row = ""
            for j in range(self.N):
                if positions[i] == j:
                    row += "Q "
                else:
                    row += "- "
            print(row)
        print("")
        


NQueens(4)

