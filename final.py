#INST326 Final Project

from argparse import ArgumentParser
import sys

class GetData:
    '''
    Creates a class that takes in data from a CSV file and returns 
    a list of all players, a teams dictionary and a dictionary of NBA record holders
    
    Attributes:
        players_list (list of tuples): A list with each player and their stats being a tuple
        team_dict (dict): Teams as keys and their players as values
        records_dict (dict): Records as keys and players as values
    '''
    def __init__(self,filename):
        '''
        
        '''
        self.players_list = []
        self.teams_dict = {}
        self.records = {}
        
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                content = line.strip().split(',')
                #Name,Team,FG%,3PT%,PPG,RPG,APG
                self.players_list.append([content[0], content[1], content[12],content[14], content[17], content[18], content[20]]) 
        
        for x in self.players_list:
            if x[1] not in self.teams_dict:
                self.teams_dict[x[1]] = x[0]
            else:
                if not isinstance(self.teams_dict[x[1]], list):
                    self.teams_dict[x[1]] = [self.teams_dict[x[1]]]
                self.teams_dict[x[1]].append(x[0])
        
        self.records = {
            '2019-2020' : {'Champion' : 'Lal',
                           'MVP' : 'Giannis Antetokounmpo',
                           'RotY' : 'Ja Morant',
                           'PPG Leader' : 'James Harden',
                           'RPG Leader' : 'Andre Drummond',
                           'APG Leader' : 'LeBron James'
                           }
        }
        
        print(self.players_list)
        
#    def next_winner(team_1, team_2):
#      '''
#      '''
        
         #Call the teams function in the GetData class to get all the teams
         #Pick the two selected teams from the dictionary
         #Compare the players on the teams selected to see who wins
    
#     def next_champion(all_teams):
#         '''
#         Takes in all the team objects and predicts who will be the next NBA champion team
        
#         Returns: 
#             The predicted champion of the season
#         '''
        
#     def next_mvp(all_players):
#         '''
#         Takes in all the player objects and predicts who the MVP of the season will be
        
#         Returns:
#             The predicted MVP of the season
#         ''' 
def main(filename):
    GetData(filename)


def parse_args(arglist):
    '''
    '''
    parser = ArgumentParser()
    parser.add_argument('filename', help = 'name of csv')
    
    
    return parser.parse_args(arglist)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.filename)
    