class GameStats():
    """monitor stats of the game"""

    def __init__(self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # game is not active when started
        self.game_active = False

        # never reset highest score
        self.high_score = 0

    def reset_stats(self):
        """initialize variable stats during game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
