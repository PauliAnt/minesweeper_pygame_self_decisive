import pygame
from Grid import Grid

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (128, 128, 128)
RED = (255, 0, 0)


class GameController:

    def __init__(self, window_width, window_height, N, M, mines):

        self.M = M
        self.N = N
        self.window_height = window_height
        self.window_width = window_width
        block_width = window_width / M
        block_height = (window_height - 200) / N

        self.block_size = int(min(block_height, block_width))
        self.vertical_offset = int(((window_height - 200) - self.block_size * N) / 2)
        self.horizontal_offset = int((window_width - self.block_size * M) / 2)

        font_size = int(self.block_size * 1.3)
        self.font = pygame.font.SysFont("footlight.ttc", font_size)

        self.screen = pygame.display.set_mode([window_width, window_height])
        self.mines = mines
        self.game_lost = False

    def startNewGame(self, n_pos, m_pos):
        self.G = Grid(self.N, self.M, self.mines)
        self.G.start_game(m_pos, n_pos)
        self.game_lost = False

    def drawGrid(self):
        ho = self.horizontal_offset
        vo = self.vertical_offset
        block = self.block_size
        self.screen.fill(BLACK)
        self.screen.fill(GREY, (ho, 200 + vo, self.M * block, self.N * block))
        print(self.screen.get_width())
        for x in range(ho, self.window_width - ho, block):
            for y in range(200 + vo, self.window_height - vo, block):
                rect = pygame.Rect(x, y, block, block)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def gridChange(self, n_ind, m_ind):
        ho = self.horizontal_offset
        vo = self.vertical_offset
        block = self.block_size
        event = self.G.getEvent(n_ind, m_ind)

        if event == -2:
            return False

        #self.screen.fill(BLACK, (
        #ho + n_ind * block, 200 + vo + m_ind * block, block, block))
        self.fillRect(n_ind, m_ind,fillColor=BLACK,outlineColor=GREY)
        if event == 0:

            n_lower = n_ind - 1
            n_higher = n_ind + 2
            m_lower = m_ind - 1
            m_higher = m_ind + 2
            if n_ind == 0:
                n_lower = n_ind
            if m_ind == 0:
                m_lower = m_ind
            if n_ind == self.N - 1:
                n_higher = n_ind + 1
            if m_ind == self.M - 1:
                m_higher = m_ind + 1

            for ii in range(n_lower, n_higher):
                for jj in range(m_lower, m_higher):
                    self.gridChange(ii, jj)
        elif event == -1:
            self.game_lost = True
        else:
            num = self.font.render(str(event), "TRUE", "Blue")
            self.screen.blit(num, (ho + n_ind * block, 200 + vo + m_ind * block))
        return False

    def toggleFlag(self, n_ind, m_ind):
        flag_status = self.G.flag(n_ind, m_ind)
        ho = self.horizontal_offset
        vo = self.vertical_offset
        block = self.block_size
        if flag_status == 1:
            self.fillRect(n_ind, m_ind,fillColor=RED,outlineColor=BLACK)
        if flag_status == 0:
            self.fillRect(n_ind,m_ind,fillColor=GREY,outlineColor=WHITE)


    def getMousePosition(self):
        (x, y) = pygame.mouse.get_pos()
        m_pos = int((y - 200 + self.vertical_offset) / self.block_size)
        n_pos = int((x - self.horizontal_offset) / self.block_size)
        return n_pos, m_pos

    def getGameState(self):
        return self.game_lost

    def fillRect(self,n_ind,m_ind,fillColor=None, outlineColor=None):
        rect = pygame.Rect(self.horizontal_offset + n_ind * self.block_size, 200 + self.vertical_offset + m_ind * self.block_size,
                self.block_size, self.block_size)
        if fillColor is not None:
            self.screen.fill(fillColor, rect)
        if outlineColor is not None:
            pygame.draw.rect(self.screen, outlineColor, rect, 1)


