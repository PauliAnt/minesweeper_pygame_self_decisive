import numpy as np

import SimpleAI.SimpleAiController as simple
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (128, 128, 128)
RED = (255, 0, 0)


class SumAIController(simple.SimpleAiController):
    def calculateSums(self):
        sum_array = np.zeros([self.N,self.M,2])
        for resolve in self.resolve_list:
            remaining = resolve.getRemaining()
            unopened = resolve.getUnopened()
            (n, m) = resolve.getIndex()
            (n_lower, n_higher, m_lower, m_higher) = self.getAdjacentBlocks(n, m)
            for ii in range(n_lower, n_higher):
                for jj in range(m_lower, m_higher):
                    sum_array[ii, jj,0] += remaining/unopened
                    sum_array[ii,jj,1] += 1

        min_num = np.inf
        n_min = -1
        m_min = -1
        for nn in range(0,self.N):
            for mm in range(0,self.M):
                if self.G.isUnopened(nn,mm) and sum_array[nn,mm,1] != 0:
                    self.fillRect(nn,mm,fillColor=GREY,outlineColor=WHITE)
                    number = round(sum_array[nn,mm,0]/sum_array[nn,mm,1],1)
                    if number < min_num:
                        min_num = number
                        n_min = nn
                        m_min = mm
                    self.smallFontInRect(nn,mm,str(number),"Red")
        self.fillRect(n_min,m_min,outlineColor=RED)
        return n_min,m_min
