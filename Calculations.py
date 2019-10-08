#The calculations methods will reside here.
#Let's get this bread

def calcWinner(team1Score, team2Score, betLine):
    return team1Score > (team2Score + betLine)

def calcUserPoints(userChoice, team1Score, team2Score, betLine):
    if(userChoice == team1 && calcWinner(team1Score, team2Score, betline)):
        userPoint += 1
    return userPoint
