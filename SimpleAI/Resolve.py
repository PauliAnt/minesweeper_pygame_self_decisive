class Resolve:

    def __init__(self, n_ind, m_ind, remaining, unopened):
        self.n = n_ind
        self.m = m_ind
        self.remaining = remaining
        self.unopened = unopened

    def update(self, N):
        self.unopened = N

    def flag(self, n_ind, m_ind):
        if abs(self.n - n_ind) <= 1 and abs(self.m - m_ind) <= 1:
            self.remaining -= 1

    def checkSolved(self):
        if self.remaining == 0:
            return 0
        if self.unopened == self.remaining:
            return 1
        else:
            return -1

    def getIndex(self):
        return self.n,self.m

    def getRemaining(self):
        return self.remaining

    def getUnopened(self):
        return self.unopened

    def printInfo(self):
        print("Position ({},{}), remaining: {}, unopened: {}".format(self.n,self.m,self.remaining,self.unopened))