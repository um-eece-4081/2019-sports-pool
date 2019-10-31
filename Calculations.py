import scoringModels
#The calculations methods reside here.


def calc_weekly_winner(team1Score, team2Score, betLine):
    return team1Score > (team2Score + betLine)

def calc_weekly_points(user,userChoice, team1Score, team2Score, betLine):
    user_point = user.get_weekly_points()
    if(userChoice == team1 and calcWinner(team1Score, team2Score, betline) or userChoice == team2 and not calcWinnter(team1Score, team2Score, betline)):
        user_point += 1
    user.set_weekly_points(user_point)
    
def get_user_choices(user):
    return user_choices

def game_of_the_week(user, actual_score):
    user_choice = user.get_user_choices()
    return actual_score - user_choice[-1]

def score_all_users(user_list):
    for user in user_list:
        

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
