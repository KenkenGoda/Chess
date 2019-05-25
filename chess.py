#chess.py
import numpy as np

class ChessBoard:
    
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board_i = []
        for i in range(8):
            board_j = []
            for j in range(8):
                board_j.append(".")
            board_i.append(board_j)
        board_i[7][0] = "R1"
        board_i[7][1] = "N1"
        board_i[7][2] = "B1"
        board_i[7][3] = "WQ"
        board_i[7][4] = "WK"
        board_i[7][5] = "B2"
        board_i[7][6] = "N2"
        board_i[7][7] = "R2"
        board_i[6][0] = "P1"
        board_i[6][1] = "P2"
        board_i[6][2] = "P3"
        board_i[6][3] = "P4"
        board_i[6][4] = "P5"
        board_i[6][5] = "P6"
        board_i[6][6] = "P7"
        board_i[6][7] = "P8"
        board_i[0][0] = "r1"
        board_i[0][1] = "n1"
        board_i[0][2] = "b1"
        board_i[0][3] = "Bq"
        board_i[0][4] = "Bk"
        board_i[0][5] = "b2"
        board_i[0][6] = "n2"
        board_i[0][7] = "r2"
        board_i[1][0] = "p1"
        board_i[1][1] = "p2"
        board_i[1][2] = "p3"
        board_i[1][3] = "p4"
        board_i[1][4] = "p5"
        board_i[1][5] = "p6"
        board_i[1][6] = "p7"
        board_i[1][7] = "p8"
        return board_i

