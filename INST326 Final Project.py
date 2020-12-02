#INST326 Final Project
from argparse import ArgumentParser
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class NBA:
    '''
    Creates a class that takes in data from a xlsx file.
    methods:
        predict_game_winner(self, team1, team2)
        predict_champion(self)
        predict_mvp(self)
    Attributes:
        players (dict): A dict whose key is player's name, value is his statistics
        teams (dict): Team name as key and players list as value
    '''
    def __init__(self, filename):
        '''Using pandas to read excel to dataframe
        Construct two attributes of NBA instance, they are players dict and teams dict'''
        self.players = dict()
        self.teams = dict()

        df = pd.read_excel(filename)
        for _, row in df.iterrows():
            player = row['FULL NAME']
            self.players[player] = {
                'ppg': row['Points per game'],
                'shoot_perc': row['True Shooting Percentage'],
                'rpg': row['Rebounds per game'],
                'apg': row['Assists per game'],
                'spg': row['Steals per game'],
                'bpg': row['Blocks per game'],
                'tpg': row['Turnovers per game'],
            }
            team = row['TEAM']
            if team in self.teams:
                self.teams[team]['players'].append(player)
            else:
                self.teams[team] = {
                    'players': [player]
                }

    def predict_game_winner(self, team1, team2):
        '''Params:
            team1 (str): team name, e.g., Hou
            team2 (str): another team name, e.g., Lal
        Return:
            team (str): the team name that get more points as the winner'''
        points1 = 0
        points2 = 0
        for player in self.teams[team1]['players']:
            points1 += self.players[player]['ppg']
        for player in self.teams[team2]['players']:
            points2 += self.players[player]['ppg']
        return team1 if points1 > points2 else team2

    def predict_champion(self):
        '''
        Call predict_game_winner method to record each team's winning times, at worst 0 win all lose, at best all win 0 lose.
        Based on every team's winning times, to draw a pie chart showing each team's probability to be the champion.
        Returns: 
            None (but drawing a pie chart, using matplotlib)
        '''
        #labels = self.teams.keys()
        team_wins = []
        for team in self.teams:
            win_times = 0
            for other_team in self.teams:
                if other_team != team: # cannot compete with itself
                    win_times += 1 if self.predict_game_winner(team, other_team) == team else 0 # win_times add 1 if it wins
            self.teams[team]['win_times'] = win_times
            team_wins.append(win_times) # record each team's winning times
        #plt.pie()# draw a pie chart based on predicted winning times（idk how to write it)
        plt.show() # show the plot

    def predict_mvp(self):
        '''
        Parameters: 
            None (only self)
        Using the formula: MVP score = Points * True Shooting% + 1.5(Assists) + 1.2(Rebounds) + 3(Blocks) + 3(Steals) - Turnovers
        to select the player that has the highest score. He is most likely to be the mvp of this season.
        Returns:
            mvp (str): The MVP player's name
        '''
        highest_score = 0
        mvp = ''
        for p in self.players:
            stats = self.players[p]
            # calculate player's score by defined formula
            score = stats['ppg']*stats['shoot_perc'] + 1.5*stats['apg'] + 1.2*stats['rpg'] + 3*stats['bpg'] + 3*stats['spg'] - stats['tpg']
            if score > highest_score: # update the mvp player
                highest_score = score
                mvp = p
        return mvp


def main(filename):
    
    # test predict_game_winner method
    team1 = 'Hou'
    team2 = 'Lal'
    winner = nba.predict_game_winner(team1, team2)
    print(team1, 'vs.', team2+',', 'the predicted winner team is:', winner)

    # test predict_mvp method
    mvp = nba.predict_mvp()
    print('The predicted MVP player of this year is:', mvp)

    # test predict_champion method
    champion = nba.predict_champion()
    print('The prediced champion of this year is:', champion)


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument('filename', help = 'name of xlsx file')
    return parser.parse_args(arglist)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.filename) 