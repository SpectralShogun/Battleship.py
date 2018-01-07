import random
from time import sleep
board = []

for x in range(-1,5):
    board.append([" +"] * 7)

def print_board(board):
    for row in range(0, len(board)):
        print("        ", end="", flush=True)
        for column in range(0, len(board[row])):
            sleep(.1)
            print(board[row][column], end="", flush=True)
        print()
                

s = "Displaying NOAA data on screen"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    

s = "[All data from NOAA system displayed]"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=False)
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)    
    
    sleep(.5)
    
s = "Setting grid formation"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)

s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
    
    

s = "[Grid formation set]"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=False)
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
    
    sleep(.5)
    

s = "[Comemncing art of war!]"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=False)
    
    
s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)

s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
    s = "\n"
for x in range(0,len(s)):
    sleep(.1)
    print(s[x], end="", flush=True)
    
    
    
b = input("{Press *Enter* to command your Fleet}")
if (b == ""):

    s = "\n"
    for x in range(0,len(s)):
        sleep(.1)
        print(s[x], end="", flush=True)
    s = "\n"
    for x in range(0,len(s)):
        sleep(.1)
        print(s[x], end="", flush=True)
    
    s = " --Displaying Grid Formation--"
    for x in range(0,len(s)):
        sleep(.1)
        print(s[x], end="", flush=False)
        

        
        
    s = "\n"
    for x in range(0,len(s)):
        sleep(.1)
        print(s[x], end="", flush=True)
    
    
    print_board(board)
    
    def random_row(board):
        return random.randint(0,len(board)-1)
    
    def random_col(board):
        return random.randint(0,len(board[0])-1)
    
    ship_row = random_row(board)
    ship_col = random_col(board)
    print (ship_row)
    print (ship_col)
    
    for turn in range(4):
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        
        if guess_row == ship_row and guess_col == ship_col:
            s = "Congratulations! You sunk my battleship!"
            for x in range(0,len(s)):
                sleep(.1)
        print(s[x], end="", flush=True)
        break
    else:
            if turn == 3:
                board[guess_row][guess_col] = "X"
                print_board(board)
                s = "Game Over"
                for x in range(0,len(s)):
                    sleep(.1)
                    print(s[x], end="", flush=True)
                print ("My ship was here: [") + str(ship_row) + "][" + str(ship_col) + "]"
            else:            
                if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print ("Oops, that's not even in the ocean.")
                elif(board[guess_row][guess_col] == "X"):
                    print ("You guessed that one already.")
                else:
                    print ("You missed my battleship!")
                    board[guess_row][guess_col] = "X"
                print (turn + 1)
                print_board(board)