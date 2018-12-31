class GameStats():
    """monitor stats of the game"""

    def __init__(self, ai_settings):
        """initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # game is active when started
        self.game_active = True

    def reset_stats(self):
        """initialize variable stats during game"""
        self.ships_left = self.ai_settings.ship_limit
