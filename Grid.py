import numpy as np
import random as rnd


class Grid:

    def __init__(self, n, m, mines):
        self.N = n * m
        self.n = n
        self.m = m
        self.bomb_matrix = np.zeros([n, m])
        self.resolve_matrix = np.zeros([n, m])
        self.unopened = np.ones([n,m])
        self.flags = np.zeros([n, m])
        self.mines = mines

    def start_game(self, n_ind, m_ind):
        self.bomb_matrix = np.zeros([self.n, self.m])
        self.resolve_matrix = np.zeros(([self.n,self.m]))
        self.unopened = np.ones([self.n, self.m])
        self.flags = np.zeros([self.n, self.m])
        n = self.n
        m = self.m
        available_modules = list(range(0, self.N))

        for nn in [n_ind - 1, n_ind, n_ind + 1]:
            for mm in [m_ind - 1, m_ind, m_ind + 1]:
                available_modules.remove(nn * n + mm)

        rnd.shuffle(available_modules)

        for ind_mine in available_modules[0:self.mines]:
            m_mine = int(ind_mine / n)
            n_mine = ind_mine % n
            self.bomb_matrix[n_mine, m_mine] = 1

        for ii in range(0, n):
            for jj in range(0, m):
                if self.bomb_matrix[ii, jj] == 1:
                    continue
                # Calculate adjacent bombs
                (ii_lower,ii_higher, jj_lower, jj_higher) = self.getAdjacentIndexes(ii, jj)

                self.resolve_matrix[ii, jj] = np.sum(self.bomb_matrix[ii_lower:ii_higher, jj_lower:jj_higher])

    def getEvent(self, n_ind, m_ind):
        block = self.bomb_matrix[n_ind, m_ind]
        if self.flags[n_ind,m_ind] == 1:
            return -2
        elif block == 1:
            return -1
        elif self.unopened[n_ind,m_ind] == 0:
            return -2
        else:
            self.unopened[n_ind, m_ind] = 0
            return int(self.resolve_matrix[n_ind, m_ind])

    def flag(self, n_ind, m_ind):
        self.flags[n_ind, m_ind] = (self.flags[n_ind, m_ind] + 1) % 2
        self.unopened[n_ind, m_ind] = (self.unopened[n_ind, m_ind] + 1) % 2
        return self.flags[n_ind, m_ind]

    def forceFlag(self,n_ind,m_ind):
        if self.unopened[n_ind,m_ind] == 1 and self.flags[n_ind,m_ind] == 0:
            self.flags[n_ind, m_ind] = 1
            self.unopened[n_ind, m_ind] = 0
            return True
        return False


    def getResolve(self, n_ind, m_ind):
        return self.resolve_matrix[n_ind, m_ind]

    def getAdjacentUnopened(self,ii,jj):
        (ii_lower, ii_higher, jj_lower, jj_higher) = self.getAdjacentIndexes(ii, jj)
        return np.sum(self.unopened[ii_lower:ii_higher, jj_lower:jj_higher])

    def getAdjacentFlags(self,ii,jj):
        (ii_lower, ii_higher, jj_lower, jj_higher) = self.getAdjacentIndexes(ii, jj)
        return np.sum(self.flags[ii_lower:ii_higher,jj_lower:jj_higher])

    def getAdjacentIndexes(self, ii, jj):
        ii_lower = ii - 1
        ii_higher = ii + 2
        jj_lower = jj - 1
        jj_higher = jj + 2
        if ii == 0:
            ii_lower = ii
        if jj == 0:
            jj_lower = jj
        if ii == self.n:
            ii_higher = ii + 1
        if jj == self.m:
            jj_higher = jj + 1
        return ii_lower, ii_higher, jj_lower, jj_higher

    def isUnopened(self,ii,jj):
        if self.unopened[ii,jj] == 1:
            return True
        else:
            return False
