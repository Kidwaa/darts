

def CalculateScore(Points, Current_Score):
    # Calculates Score of Player after adding points
    if Points > 0:
        New_Score = Current_Score
        New_Score = New_Score-Points
        if New_Score < 0:
            New_Score = New_Score+Points

    return New_Score


def player_won(Score_of_Player, Player_Name):
    # Calculates if player won
    if Score_of_Player == 0:
        print(f"{Player_Name} won")
        print("Game Over")
        return True

    else:
        return False


GameTotal = int(input("How many points is the game in?"))

n = 1
Players = []
while True:
    Player = input(
        f"Insert Name of Player {n}. If there are no more players, insert STOP")

    if Player == "STOP":
        break
    else:
        n = n+1
        Players.append(Player)

number_of_player = len(Players)

Player_Scores = dict.fromkeys(Players, GameTotal)

count = number_of_player
Flag = 1
while Flag == 1:

    for i in range(0, number_of_player):
        if 0 in list(Player_Scores.values()):
            Flag == 0
        else:
            score = int(input(f"Insert score of {Players[i]}"))
            New_Score = CalculateScore(score, list(Player_Scores.values())[i])
            Player_Scores[Players[i]] = New_Score
            print(f"Score of {Players[i]} is {New_Score}")
            print(Player_Scores)
            if player_won(New_Score, Players[i]) is True:
                Flag = 0
            else:
                continue
