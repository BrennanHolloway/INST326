from final_inst import NBA, main
import pytest


class ParameterError(Exception):
    pass

def test_game_winner(tmp_path):
    """ Test winner """
    team1 = 'Hou'
    team2 = 'Lal'
    assert predict_game_winner(team1,team2)== "Lal"
     
def test_champion():
    """ Test champion """
    
    team1 = 'Hou'
    team2 = 'Lal'
    assert predict_champion(team1,team2)== "Lal"
    
def test_mvp():
    """ Test mvp """
    team1 = 'Hou'
    team2 = 'Lal'
    assert predict_mvp(team1,team2)== "DeMarre Carroll"
    
def test_best_shooter():
    team1 = 'Hou'
    team2 = 'Lal'
    assert best_rebounder(team1,team2)== "Quin Cook"


def test_best_rebounder():
    
    team1 = 'Hou'
    team2 = 'Lal'
    assert best_rebounder(team1,team2)== "DeMarre Carroll"