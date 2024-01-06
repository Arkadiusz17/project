print ("This is a rock paper scissors game. Your options are: rock, paper , scissors")
player1_result = 0
player2_result = 0


while player1_result != 3 and player2_result != 3:
    Choice_options_player = True
    player1 = input("player 1 state your choice: ")
    player2 = input("player 2 state your choice: ")

    if player1 == 'paper' and player2 == 'rock'\
    or player1 == 'rock' and player2 == 'scissors' \
    or player1 == 'scissors' and player2 == 'paper' :
        print("Player 1 Win !")
        player1_result +=1
    elif player1 == player2:
        print("Draw !")
    else:
        print("Player 2 Win !")
        player2_result += 1
    
if player1_result > player2_result:
    print("player 1 won the entire game")
else:
    print("player 2 won the entire game")