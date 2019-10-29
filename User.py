class User:
    def __init__(self, is_winston_cup, betting_sheet, weekly_points, winston_points, user_id):
        self.is_winston_cup = is_winston_cup
        self.betting_sheet = betting_sheet
        self.weekly_points = weekly_points
        self.winston_points = winston_points
        self.user_id = user_id
        self.currentPoints = currentPoints
    def get_is_winston_cup(self):
        return self.is_winston_cup
    def get_betting_sheet(self):
        return self.betting_sheet
    def get_weekly_points(self):
        return self.weekly_points
    def get_winston_points(self):
        return self.winston_points
    def set_weekly_points(self, we_points):
        self.weekly_points = w_points
    def set_winston_points(self, wi_points):
        self.winston_points = wi_points
    def get_user_id(self):
        return self.user_id
