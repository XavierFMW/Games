 
class Game:
    """
    Contains all the information and programs needed to play a game of TikTakToe.

    Attributes:
        playersDict (dict): A dictionary containing each player's name and icon.

        won (bool): Determines whether or not a round of TikTakToe has been won.

        winner (str): The winning player of a round of TikTakToe.

        guide (str): A guide as to how the game is played. Contains a diagram of how the game's board is numbered.

        keysDict (dict): Matches the number input by the player to the corresponding entry in the 'board' list.

        board (list): Contains each of the separate elements used to form the game's board. Each element is stored as a string, all of which
            are concatenated together to form a single printable result when the 'showBoard()' method is called.

    Methods:
        __init__(self, p1, p2)
        showBoard(self)
        turn(self, player)
        play(self)
    """

    def __init__(self, p1, p2):

        self.playersDict = {f"Player 1 ({p1})": p1, f"Player 2 ({p2})": p2}

        self.won = False
        self.winner = None

        self.guide = """
        -------
        |1|2|3|
        -------
        |4|5|6|
        -------
        |7|8|9|
        -------

        This is how the spaces on the board are numbered. You will be asked for a space to fill each turn.
        """

        self.keysDict = {"1": 2, "2": 4, "3": 6, "4": 10, "5": 12, "6": 14, "7": 18, "8": 20, "9": 22}
        self.board = [
        "------- \n", 
        "|", " ", "|", " ", "|", " ", "| \n", 
        "------- \n", 
        "|", " ", "|", " ", "|", " ", "| \n", 
        "------- \n", 
        "|", " ", "|", " ", "|", " ", "| \n", 
        "-------"
        ]


    def showBoard(self):
        """
        Concatenates all of the entries within the 'board' list into one string, then returns the result.
        """
        output = ""

        for item in self.board:
            output += str(item)

        return output


    def turn(self, player):
        """
        Causes one turn of play within a round of TikTakToe.

        Arguments:
            player (str): The name of the player acting during the turn, a key to the 'playersDict' dictionary.

        Notes:
            During one turn, a player simply chooses a spot and has said spot filled by their given symbol. (Wow, like a round of TikTakToe)
        """

        icon = self.playersDict[player]

        print("\n\n" + self.showBoard())
        print(f"It's {player}'s turn.")

        space = input("Input a space to fill. (1-9): ")
        
        while space not in self.keysDict or self.board[self.keysDict[space]] != " ":
            space = input("Invalid space, enter a new space to fill. (1-9): ")

        self.board[self.keysDict[space]] = icon


    def play(self):
        """
        Causes one round of TikTakToe to be played.

        Notes:
            Multi-line 'if' statements are used to cover each with scenario for a game of TikTakToe. Each possible straight line within a 
                TikTakToe board is individually checked, causing the spaghetti-like nature of this code. This was as efficient as I could make 
                this, massively helped by the fact that conditionals can be chained together (I seriously can't believe that chaining conditionals
                like this works here, it almost feels like cheating.) Apologies to anybody who has to look back at this.
        """

        print(self.guide)

        while self.won == False:

            for player in self.playersDict:
                self.turn(player)

                if (self.board[2] == self.board[4] == self.board[6] != " " or self.board[10] == self.board[12] == self.board[14] != " " or self.board[18] == self.board[20] == self.board[22] != " " or 
                    self.board[2] == self.board[10] == self.board[18] != " " or self.board[4] == self.board[12] == self.board[20] != " " or self.board[6] == self.board[14] == self.board[22] != " " or 
                    self.board[2] == self.board[12] == self.board[22] != " " or self.board[6] == self.board[12] == self.board[18] != " "):

                    self.won = True
                    self.winner = player

                    break

                elif (self.board[2] != " " and self.board[4] != " " and self.board[6] != " " and 
                    self.board[10] != " " and self.board[12] != " " and self.board[14] != " " and
                    self.board[18] != " " and self.board[20] != " " and self.board[22] != " "):

                    self.won = True
                    self.winner = "Draw, board filled."

                    break

        print("\n\n" + self.showBoard())
        print(f"Game over! Winner: {self.winner}")
