import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value) #choose a random number betn max and min value

    return roll

while True:      # pick a vlaid number bet the given number
    players = input("enter the numberb of players(2-4):")
    if players.isdigit():
        players = int (players)
        if 2 <= players <= 4:
            break
        else:
            print("must be betn  2-4 players.")
    else:
        print("Invalid ,try again.")

max_score = 50
player_score = [0 for _ in range(players)] # show the number in 0 array format
while max(player_score) < max_score:
    for player_idx in range(players):
        print("\n player",player_idx +1 ,"trun has just started ")
        print("your tortal score is:",player_score[player_idx] ,"\n")
        current_score = 0
        while True:
            should_roll = input('would you like to roll (y)?')
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("you roll a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score  += value
                print("you rolled a:",value)
            print("your score is :",current_score)

        player_score[player_idx] += current_score
        print("your total score is :",player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("player  number",winning_idx + 1,
      "is the winner with a score of :",max_score)