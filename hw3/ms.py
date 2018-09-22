""" A subclass of a constraint problem to find a magic square for a
    nxn grid and sum n*(n*n+1)/2. """

from constraint import *

class MS(Problem):

    def __init__(self, n=3, solver=None):

        """N is the size of the magic square, solver is the CSP solver
           that will be used to sove the problem """

        # call the base class init method
        super(MS, self).__init__(solver=solver)

        # set any MS instance variables needed
        total_sum = n*(n*n+1)/2

        # define CSP variables with their domains
        self.addVariables(range(0, n*n), range(1, (n*n)+1))

        # add CSP constraints: constraint must add up to n*(n*n+1)/2
        self.addConstraint(AllDifferentConstraint(), range(0, n*n))
        self.addConstraint(ExactSumConstraint(total_sum), [(n+1)*i for i in range(n)])        # top left corner to bottom right diagonal
        self.addConstraint(ExactSumConstraint(total_sum), [(n-1)*i for i in range(1, n+1)])   # top right corner to bottom left diagonal

        for row in range(n):
            self.addConstraint(ExactSumConstraint(total_sum), [row*n+i for i in range(n)])    # each row is constrained

        for col in range(n):
            self.addConstraint(ExactSumConstraint(total_sum), [col+n*i for i in range(n)])    # each column is constrained
