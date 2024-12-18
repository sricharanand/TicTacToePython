class TicTacToe:
    def __init__(self,player1,player2):
        self.board=[
                    [" "," "," "],
                    [" "," "," "],
                    [" "," "," "]
                    ]
        #will be a 2D list (3x3)
        self.player='X'
        #x starts by default

        self.player1 = player1
        self.player2 = player2
        self.winner = None
        #all are attributes in the class

    def makemove(self,row,column):

        if self.board[row][column] == " ":
        #if the cell is empty
            self.board[row][column] = self.player
            #update the cell with the mark (self.player)

            if not self.is_winner():
            #if there is no win/draw
            #  chaning the turns
                if self.player == "X":
                    self.player = "O"
                else:
                    self.player = "X"

            # showing the changes that has been done in the board
            for i in self.board:
                print(i)
            print("\n")
        else:
            raise ValueError("Cell is already filled.")

    def is_winner(self):

        for row in range(3):
            for col in range(3):
        #iterating across the whole board
                if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                #matching in row
                    if self.player == "X":
                        # print(f"{self.player1} wins")
                        self.winner = self.player1
                    else:
                        self.winner = self.player2
                    return True

                elif self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                #matching in column
                    if self.player == "X":
                        self.winner = self.player1
                    else:
                        self.winner = self.player2
                    return True

                elif self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
                #matching in diagonal
                    if self.player == "X":
                       self.winner = self.player1
                    else:
                        self.winner = self.player2
                    return True

                # else:
                #     return False
                #game continues
    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)
