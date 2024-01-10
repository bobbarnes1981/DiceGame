import logging
import random

MAX_CHIPS = 24
NUM_PLAYERS = 3
MIN_CHIPS = 3
MAX_DICE = 3

NUM_GAMES = 10000

player_wins = []
for i in range(NUM_PLAYERS):
    player_wins.append(0)
total_rounds = 0

class Game():
    DICE_OPTIONS = ['*', '*', '*', 'L', 'C', 'R']
    def __init__(self, max_chips, num_players, min_chips, max_dice):
        self.max_chips = max_chips
        self.num_players = num_players
        self.min_chips = min_chips
        self.max_dice = max_dice
        self.starting_chips = self.max_chips // self.num_players
        if self.starting_chips < self.min_chips:
            raise Exception("Not enough chips")
        self.reset()
    def reset(self):
        self.round = 0
        self.centre = 0
        self.has_winner = False
        self.players = []
        for i in range(self.num_players):
            self.players.append(self.starting_chips)
    def __show_state(self):
        logging.info("Centre chips: {0}".format(self.centre))
        players_with_chips = []
        for i in range(len(self.players)):
            if self.players[i] > 0:
                players_with_chips.append(i)
            logging.info("player {0}: chips: {1}".format(i, self.players[i]))
        return players_with_chips
    def __roll_dice(self, num_dice):
        results = []
        for i in range(num_dice):
            results.append(random.choice(self.DICE_OPTIONS))
        return results
    def play(self):
        logging.info("Players: {0}".format(self.num_players))
        logging.info("Chips per player: {0}".format(self.starting_chips))
        self.__show_state()
        while self.has_winner == False:
            self.round+=1
            logging.info("Round: {0}".format(self.round))
            for i in range(len(self.players)):
                logging.info("Player: {0}".format(i))
                chips = self.players[i]
                logging.info("Chips: {0}".format(chips))
                if chips > 0:
                    num_dice = min(chips, self.max_dice)
                    logging.info("Dice: {0}".format(num_dice))
                    results = self.__roll_dice(num_dice)
                    logging.info("Results: {0}".format(results))
                    for result in results:
                        if result == 'L':
                            target = i-1
                            if target < 0:
                                target += self.num_players
                            self.players[i]-=1
                            self.players[target]+=1
                        if result == 'C':
                            self.players[i]-=1
                            self.centre+=1
                        if result == 'R':
                            target = i+1
                            if target > NUM_PLAYERS-1:
                                target -= NUM_PLAYERS
                            self.players[i]-=1
                            self.players[target]+=1
                players_with_chips = self.__show_state()
                if len(players_with_chips) == 1:
                    self.has_winner = True
                    break
        self.winner = players_with_chips[0]

g = Game(MAX_CHIPS, NUM_PLAYERS, MIN_CHIPS, MAX_DICE)
for i in range(NUM_GAMES):
    print("Game: {0}".format(i+1))
    g.play()
    print("Winner: {0} Rounds: {1} Chips: {2}".format(g.winner, g.round, g.players[g.winner]))
    player_wins[g.winner]+=1
    total_rounds += g.round
    print("Wins: {0}".format(player_wins))
    print("Average rounds: {0}".format(total_rounds / (i+1)))
    g.reset()