#INST326 Final Project

class player(player_name, list_of_player_stats):
    '''
    Creates a player object which will contain their stats for the season 
    ARGS:
        player_name (str): name of the player
        list_of_player_stats (list): list of that players stats for the season
    '''
    def __init__(self):
        '''
        Initalizes the players 
        '''
    
    def create_player(player_name):
        '''
        Creates a player object
    
        Returns:
            the string of the player name    
        '''
        
    def player_stats(list_of_player_stats):
        '''
        Populates the player object with our chosen stats
        
        Returns:
            the list of the player stats
        '''
        
class team(players, list_of_team_stats):
    '''
    Creates team objects which include the names of five players and one coach 
    ARGS:
        players (list): list of players on each team
        list_of_team_stats (list): list of team stats
    '''
    def __init__(self):
        '''
        Initalizes the teams
        '''
        
    def create_team(players):
        '''
        LIST: An object made up of player objects
        
        Returns:
            List of players on the team
        '''
    
    def team_stats(list_of_team_stats):
        '''
        Gives the team stats (Tuple)
        
        Returns:
            List of team stats
        '''
    
    def coach(name):
        '''
        Adds the name of the coach to the team list in the first position 
        '''
        
class predictions():
    '''
    Uses the team and player objects to compare and make predictions about future winners
    '''
    def next_winner(team_1, team_2):
        '''
        Takes in two team objects and predicts the winner of the matchup
        
        Returns:
            The predicted winner of the game
        '''
    
    def next_champion(all_teams):
        '''
        Takes in all the team objects and predicts who will be the next NBA champion team
        
        Returns: 
            The predicted champion of the season
        '''
        
    def next_mvp(all_players):
        '''
        Takes in all the player objects and predicts who the MVP of the season will be
        
        Returns:
            The predicted MVP of the season
        ''' 
        
class records():
    '''
    Records all the major achievements for each season and stores it as a list of dictionaries
    i.e. MVP, DMVP, Champion, Finals MVP etc..
    '''
    
    def __init__(self):
        '''
        initalizes the list to keep track of players
        '''
    
    def record(list_of_accolades):
        '''
        takes in a list of accolades and adds it to a running list of all-time NBA players
        
        Returns:
            An updated list with the new best players from the current season
        '''