import asyncio
import pygame, sys
from settings import *
from level import Level


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('GameName')
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.main_sound = pygame.mixer.Sound('./audio/main.mp3')
        self.death_sound = pygame.mixer.Sound('./audio/rip.mp3')
        self.loading_sound = pygame.mixer.Sound('./audio/loading.mp3')


        self.game_running = True

        self.game_over_font = pygame.font.Font(UI_FONT, 48)
        self.game_over_text = self.game_over_font.render("GAME OVER", True, (255, 0, 0))  # Red text
        self.text_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.start_font = pygame.font.Font(UI_FONT, 48)
        self.start_text = self.game_over_font.render("RPG GAME", True, (255, 0, 0))  # Red text
        self.start_rect = self.start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2- 100))
        self.empty_text = self.game_over_font.render("------", True, (255, 0, 0))  # Red text
        self.empty_rect = self.start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.start2_text = self.game_over_font.render("CONTROLS - WASD", True, (255, 0, 0))  # Red text
        self.start2_rect = self.start2_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.start3_text = self.game_over_font.render("WEAPON SWAP - Q", True, (255, 0, 0))  # Red text
        self.start3_rect = self.start3_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.start4_text = self.game_over_font.render("MAGIC SWAP - E", True, (255, 0, 0))  # Red text
        self.start4_rect = self.start4_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        self.start5_text = self.game_over_font.render("WEAPON - SPACE", True, (255, 0, 0))  # Red text
        self.start5_rect = self.start5_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        self.start6_text = self.game_over_font.render("MAGIC - CTRL", True, (255, 0, 0))  # Red text
        self.start6_rect = self.start6_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))


    async def run(self):
        self.main_sound.set_volume(0.01)
        self.main_sound.play(loops=-1)

        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if player_stats['health'] <= 0:
                self.game_running = False
                self.main_sound.set_volume(0)
                self.death_sound.set_volume(0.01)
                self.death_sound.play()
                pygame.time.delay(250)
                self.screen.fill('black')
                self.screen.blit(self.game_over_text, self.text_rect)
                pygame.display.flip()
                pygame.time.delay(2000)





            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            await asyncio.sleep(0)




if __name__ == '__main__':
    game = Game()
    game.loading_sound.set_volume(0.02)
    game.loading_sound.play()
    game.screen.blit(game.start_text, game.start_rect)
    game.screen.blit(game.start2_text, game.start2_rect)
    game.screen.blit(game.start3_text, game.start3_rect)
    game.screen.blit(game.start4_text, game.start4_rect)
    game.screen.blit(game.start5_text, game.start5_rect)
    game.screen.blit(game.start6_text, game.start6_rect)
    pygame.display.flip()
    pygame.time.delay(5000)
    game.loading_sound.stop()
    asyncio.run(game.run())



