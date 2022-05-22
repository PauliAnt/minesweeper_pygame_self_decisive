import pygame
import GameController
from Resolve import Resolve
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class SimpleAiController(GameController.GameController):

    def __init__(self, window_width, window_height, N, M, mines):
        super().__init__(window_width, window_height, N, M, mines)
        self.resolve_matrix = np.zeros([N, M])
        self.resolve_list = []

    def startNewGame(self, n_pos, m_pos):
        super().startNewGame(n_pos,m_pos)
        self.resolve_matrix = np.zeros([self.N, self.M])
        self.resolve_list = []

    def gridChange(self, n_ind, m_ind):
        super().gridChange(n_ind, m_ind)

        # Check adjacent resolves and add them to list
        (n_lower, n_higher, m_lower, m_higher) = self.getAdjacentBlocks(n_ind, m_ind)
        for ii in range(n_lower, n_higher):
            for jj in range(m_lower, m_higher):
                if self.resolve_matrix[n_ind, m_ind] == 0:
                    resolve_num = self.G.getResolve(n_ind, m_ind)
                    if resolve_num != 0:
                        resolve = self.createResolve(n_ind, m_ind, resolve_num)
                        self.resolve_list.append(resolve)
                        self.resolve_matrix[n_ind, m_ind] = 1


    def createResolve(self, n_ind, m_ind, resolve_num):
        unopened = self.G.getAdjacentUnopened(n_ind, m_ind)
        remaining = resolve_num - self.G.getAdjacentFlags(n_ind, m_ind)
        return Resolve(n_ind, m_ind, remaining, unopened)

    def addFlag(self, n_ind, m_ind):
        super().toggleFlag(n_ind, m_ind)
        for resolve in self.resolve_list:
            resolve.flag(n_ind, m_ind)

    def updateResolves(self):
        for resolve in self.resolve_list:
            (n,m) = resolve.getIndex()
            N = self.G.getAdjacentUnopened(n,m)
            resolve.update(N)

    def checkSolved(self):
        for resolve in self.resolve_list:
            action = resolve.checkSolved()
            if action == 0:
                (n, m) = resolve.getIndex()
                self.fillRect(n, m, outlineColor=GREEN)
                self.resolve_list.remove(resolve)
                self.openAdjacent(n, m)
            elif action == 1:
                (n, m) = resolve.getIndex()
                self.fillRect(n, m, outlineColor=GREEN)
                self.flagAdjacent(n,m)
                self.resolve_list.remove(resolve)

    def flagUp(self,n_ind,m_ind):
        flagStatus = self.G.forceFlag(n_ind, m_ind)
        if flagStatus:
            self.fillRect(n_ind, m_ind, fillColor=RED, outlineColor=BLACK)
            for resolve in self.resolve_list:
                resolve.flag(n_ind, m_ind)

    def getResolveInfo(self,n_ind,m_ind):
        for resolve in self.resolve_list:
            (nn, mm) = resolve.getIndex()
            if nn == n_ind and mm == m_ind:
                resolve.printInfo()
                return
        print("Resolved position ({}, {})".format(n_ind,m_ind))
