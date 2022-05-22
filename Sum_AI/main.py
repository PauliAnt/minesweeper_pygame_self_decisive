import pygame
from SumAIController import SumAIController
pygame.font.init()

window_width = 1000
window_height = 700


def main():

    N = 30
    M = 16
    mines = 99

    Clock = pygame.time.Clock()

    # Set up the drawing window

    running = True
    # INIT gameController
    gc = SumAIController(window_width, window_height, N, M, mines)
    while running:

        # Run until the user asks to quit

        gc.drawGrid()

        # MAIN LOOP
        game_lost = False
        gc.startNewGame(N//2, M//2)
        gc.gridChange(N//2, M//2)
        while not game_lost:
            Clock.tick(10)
            (button1, button2, button3) = pygame.mouse.get_pressed(num_buttons=3)

            # Check safe spaces
            gc.updateResolves()
            solved = gc.checkSolved()
            game_lost = gc.getGameState()
            if not solved:
                n_min, m_min = gc.calculateSums()
                gc.gridChange(n_min,m_min)

            if button1:
                (n_pos, m_pos) = gc.getMousePosition()
                gc.gridChange(n_pos, m_pos)
            elif button3:
                (n_pos, m_pos) = gc.getMousePosition()
                gc.addFlag(n_pos, m_pos)

            elif button2:
                (n_pos, m_pos) = gc.getMousePosition()
                gc.getResolveInfo(n_pos,m_pos)

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Flip the display
            pygame.display.update()
        pygame.time.wait(2000)


        # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()