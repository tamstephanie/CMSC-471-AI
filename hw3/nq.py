""" A subclass of a constraint problem to solve an n-queens problem of
    a given size with a given solver """

from constraint import *

class NQ(Problem):

    def __init__(self, n=8, solver=None):

        """N is the size of the board, solver is the CSP solver
           that will be used to sove the problem """

        # call the base class init method
        super(NQ, self).__init__(solver=solver)

        # set any NQ instance variables needed
        columns = range(n)
        rows = range(n)

        # define CSP variables with their domains
        self.addVariables(columns, rows)

        # add CSP constraints 
        for col1 in columns:
            for col2 in columns:
                if col1 < col2:

                    """ constraints for the queen are set: nothing in the same row, column, and diagonals if possible """
                    self.addConstraint(lambda row1, row2, col1=col1, col2=col2:
                                          abs(row1-row2) != abs(col1-col2) and row1 != rows, (col1, col2))
        

