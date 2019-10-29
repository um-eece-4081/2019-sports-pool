import User
#The calculations methods will reside here.
#Let's get this bread


def calc_winner(team1Score, team2Score, betLine):
    return team1Score > (team2Score + betLine)

def calc_user_points(user,userChoice, team1Score, team2Score, betLine):
    user.userPoint = get_weekly_points()
    if(userChoice == team1 and calcWinner(team1Score, team2Score, betline) or userChoice == team2 and not calcWinnter(team1Score, team2Score, betline)):
        userPoint += 1
    user.set_weekly_points(userPoint)
    return userPoint

def user_bet_points(season_user_win,user_score,weekly_user_win,season_user,weekly_user,weekly_user_gow_win,season_user_gow_win): #Basic Point Layout
    if season_user & season_user_win:
        user_score+1
    else:
        user_score

    if weekly_user & weekly_user_win:
        user_score+1
    else:
        user_score

    if weekly_user & weekly_user_gow_win:
        user_score + 2
    else:
        user_score

    if season_user & season_user_gow_win:
        user_score + 2
    else:
        user_score
        return user_score
