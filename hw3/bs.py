""" A subclass of a constraint problem to solve an n-queens problem of
    a given size with a given solver """

from constraint import *

class BS(Problem):
    
    def __init__(self, n=6, solver=None):

        """N is the size of the board, solver is the CSP solver
           that will be used to solve the problem """

        
