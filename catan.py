# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# sns.set_style("ticks")
# 
# dist = np.zeros(11)
# 
# def roll_input():
#     x = input("Roll: ")
#     plt.close()
#     dist[int(x) - 2] += 1
# 
#     mean = 0
#     for i in range(2, 13):
#         mean += i * dist[i - 2]
#     mean /= np.sum(dist)
#     print(mean)
#     np.var
#     [j for j in dist[i] for i in range(12)]
#     variance = np.var([j for j in dist[i-2] for i in range(2,13)])
#     print(dist)
# 
#     plt.bar(np.arange(2, 13), dist)
#     plt.xlim(2, 13)
#     plt.show(block=False)
# roll_input()
# dist
# 
# rolls = []
# for dice_value, dice_count in enumerate(dist):
#     for j in range(int(dice_count)):
#         rolls.append(dice_value + 2)
# np.sqrt(np.var(rolls))
# 
# plt.bar(np.arange(2, 13), dist)
# plt.xlim(2, 13)
# plt.show(block=False)
# 
# rolls
# print(dist)
# 
# f(x) = x
# # mine = [5,8,10,3,10,11,4,5,11]
# 
# 
# games = np.array([[0.,   3.,   3.,   3.,   5.,   7.,  12.,   9.,   4.,   3.,   0.],
#                   [0.,  1.,  5.,  1.,  6., 6.,  6.,  5.,  2.,  3.,  0.],
#                   [1.,   2.,   0.,   6.,  10.,   9.,   7.,   5.,   2.,   7.,   3.],
#                   [0.,   3.,   1.,   3.,   4.,   5.,   3.,  10.,   5.,   5.,   0.],
#                   [1.,  5.,  2.,  6.,  4.,  6.,  4.,  3.,  8.,  2.,  0.]])
# combined = 0
# for game in games:
#     combined += game
# print(combined)
# 
# mean = 0
# for i in range(2, 13):
#     mean += i * combined[i - 2]
# mean /= np.sum(combined)
# print(mean)
# 
# plt.bar(np.arange(2, 13), combined)
# plt.xlim(2, 13)
# plt.show(block=False)

chits = {5: ['A', 'O'],
         2: ['B'],
         6: ['C', 'P'],
         3: ['D', 'Q'],
         8: ['E', 'K'],
         10: ['F', 'L'],
         9: ['G', 'M'],
         12: ['H'],
         11: ['I', 'R'],
         4: ['J', 'N']}

import pandas as pd
class Player:
    def __init__(self, name):
        self.name = name
        self.placements = []
        self.harvests = []
        
    def place(self, letters):
        self.placements.append(letters)

class CatanGame:
    def __init__(self, players, resource_dict):
        self.chits = chits
        self.players = players
        self.resource_dict = resource_dict
        self.rolls = []

    def print_results(self):
        mean = np.mean(self.rolls)
        median = np.median(self.rolls)
        std = np.std(self.rolls)
        
        print('Mean: %.2f' %mean)
        print('Median: %.2f' %median)
        print('Std Dev: %.2f' %std)
        
        n, bins, x = plt.hist(self.rolls, bins = np.array(range(2,14)))
        plt.xticks(np.arange(min(bins)+1/2, max(bins), 1), bins)
        plt.show()
        
        player_names = [player.name for player in self.players]
        try:
            df = pd.DataFrame(
                [pd.DataFrame(player.harvests).sum() for player in self.players], 
                index=player_names)
            df.T.plot.bar()
            plt.show()
        except: 
            pass
        
    def roll(self, number):
        self.rolls.append(number)
        self.print_results()
        
        if number == 7:
            return
            
        for player in self.players:
            earned_resources = {'w' : 0, 'wh' : 0, 's' : 0, 'r' : 0, 'b' : 0}
            for placement in player.placements:
                for letter in placement:
                    if letter in chits[number]:
                        earned_resources[resource_dict[letter]] += 1
            player.harvests.append(earned_resources)
            
    
resource_dict = {# wheat : wh, wood : w, sheep : s, rock : r, brick : b
    'A' : 'r', 
    'B' : 'w', 
    'C' : 's', 
    'D' : 'w', 
    'E' : 'w', 
    'F' : 'wh', 
    'G' : 'r', 
    'H' : 's', 
    'I' : 'b', 
    'J' : 'b', 
    'K' : 's', 
    'L' : 'wh', 
    'M' : 'wh', 
    'N' : 'r', 
    'O' : 'w', 
    'P' : 'b', 
    'Q' : 's', 
    'R' : 'wh'}

patrick = Player('Patrick')
cail = Player('Cail')
amelia = Player('Amelia')
colin = Player('Colin')
game = CatanGame(
    players = [patrick, cail, colin, amelia], 
    resource_dict=resource_dict)

amelia.place(['G', 'F', 'I'])
cail.place(['B', 'N', None])
patrick.place(['L', 'E', 'K'])
colin.place(['A', 'R', 'E'])
patrick.place(['P', 'M', 'O'])
colin.place(['P', 'N', 'I'])
amelia.place(['B', 'D', 'Q'])
cail.place(['J', 'K', None])

game.roll(5)
game.roll(9)
game.roll(6)
game.roll(8)
game.roll(10)
game.roll(6)
game.roll(6)
game.roll(4)
game.roll(5)
game.roll(7)
game.roll(4)
game.roll(6)
game.roll(7)
game.roll(9)
game.roll(7)
game.roll(5)
game.roll(9)
game.roll(6)
game.roll(7)
game.roll(7)
game.roll(4)
game.roll(7)
game.roll(8)
game.roll(3)
game.roll(9)
game.roll(11)
game.roll(9)
game.roll(4)
game.roll(12)
game.roll(7)
game.roll(8)
game.roll(9)
game.roll(7)
game.roll(7)
game.roll(6)
game.roll(10)
game.roll(10)
game.roll(6)
game.roll(9)
game.roll(7)
game.roll(2)
game.roll(8)
game.roll(4)
game.roll(9)
game.roll(6)
game.roll(6)
