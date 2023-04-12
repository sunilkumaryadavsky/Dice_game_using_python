import random
player1 = 0
player2 = 0
dice_list = [1,2,3,4,5,6]
while True:

        
    def dice_game():
        x = input('Player1 press "Enter" to roll the dice')
        r=random.choice(dice_list)
        global player1 
        player1 = player1 +r
        print('Point for player1 :', player1, "Points to win ------->" ,50-player1  )    
        y = input('Player2 press "Enter" to roll the dice')
        s=random.choice(dice_list)
        global player2
        player2 = player2 + s

        print('Point for player2 : ', player2, "Points to win ------->" ,50-player2)               
        if player1 >=50:
            print('Congrats Player1 win the game')
            exit()
        elif player2 >=50:
            print('Congrats Player2 win the game')
            exit()

    dice_game()

