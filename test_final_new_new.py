from final_new_new import NBA

def test_predict_game_winner(self):
    """ Test winner """
    nba = NBA()
    assert nba.predict_game_winner('Den','Okc') == "Okc"
        
def test_predict_champion():
    """ Test champion """
    nba = NBA()
    assert nba.predict_champion()== "Den"
        
def test_predict_mvp():
    """ Test mvp """
    nba = NBA()
    assert nba.predict_mvp()== "Donovan Mitchell"
        
def test_best_shooter():
    """ Test bestshooter """
    nba = NBA()
    assert nba.best_shooter('Lal', 'Hou')== "Quinn Cook"

def test_best_rebounder():
    """ Test best rebounder """
    nba = NBA()
    assert nba.best_rebounder('Lal', 'Hou')== "LeBron James"
