#INST326 Final Project

from argparse import ArgumentParser
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class NBA:
    '''
    Creates a class that takes in data from a CSV file and returns 
    a list of all players, a teams dictionary, and a dataframe of all information
    
    Methods:
        predict_game_winner(self, team1, team2)
        predict_champion(self)
        predict_mvp(self)
        
    Attributes:
        players_list (list of tuples): A list with each player and their stats being a tuple
        team_dict (dict): Teams as keys and their players as values
        
    '''
    
    def __init__(self,filename):
        '''
        Reads in a CSV file 
        Constructs three attributes of NBA instance that are a players_dict, a teams_dict and a dataframe
        '''
        self.players_dict = {}
        self.teams_dict = {} 
        
        columns = ["Name","Team","Position","Age","GP","MPG",
                   "MIN%","USG%","TO%","FTA","FT%","2PA","2P%","3PA"
                   ,"3P%","eFG%","TS%","PPG","RPG","TRB%","APG","AST%",
                   "SPG","BPG","TOPG","VIV","ORTG","DRTG"]
        self.df = pd.read_csv(filename, sep = ',', names=columns)
        print(self.df.head())
        
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                content = line.strip().split(',')
                name = content[0]
                team = content[1]
                #Name,Team,FG%,3PT%,PPG,RPG,APG,Steals,Blocks,Turnovers
                self.players_dict.update( {name : {'Team' : content[1], 'FG%' : content[12],'3PT%' : content[14], 
                                                   'PPG' : content[17], 'RPG' : content[18], 'APG' : content[20], 
                                                   'Steals' : content[22], 'Blocks' : content[23], 'Turnovers' : content[24]}} ) 
                if team in self.teams_dict:
                    self.teams_dict[team].append(name)
                else:
                    self.teams_dict[team] = [name] 
        
    def predict_game_winner(self, team1, team2):
        '''
        Params:
            team1 (str): team name, e.g., Hou
            team2 (str): another team name, e.g., Lal
        Return:
            team (str): the team name that get more points as the winner
        '''
        points1 = 0
        points2 = 0
        for player in self.teams_dict[team1]:
            points1 += float(self.players_dict[player]['PPG'])
        for player in self.teams_dict[team2]:
            points2 += float(self.players_dict[player]['PPG'])
        
        return team1 if points1 > points2 else team2
     
    def predict_champion(self):
        '''
        Call predict_game_winner method to record each team's winning times, at worst 0 win all lose, at best all win 0 lose.
        Based on every team's winning times, to draw a pie chart showing each team's probability to be the champion.
        Returns: 
            best_team (str): the name of the team we predict to be the best
            counter (int): the number of wins they have
            (Also a PIE chart of each teams wins to go with our prediction)
        '''
        team_wins = []
        labels = []
        wins = []
        win_times = 0
        for team in self.teams_dict:
            labels.append(team)
            team_wins.append( {team : win_times} )
            win_times = 0
            for other_team in self.teams_dict:
                if other_team != team: # cannot compete with itself
                    win_times += 1 if self.predict_game_winner(team, other_team) == team else 0 # win_times add 1 if it wins

        best_team = ''
        counter = 0 
        for x in team_wins:
            for y in x:
                wins.append(x[y])
                if x[y] > counter:
                    best_team = y
                    counter = x[y]           

        plt.pie( wins, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140) # draw a pie chart based on predicted winning teams
        plt.axis('equal')
        plt.show() # show the plot
        
        return(best_team, counter)
        
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
        for p in self.players_dict:
            stats = self.players_dict[p]
            # calculate player's score by defined formula
            score = float(stats['PPG']) * float(stats['FG%'])
            + (1.5*float(stats['APG'])) + (1.2*float(stats['RPG']))
            + (3*float(stats['Blocks'])) + (3*float(stats['Steals']))
            - float(stats['Turnovers'])
            if score > highest_score: # update the mvp player
                highest_score = score
                mvp = p
        return mvp
    
    def best_shooter(self, team3, team4):
        '''
        Parameters:
            team3: A choosen NBA team
            team4: A choosen NBA team
        Takes in two NBA team and calls our predict_game_winner function to determine who would win the game,
        then finds who was the best shooter on that team
        Returns:
            shooter (str): The name of the player who was the best shooter
        '''
        counter = 0
        best_shooter = 0
        shooter = ''
        winner = self.predict_game_winner(team3,team4)
        
        for player in self.teams_dict[winner]:
            counter = (self.players_dict[player]["3PT%"])
            if float(counter) > float(best_shooter):
                best_shooter = counter
                shooter = player
                
        return shooter
        
    def best_rebounder(self, team3, team4):
        '''
        Parameters:
            team3: A choosen NBA team
            team4: A choosen NBA team
        Takes in two NBA team and calls our predict_game_winner function to determine who would win the game,
        then finds who was the best rebounder on that team
        Returns:
            rebounder (str): The name of the player who was the best rebounder
        '''
        counter = 0
        best_rebounder = 0
        rebounder = ''
        winner = self.predict_game_winner(team3,team4)
        
        for player in self.teams_dict[winner]:
            counter = (self.players_dict[player]["RPG"])
            if float(counter) > float(best_rebounder):
                best_rebounder = counter
                rebounder = player
                
        return rebounder
        
def main(filename):
    """
    Parameters:
        filename 
    Uses the data from the CSV file to predict the game winner of a game by adding average points per game for the top 5 players in each team.
    MVP will be predicted by calling predict_mvp method up above by using the formula used.
    The champion of the season will be predicted by analyzing the stats of the players on each team predicting the highest probable champion.
    Prints:
        Predicted winner, MVP, and Champion
    """
    nba = NBA(filename)
    
    #Test predict_game_winner method
    team1 = 'Den'
    team2 = 'Okc'
    winner = nba.predict_game_winner(team1, team2)
    print(team1, 'vs.', team2, ', the predicted winning team is:', winner)
    
    #Test predict_champion method
    best = nba.predict_champion()
    print(best[0], 'is the next predicted champion of the NBA with a total wins of', best[1])
    
    #Test predict_mvp method
    mvp_2 = nba.predict_mvp()
    print('The predicted MVP player of the year is:', mvp_2)
    
    #Test best_shooter method
    team3 = 'Lal'
    team4 = 'Hou'
    shooter = nba.best_shooter(team3, team4)
    print('The best shooter on the winning team between the matchup of', team3, 'and', team4, 'was', shooter)
    
    #Test the rebounder method
    rebounder = nba.best_rebounder(team3, team4)
    print('The best rebounder on the winning team between the matchup of', team3, 'and', team4, 'was', rebounder)
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument('filename', help = 'name of csv')
    return parser.parse_args(arglist)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.filename)
    