class WhiteKing(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 4
        self.symbol = "WK"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for WK")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if (abs(self.position_i-destination_j)<2 and abs(self.position_j-destination_j)<2):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteQueen(ChessBoard):
    
    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 3
        self.symbol = "WQ"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for WQ")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if (destination_i == self.position_i or destination_j == self.position_j or abs(self.position_i-destination_i) == abs(self.position_j-destination_j)):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteRook1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 0
        self.symbol = "R1"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for R1")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if (destination_i == self.position_i or destination_j == self.position_j):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteRook2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 7
        self.symbol = "R2"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for R2")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if (destination_i == self.position_i or destination_j == self.position_j):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteBishop1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 2
        self.symbol = "B1"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for B1")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if abs(self.position_i-destination_i) == abs(self.position_j-destination_j):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteBishop2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 5
        self.symbol = "B2"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for B2")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if abs(self.position_i-destination_i) == abs(self.position_j-destination_j):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteKnight1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 1
        self.symbol = "N1"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for N1")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if abs(self.position_i-destination_i)**2 + abs(self.position_j-destionation_j)**2 == 5:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhiteKnight2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 6
        self.symbol = "N2"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for N2")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if abs(self.position_i-destination_i)**2 + abs(self.position_j-destionation_j)**2 == 5:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass
                    
class WhitePone1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 6
        self.position_j = 0
        self.symbol = "P1"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P1")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 6
        self.position_j = 1
        self.symbol = "P2"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P2")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone3(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 6
        self.position_j = 2
        self.symbol = "P3"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P3")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone4(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 6
        self.position_j = 3
        self.symbol = "P4"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P4")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone5(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 4
        self.position_j = 1
        self.symbol = "P5"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P5")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone6(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 5
        self.position_j = 1
        self.symbol = "P6"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P6")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone7(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 6
        self.position_j = 1
        self.symbol = "P7"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P7")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class WhitePone8(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 7
        self.position_j = 1
        self.symbol = "P8"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for P8")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if destination_i == self.position_i and destination_j-self.position_j == 1:
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass


class BlackKing(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 0
        self.position_j = 4
        self.symbol = "Bk"

    def move(self):
        while True:
            try:
                print("give a i and j coordinate for Bk")
                destination_i = int(input())
                destination_j = int(input())
                if self.board[destination_i][destination_j] == ".":
                    if (abs(self.position_i - destination_i) < 2 and abs(self.position_j-destination_j) < 2):
                        self.board[self.position_i][self.position_j] = "."
                        self.position_i = destination_i
                        self.position_j = destination_j
                        self.board[self.position_i][self.position_j] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackQueen(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_i = 0
        self.position_j = 3
        self.symbol = "Bq"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for Bq")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if (destination_x == self.position_x or destination_y == self.position_y or abs(self.position_x-destination_x) == abs(self.position_y-destination_y)):
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackRook1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 0
        self.position_y = 0
        self.symbol = "r1"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for r1")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if (destination_x == self.position_x or destination_y == self.position_y):
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackRook2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 0
        self.position_y = 7
        self.symbol = "r2"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for r2")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if (destination_x == self.position_x or destination_y == self.position_y):
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackBishop1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 0
        self.position_y = 2
        self.symbol = "b1"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for b1")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if abs(self.position_x-destination_x) == abs(self.position_y-destination_y):
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackBishop2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 0
        self.position_y = 5
        self.symbol = "b2"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for b2")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if abs(self.position_x-destination_x) == abs(self.position_y-destination_y):
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackKnight1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 1
        self.position_y = 7
        self.symbol = "n1"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for n1")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if abs(self.position_x-destination_x)**2 + abs(self.position_y-destionation_y)**2 == 5:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackKnight2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 6
        self.position_y = 7
        self.symbol = "n2"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for n2")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if abs(self.position_x-destination_x)**2 + abs(self.position_y-destionation_y)**2 == 5:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone1(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 0
        self.position_y = 6
        self.symbol = "p1"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p1")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone2(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 1
        self.position_y = 0
        self.symbol = "p2"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p2")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone3(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 2
        self.position_y = 0
        self.symbol = "p3"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p3")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone4(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 3
        self.position_y = 0
        self.symbol = "p4"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p4")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone5(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 4
        self.position_y = 0
        self.symbol = "p5"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p5")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone6(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 5
        self.position_y = 0
        self.symbol = "p6"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p6")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone7(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 6
        self.position_y = 0
        self.symbol = "p7"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p7")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class BlackPone8(ChessBoard):

    def __init__(self):
        ChessBoard.__init__(self)
        self.position_x = 7
        self.position_y = 0
        self.symbol = "p8"

    def move(self):
        while True:
            try:
                print("give a x and y coordinate for p8")
                destination_x = int(input())
                destination_y = int(input())
                if self.board[destination_x][destination_y] == ".":
                    if destination_x == self.position_x and destination_y-self.position_y == 1:
                        self.board[self.position_x][self.position_y] = "."
                        self.position_x = destination_x
                        self.position_y = destination_y
                        self.board[self.position_x][self.position_y] = self.symbol
                        return self.board
                        break
                    else:
                        print("your move is invalid, please choose coordinates again")
                        continue
            except:
                pass

class Engine(ChessBoard):

    def __init__(self):
        WhiteKing.__init__(self)
        WhiteQueen.__init__(self)
        WhiteRook1.__init__(self)
        WhiteRook2.__init__(self)
        WhiteBishop1.__init__(self)
        WhiteBishop2.__init__(self)
        WhiteKnight1.__init__(self)
        WhiteKnight2.__init__(self)
        WhitePone1.__init__(self)
        WhitePone2.__init__(self)
        WhitePone3.__init__(self)
        WhitePone4.__init__(self)
        WhitePone5.__init__(self)
        WhitePone6.__init__(self)
        WhitePone7.__init__(self)
        WhitePone8.__init__(self)
        BlackKing.__init__(self)
        BlackQueen.__init__(self)
        BlackRook1.__init__(self)
        BlackRook2.__init__(self)
        BlackBishop1.__init__(self)
        BlackBishop2.__init__(self)
        BlackKnight1.__init__(self)
        BlackKnight2.__init__(self)
        BlackPone1.__init__(self)
        BlackPone2.__init__(self)
        BlackPone3.__init__(self)
        BlackPone4.__init__(self)
        BlackPone5.__init__(self)
        BlackPone6.__init__(self)
        BlackPone7.__init__(self)
        BlackPone8.__init__(self)

    
    def play(self):
        print("Please write what figure you choose to move: King, Queen, Bishop, Bishop', Knight, Knight', Pone, or Pone'")
        while True:
            choise = str(input())
            if choise == "WK":
                WhiteKing.move(self)
                break
            elif choise == "WQ":
                WhiteQueen.move(self)
                break
            elif choise == "R1":
                WhiteRook1.move(self)
                break
            elif choise == "R2":
                WhiteRook2.move(self)
                break
            elif choise == "B1":
                WhiteBishop1.move(self)
                break
            elif choise == "B2":
                WhiteBishop2.move(self)
                break
            elif choise == "N1":
                WhiteKnight1.move(self)
                break
            elif choise == "N2":
                WhiteKnight2.move(self)
                break
            elif choise == "P1":
                WhitePone1.move(self)
                break
            elif choise == "P2":
                WhitePone2.move(self)
                break
            elif choise == "P2":
                WhitePone2.move(self)
                break
            elif choise == "P3":
                WhitePone3.move(self)
                break
            elif choise == "P4":
                WhitePone4.move(self)
                break
            elif choise == "P5":
                WhitePone5.move(self)
                break
            elif choise == "P6":
                WhitePone6.move(self)
                break
            elif choise == "P7":
                WhitePone7.move(self)
                break
            elif choise == "P8":
                WhitePone8.move(self)
                break
            else:
                print("please choose again")

    def display(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

if __name__ == ('__main__'):
    c_engine = Engine()
    c_engine.display()
    c_engine.play()
    c_engine.display()
            

