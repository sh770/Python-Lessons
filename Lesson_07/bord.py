## build a board class to represent the board of a standard board game
## the board is a 2D array of 0s

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        # self.matrix = [["0" for i in range(self.cols)] for j in range(self.rows)]
        # pass             
        

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join([str(elem) for elem in row]) + "\n"
        return result



def main():
    b = Board(8, 8)
    print(b) # should print a 8x8 board 
    """
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
    """
main()