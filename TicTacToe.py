#Global variables
board=["-","-","-"
      ,"-","-","-"
      ,"-","-","-"]

game_still_going_on=True
current_player="X"
winner=None
#displaying board
def display_board():
  print(board[0]+"|"+board[1]+"|"+board[2])
  print(board[3]+"|"+board[4]+"|"+board[5])
  print(board[6]+"|"+board[7]+"|"+board[8]) 


def playGame():
  display_board()
  
  #While game is still being played
  while game_still_going_on:
    #handle single turn of an arbitary player
    handle_turn(current_player)
    check_if_game_over()
    flip_player()  
  if winner=="X" or winner=="0":
    print (winner+" won.")
  elif(winner==None):
    print("Tie")    
#handle single turn of an arbitary player
def handle_turn(player):
   global current_player
   print(player+"'s turn")
   position=input("Choose a position between from 1-9:")
   while position not in ["1","2","3","4","5","6","7","8","9"]:
     position=input("Invalid Input!!Choose a position between from 1-9:")
   position=int(position)-1
   if board[position]=="-":
    board[position]=player
    display_board()
   else:
     print("This position is already occupied.cant Overwrite!")
     handle_turn(current_player)

     
   
def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
   #to make winner treated as a global variable
   global winner
   rows_winner=check_rows()
   column_winner=check_columns()
   diagonals_winner=check_diagonals()
   if(rows_winner):
     winner=rows_winner
   elif(column_winner):
     winner=column_winner
   elif(diagonals_winner):
     winner=diagonals_winner
   else:
     winner=None    
     return


def check_if_tie():
  global game_still_going_on
  if "-" not in board:
    game_still_going_on=False
  return 


def flip_player():
  global current_player
  if current_player=="X":
      current_player="0"
  elif current_player=="0":
      current_player="X"    
  return


def check_rows():
  global game_still_going_on
  row1=board[0]==board[1]==board[2]!="-"
  row2=board[3]==board[4]==board[5]!="-"
  row3=board[6]==board[7]==board[8]!="-"
  if row1 or row2 or row3:
    game_still_going_on=False
  if row1: 
    return board[0]
  elif row2: 
    return board[3]
  elif row3: 
    return board[6]
  return 


def check_columns():
  global game_still_going_on
  col1=board[0]==board[3]==board[6]!="-"
  col2=board[1]==board[4]==board[7]!="-"
  col3=board[2]==board[5]==board[8]!="-"
  if col1 or col2 or col3:
    game_still_going_on=False
  elif col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]
  return

def check_diagonals():
  global game_still_going_on
  dia1=board[0]==board[4]==board[8]!="-"
  dia2=board[2]==board[4]==board[6]!="-"
  if dia1 or dia2:
    game_still_going_on=False
  if dia1:
    return board[0]
  elif dia2:
    return board[2] 
  else:
    return


playGame()