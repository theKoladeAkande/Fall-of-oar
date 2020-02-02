__metaclass__ = type 


class Settings:
    """A class that contains all the settings for Fall Of Oar"""

    def __init__(self):
        """ Intitalize with game's settings. """

        # Settings for the screen
        self.screen_width = 800
        self.screen_height = 600
        self.background_colour = (0, 0)

        # Spaceship's speed settings
        self.spaceship_speed = 1.2

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3
        