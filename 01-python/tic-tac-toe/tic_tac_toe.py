import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None  

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    WAYS_TO_WIN=((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for way in WAYS_TO_WIN:
      if self.board[way[0]] == self.board[way[1]] == self.board[way[2]] != None:
        if(self.board[way[0]] == _PLAYER_SYMBOL):
          self.winner = _PLAYER
        else:
            self.winner = _MACHINE 
        self.is_game_over = True
        return True
    return self.board.count(None) == 0
    
  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    verificador = True
    while verificador:
      r = random.randrange(9)
      #print(r)
      if self.board[r] is None:
        self.board[r] = _MACHINE_SYMBOL
        verificador = False

  def format_board(self):
    x=1
    for i in self.board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
        char=' '
        if i in (_MACHINE_SYMBOL,_PLAYER_SYMBOL): char=i
        x+=1
        print(char,end=end)

        #vacio = " "
    #print("\n", vacio if self.board[0] is None else self.board[0], "|", vacio if self.board[0] is None else self.board[1], "|", vacio if self.board[0] is None else self.board[2])
    #print(vacio if self.board[0] is None else self.board[3], "|", vacio if self.board[0] is None else self.board[4], "|", vacio if self.board[0] is None else self.board[5])
    #print(vacio if self.board[0] is None else self.board[6], "|", vacio if self.board[0] is None else self.board[7], "|", vacio if self.board[0] is None else self.board[8], "\n")

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if (self.winner is not None):
      print("The winner is: {0}".format(self.winner))
    pass
