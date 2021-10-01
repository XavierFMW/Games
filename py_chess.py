from colorama import Fore
import sys


class piece:

    def __init__(self, white, row, column):

        self.white = white

        self.row = row
        self.col = column

        self.moves = [(row, column), ]
        
        str = type(self).__name__[0]

        if white:
            self.letter = Fore.RED + str.upper()

        else:
            self.letter = Fore.BLUE + str


    def straight(self, board):

        move_set = []

        for x in [1, - 1]:

            n = x
            m = x

            while True:

                try:
                    space = board[self.row][self.col + n]

                    if isinstance(space, str):
                        move_set.append((self.row, self.col + n))

                        if n > 0:
                            n += 1
                        else:
                            n -= 1

                    elif space.white != self.white:

                        move_set.append((self.row, self.col + n))
                        break

                    else:
                        break

                except IndexError:
                    break


            while True:

                try:
                    space = board[self.row + m][self.col]

                    if isinstance(space, str):
                        move_set.append((self.row + m, self.col))

                        if m > 0:
                            m += 1
                        else:
                            m -= 1

                    elif space.white != self.white:

                        move_set.append((self.row + m, self.col))
                        break

                    else:
                        break

                except IndexError:
                    break

        return move_set


    def diagonal(self, board):
        
        move_set = []

        for x in [1, - 1]:

            n = x
            m = x

            while True:

                try:
                    space = board[self.row + n][self.col + n]

                    if isinstance(space, str):
                        move_set.append((self.row + n, self.col + n))

                        if n > 0:
                            n += 1
                        else:
                            n -= 1

                    elif space.white != self.white:

                        move_set.append((self.row + n, self.col + n))
                        break

                    else:
                        break

                except IndexError:
                    break


            while True:

                try:
                    space = board[self.row + m][self.col - m]

                    if isinstance(space, str):
                        move_set.append((self.row + m, self.col - m))

                        if m > 0:
                            m += 1
                        else:
                            m -= 1

                    elif space.white != self.white:

                        move_set.append((self.row + m, self.col - m))
                        break

                    else:
                        break

                except IndexError:
                    break
        
        return move_set

    
    def move(self, board, coords):
        
        move_set = self.genMoveSet(board)

        if coords in move_set:

            if type(board[coords[0]][coords[1]]).__name__ == "king":

                white = not board[coords[0]][coords[1]].white

                if white:
                    sys.exit(Fore.RED + "\n\nWHITE WINS!")
                else:
                    sys.exit(Fore.BLUE + "\n\nBLACK WINS!")

            else:

                board[coords[0]][coords[1]] = self
                board[self.row][self.col] = Fore.WHITE + "x"

                self.moves.append(coords)

                self.row = coords[0]
                self.col = coords[1]

                return True

        else:
            return False



class pawn(piece):

    def genMoveSet(self, board):
        
        move_set = []

        try:

            if self.white:

                space = board[self.row - 1][self.col]

                if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                    move_set.append((self.row - 1, self.col))

            else:

                space = board[self.row + 1][self.col]

                if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                    move_set.append((self.row + 1, self.col))

        except IndexError:
            pass


        if len(self.moves) == 1:

            try:

                if self.white:

                    space = board[self.row - 2][self.col]

                    if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                        move_set.append((self.row - 2, self.col))

                else:

                    space = board[self.row + 2][self.col]

                    if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                        move_set.append((self.row + 2, self.col))

            except IndexError:
                pass
        

        if self.white:
            coords_set = [(-1, -1), (-1, 1)]
        else:
            coords_set = [(1, -1), (1, 1)]

        for coords in coords_set:

            try:
                space = board[self.row + coords[0]][self.col + coords[1]]

                if not isinstance(space, str) and space.white != self.white:
                    move_set.append((self.row + coords[0], self.col + coords[1]))

            except IndexError:
                pass


        return move_set




class rook(piece):

    def genMoveSet(self, board):
        return self.straight(board)



class bishop(piece):

    def genMoveSet(self, board):
        return self.diagonal(board)



class horse(piece):

    def genMoveSet(self, board):

        move_set = []
        
        for coords in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:

            try:
                space = board[self.row + coords[0]][self.col + coords[1]]

                if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                    move_set.append((self.row + coords[0], self.col + coords[1]))

            except IndexError:
                pass

        return move_set



class king(piece):

    def genMoveSet(self, board):

        move_set = []
        
        for coords in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:

            try:
                space = board[self.row + coords[0]][self.col + coords[1]]

                if isinstance(space, str) or not isinstance(space, str) and space.white != self.white:
                    move_set.append((self.row + coords[0], self.col + coords[1]))

            except IndexError:
                pass

        return move_set



class queen(piece):

    def genMoveSet(self, board):
        
        move_set = []

        move_set.extend(self.straight(board))
        move_set.extend(self.diagonal(board))

        return move_set



class system:

    def __init__(self):

        x = Fore.WHITE + "x" 

        self.board = [
        [rook(False, 0, 0), horse(False, 0, 1), bishop(False, 0, 2), queen(False, 0, 3), king(False, 0, 4), bishop(False, 0, 5), horse(False, 0, 6), rook(False, 0, 7)], 
        [pawn(False, 1, 0), pawn(False, 1, 1), pawn(False, 1, 2), pawn(False, 1, 3), pawn(False, 1, 4), pawn(False, 1, 5), pawn(False, 1, 6), pawn(False, 1, 7), ],
        [x, x, x, x, x, x, x, x], 
        [x, x, x, x, x, x, x, x], 
        [x, x, x, x, x, x, x, x], 
        [x, x, x, x, x, x, x, x], 
        [pawn(True, 6, 0), pawn(True, 6, 1), pawn(True, 6, 2), pawn(True, 6, 3), pawn(True, 6, 4), pawn(True, 6, 5), pawn(True, 6, 6), pawn(True, 6, 7), ], 
        [rook(True, 7, 0), horse(True, 7, 1), bishop(True, 7, 2), queen(True, 7, 3), king(True, 7, 4), bishop(True, 7, 5), horse(True, 7, 6), rook(True, 7, 7)],
        ]


    def opposite(self, list):

        reversed = []

        for arr in list[::-1]:
            reversed.append(arr[::-1])

        return reversed

    
    def letter(self, obj):

        if isinstance(obj, str):
            return obj

        else:
            return obj.letter


    def show(self, list, front):

        if not front:
            list = self.opposite(list)

        for arr in list:
            print(f"{self.letter(arr[0])} {self.letter(arr[1])} {self.letter(arr[2])} {self.letter(arr[3])} {self.letter(arr[4])} {self.letter(arr[5])} {self.letter(arr[6])} {self.letter(arr[7])}")


    def decode(self, str):

        num_dict = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

        row = num_dict[str[1]]
        column = int(chr(ord(str[0]) - 49))

        return (row, column)    


    def turn(self, white=True):

        self.show(self.board, white)

        if white:
            print(Fore.RED + "\nWhite's turn.")
        else:
            print(Fore.BLUE + "\nBlack's turn.")

        while True:

            answer = input(Fore.WHITE + "\n\n").split()

            try:
                move_from = self.decode(answer[0])
                move_to = self.decode(answer[1])

                space = self.board[move_from[0]][move_from[1]]

                if isinstance(space, str):
                    print("No piece on that space!")

                elif space.white != white:
                    print("That piece isn't yours!")

                else:

                    if space.move(self.board, move_to):
                        break
                                    
                    else:
                        print(f"Cannot move {type(space).__name__.title()} to {answer[1]}!")

            except KeyError:
                print("Invalid input")

        self.turn(not white)


test = system()
test.turn()
