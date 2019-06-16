# PF-Exer-28

# This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    team1_count=match_tuple.count("Team1")
    team2_count=match_tuple.count("Team2")
    if(team1_count>team2_count):
        return "Team1"
    elif(team2_count>team1_count):
        return "Team2"
    else:
        return "Tie"

# Invoke the function with each of the print statements given below
# print(find_winner_of_the_day("Team1", "Team2", "Team1"))
# print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))