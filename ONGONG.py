import pygame
pygame.init()

WHITE = (255, 255, 255)


ToDo = input('what doing ')

display = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption('image')
image = pygame.image.load("C:\\Users\\vinsi\\Downloads\\jacquard-idye-poly-violet.jpg").convert()
display.blit(image, (0, 0))

def print_text(text, position, font_size):
    font = pygame.font.SysFont('Times New Roman', 24, False, False)
    surface = font.render(ToDo, False, WHITE)
    display.blit(surface, (0, 0))

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        print_text(ToDo, (200,200), 24)
        pygame.display.update()

game()
pygame.quit()