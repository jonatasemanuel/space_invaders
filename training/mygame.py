import sys, pygame


# class Settings():
#     def __init__(self) -> None:
#         self.screen_width = 1200
#         self.screen_heigth = 800
#         self.bg_color = (220, 220, 230)


def run():
    pygame.init()
    # ai_settings = Settings()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Blue game')
    bg_color = (150, 200, 230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run()
