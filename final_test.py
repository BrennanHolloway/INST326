from final_inst import  NBA, main
import pytest


def test_read_stats(path):
    
    tmp_file = path / "326nba.csv"
    team1 = 'Den'
    team2 = 'Okc'
    team3 = 'Lal'
    team4 = 'Hou'
    try:
       if main(tmp_file) :  
            print (f"{team1} vs the predicted winning team is: {team2}")
            print(f"{team1} is the next predicted champion of the NBA with a total wins of,  {team2}")
            print(f"The predicted MVP player of the year is: {team2}")
            print(f"The best shooter on the winning team between the matchup of {team3} and {team4} was Quinn Cook")
            print(f"The best rebounder on the winning team between the matchup of {team3} and {team4} was LeBron James")
    finally:
        tmp_file.unlink()
    