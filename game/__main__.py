import random

MAX_CHIPS = 24
NUM_PLAYERS = 3
MIN_CHIPS = 3
MAX_DICE = 3

STARTING_CHIPS = MAX_CHIPS // NUM_PLAYERS

DICE_OPTIONS = ['*', '*', '*', 'L', 'C', 'R']

if STARTING_CHIPS < MIN_CHIPS:
    raise Exception("Not enough chips")

def show_state(centre, players):
    print("Centre chips: {0}".format(centre))
    players_with_chips = []
    for i in range(len(players)):
        if players[i] > 0:
            players_with_chips.append(i)
        print("player {0}: chips: {1}".format(i, players[i]))
    return players_with_chips

def roll_dice(num_dice):
    results = []
    for i in range(num_dice):
        results.append(random.choice(DICE_OPTIONS))
    return results

print("Players: {0}".format(NUM_PLAYERS))
print("Chips per player: {0}".format(STARTING_CHIPS))

round = 0
centre = 0
players = []
for i in range(NUM_PLAYERS):
    players.append(STARTING_CHIPS)
show_state(centre, players)

has_winner = False

while has_winner == False:
    round+=1
    print("Round: {0}".format(round))
    for i in range(len(players)):
        print("Player: {0}".format(i))
        chips = players[i]
        print("Chips: {0}".format(chips))
        if chips > 0:
            num_dice = min(chips, MAX_DICE)
            print("Dice: {0}".format(num_dice))
            results = roll_dice(num_dice)
            print("Results: {0}".format(results))
            for result in results:
                if result == 'L':
                    target = i-1
                    if target < 0:
                        target += NUM_PLAYERS
                    players[i]-=1
                    players[target]+=1
                if result == 'C':
                    players[i]-=1
                    centre+=1
                if result == 'R':
                    target = i+1
                    if target > NUM_PLAYERS-1:
                        target -= NUM_PLAYERS
                    players[i]-=1
                    players[target]+=1
        players_with_chips = show_state(centre, players)
        if len(players_with_chips) == 1:
            has_winner = True
            break

print("Done")

print("Winner: {0} Rounds: {1}".format(players_with_chips[0], round))
