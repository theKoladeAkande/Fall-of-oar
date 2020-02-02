import sys


import pygame


from space_ship import SpaceShip


from settings import Settings



from bullet import Bullet


__metaclass__ = type 


class FallOfOar():
    """ Manages game's properties and assets. """

    def __init__(self):
        """Initialize game, create screen objects and other required resources. """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Fall Of Oar")
        self.spaceship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()



    def run_game(self):
        """ Runs the main loop for the game. """
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_bullets()
            self._update_screen()



    def _check_events(self):
        """ Listens for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """ Listens and take action on key press events"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True
        elif event.key == pygame.K_x:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Listens and take actions on key release events"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False



    def _fire_bullet(self):
        """Creates new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """ Update the bullets position and deletes old bullets"""
        self.bullets.update()
        # Delete bullets no longer showing on the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)





    def _update_screen(self):
        """ updates the images and draw them to screen"""
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()





if __name__ == "__main__":
    # create game instance, run game
    foor = FallOfOar()
    foor.run_game()
