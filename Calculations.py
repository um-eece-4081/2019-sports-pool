#The calculations methods will reside here.
#Let's get this bread

def calcWinner(team1Score, team2Score, betLine):
    return team1Score > (team2Score + betLine)

def calcUserPoints(userChoice, team1Score, team2Score, betLine):
    if(userChoice == team1 and calcWinner(team1Score, team2Score, betline)):
        userPoint += 1
    return userPoint

def UserBetPoints(SeasonUserWin,UserScore,WeeklyUserWin,SeasonUser,WeeklyUser,WeeklyUserGOWWin,SeasonUserGOWWin): #Basic Point Layout
    if SeasonUser&SeasonUserWin==True:
        UserScore+1
    else:
        UserScore

    if WeeklyUser&WeeklyUserWin==True:
        UserScore+1
    else:
        UserScore

    if WeeklyUser & WeeklyUserGOWWin == True:
        UserScore + 2
    else:
        UserScore

    if SeasonUser & SeasonUserGOWWin == True:
        UserScore + 2
    else:
        UserScore
        return UserScore
