# Rock, Paper, Scissors

import random

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']
player_score = 0
computer_score = 0

while True:
    player_move = input("Your move: ")
    if player_move == 'q':
        break

    computer_move = random.choice(moves)

    print ("Player: " + player_move)
    print ("Computer: " + computer_move)
    if player_move == computer_move:
        print ("Tie")
    elif player_move + computer_move in player_wins:
        print ("Player wins")
        player_score += 1
    else:
        print("Computer wins")
        computer_score += 1

print ("Final score is Computer: " + str(computer_score) + " Player: " + str(player_score))