from Grid import Grid
import pygame

pygame.font.init()

window_width = 1000
window_height = 700
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (128, 128, 128)
RED = (255,0,0)
def main():

    global SCREEN, N, M, FONT, HORIZONTAL_OFFSET, VERTICAL_OFFSET, BLOCK_SIZE
    N = 16
    M = 16
    mines = 40



    HORIZONTAL_OFFSET = 0
    VERTICAL_OFFSET = 0
    block_width = window_width / M
    block_height = (window_height - 200) / N

    BLOCK_SIZE = int(min(block_height,block_width))
    VERTICAL_OFFSET = int(((window_height - 200) - BLOCK_SIZE * N) / 2)
    HORIZONTAL_OFFSET = int((window_width - BLOCK_SIZE * M) / 2)

    print([VERTICAL_OFFSET,HORIZONTAL_OFFSET])
    fontsize = int(BLOCK_SIZE * 1.3)
    FONT = pygame.font.SysFont("footlight.ttc", fontsize)


    Clock = pygame.time.Clock()

    # Set up the drawing window
    SCREEN = pygame.display.set_mode([window_width, window_height])
    running = True
    while running:

    # Run until the user asks to quit

        drawGrid()


        # MAIN LOOP
        game_started = False
        game_lost = False
        while not game_lost:
            Clock.tick(10)
            (button1, button2, button3) = pygame.mouse.get_pressed(num_buttons=3)
            if button1:
                (n_pos, m_pos) = getMousePosition()
                if not game_started:
                    G = Grid(N,M,mines)
                    G.start_game(m_pos,n_pos)
                    game_started = True
                game_lost= gridChange(G,n_pos,m_pos)
            elif button3:
                (n_pos, m_pos) = getMousePosition()
                flag_status = G.flag(n_pos,m_pos)
                print(flag_status)
                if flag_status == 1:
                    drawFlag(n_pos,m_pos)
                if flag_status == 0:
                    removeFlag(n_pos,m_pos)

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            getMousePosition()
            # Flip the display
            pygame.display.update()


        # Done! Time to quit.
    pygame.quit()

def drawGrid():
    SCREEN.fill(BLACK)
    SCREEN.fill(GREY,(HORIZONTAL_OFFSET,200+VERTICAL_OFFSET,M*BLOCK_SIZE,N*BLOCK_SIZE))
    print(SCREEN.get_width())
    for x in range(HORIZONTAL_OFFSET, window_width-HORIZONTAL_OFFSET, BLOCK_SIZE):
        for y in range(200+VERTICAL_OFFSET, window_height - VERTICAL_OFFSET, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def gridChange(G,n_ind,m_ind):
    event = G.getEvent(n_ind, m_ind)

    if event == -2:
        return False

    SCREEN.fill(BLACK,(HORIZONTAL_OFFSET+n_ind*BLOCK_SIZE,200+VERTICAL_OFFSET+m_ind*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))
    if event == 0:

        n_lower = n_ind - 1
        n_higher = n_ind + 2
        m_lower = m_ind - 1
        m_higher = m_ind + 2
        if n_ind == 0:
            n_lower = n_ind
        if m_ind == 0:
            m_lower = m_ind
        if n_ind == N-1:
            n_higher = n_ind+1
        if m_ind == M-1:
            m_higher = m_ind+1

        for ii in range(n_lower,n_higher):
            for jj in range(m_lower,m_higher):
                gridChange(G,ii,jj)
    elif event == -1:
        return True
        print("lost")
    else:
        num = FONT.render(str(event), "TRUE", "Blue")
        SCREEN.blit(num, (HORIZONTAL_OFFSET + n_ind * BLOCK_SIZE, 200 + VERTICAL_OFFSET + m_ind * BLOCK_SIZE))
    return False

def drawFlag(n_ind,m_ind):
    SCREEN.fill(RED,(HORIZONTAL_OFFSET+n_ind*BLOCK_SIZE,200+VERTICAL_OFFSET+m_ind*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))

def removeFlag(n_ind,m_ind):
    SCREEN.fill(GREY, (HORIZONTAL_OFFSET + n_ind * BLOCK_SIZE, 200 + VERTICAL_OFFSET + m_ind * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def getMousePosition():
    (x,y) = pygame.mouse.get_pos()
    m_pos = int((y-200+VERTICAL_OFFSET) / BLOCK_SIZE)
    n_pos = int((x-HORIZONTAL_OFFSET)/BLOCK_SIZE)
    return n_pos,m_pos

if __name__ == "__main__":
        main()
