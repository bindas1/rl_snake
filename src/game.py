import pygame
from snake import Snake


class Game:
    # rgb colors
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    DARK_GREEN = (0, 100, 0)
    LIGHT_GRASS = (65,152,10)
    DARK_GRASS = (19,133,16)

    RED = (200,0,0)
    BLUE1 = (0, 0, 255)
    BLUE2 = (0, 100, 255)

    def __init__(self, block_size=40, blocks_wide=30, blocks_height=20, padding=True):
        pygame.init()
        self.block_size = block_size
        self.grid_size = (blocks_wide, blocks_height)
        self.width, self.height = blocks_wide * block_size, blocks_height * block_size
        self.padding = padding
        if self.padding:
            self.width += 2 * block_size
            self.height += 2 * block_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.snake = Snake(self.width, self.height)
        pygame.display.set_caption("RL Snake")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_1:
                    self.play_manual()
                elif event.key == pygame.K_2:
                    self.play_ai()

    def color_block(self, x, y, color):
        if self.padding:
            x += self.block_size
            y += self.block_size
        pygame.draw.rect(self.screen, color, (x, y, self.block_size, self.block_size))


    def play_manual(self):
        while self.running:
            self.render()
            self.handle_events()
            # self.snake.handle_input()
            # self.snake.update()
            self.clock.tick(10)

    def play_ai(self):
        while self.running:
            self.handle_events()
            # self.ai.make_decision()
            # self.snake.update()
            self.render()
            self.clock.tick(10)

    def render(self):
        self.screen.fill(Game.BLACK)
        if self.padding:
            pygame.draw.rect(self.screen, Game.DARK_GREEN, (0, 0, self.width, self.block_size))
            pygame.draw.rect(self.screen, Game.DARK_GREEN, (0, 0, self.block_size, self.height))
            pygame.draw.rect(self.screen, Game.DARK_GREEN, (0, self.height-self.block_size, self.width, self.block_size))
            pygame.draw.rect(self.screen, Game.DARK_GREEN, (self.width-self.block_size, 0, self.block_size, self.height))
        # draw grass grid
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if (i + j) % 2 == 0:
                    self.color_block(i * self.block_size, j * self.block_size, Game.LIGHT_GRASS)
                else:
                    self.color_block(i * self.block_size, j * self.block_size, Game.DARK_GRASS)
        
        # self.snake.draw(self.screen)
        pygame.display.flip()

    def main_menu(self):
        welcome_font = pygame.font.Font(None, 36)
        menu_font = pygame.font.Font(None, 24)

        welcome_text = welcome_font.render("Welcome to RL Snake!", True, (255, 255, 255))
        manual_text = menu_font.render("1. Play manually", True, (255, 255, 255))
        ai_text = menu_font.render("2. Let AI play", True, (255, 255, 255))

        while self.running:
            self.handle_events()

            self.screen.fill(Game.BLACK)
            self.screen.blit(welcome_text, (self.width // 2 - welcome_text.get_width() // 2, 100))
            self.screen.blit(manual_text, (self.width // 2 - manual_text.get_width() // 2, 200))
            self.screen.blit(ai_text, (self.width // 2 - ai_text.get_width() // 2, 250))

            pygame.display.flip()
            self.clock.tick(10)

if __name__ == "__main__":
    game = Game()
    game.main_menu()
    pygame.quit()
