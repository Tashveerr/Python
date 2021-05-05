class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (23, 0, 280)

        # Ship settings
        self.ship_speed = 0.5
        self.ship_limit = 10

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10000

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 3
