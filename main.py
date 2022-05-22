import pygame
from GameController import GameController

pygame.font.init()

window_width = 1000
window_height = 700


def main():

    N = 30
    M = 16
    mines = 40

    Clock = pygame.time.Clock()

    # Set up the drawing window

    running = True
    # INIT gameController
    gc = GameController(window_width, window_height, N, M, mines)
    while running:

        # Run until the user asks to quit

        gc.drawGrid()

        # MAIN LOOP
        game_started = False
        game_lost = False
        while not game_lost:
            Clock.tick(10)
            (button1, button2, button3) = pygame.mouse.get_pressed(num_buttons=3)
            if button1:
                (n_pos, m_pos) = gc.getMousePosition()
                if not game_started:
                    gc.startNewGame(n_pos, m_pos)
                    game_started = True
                gc.gridChange(n_pos, m_pos)
                game_lost = gc.getGameState()
            elif button3:
                (n_pos, m_pos) = gc.getMousePosition()
                gc.toggleFlag(n_pos, m_pos)

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Flip the display
            pygame.display.update()

        # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
