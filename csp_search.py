from cspProblem import Variable, CSP, Constraint
from searchProblem import Arc, Search_problem

# define the variables with their domain
A = Variable('A', {1, 2, 3, 4})
B = Variable('B', {1, 2, 3, 4})
C = Variable('C', {1, 2, 3, 4})
D = Variable('D', {1, 2, 3, 4})
E = Variable('E', {1, 2, 3, 4})
F = Variable('F', {1, 2, 3, 4})
G = Variable('G', {1, 2, 3, 4})
H = Variable('H', {1, 2, 3, 4})

# define the helper functions for constraints
def not_equal(var1, var2):
    """Returns a constraint that ensures two variables are not equal."""
    return Constraint([var1, var2], lambda a, b: a != b)

def not_equal_2(var1, var2):
    """Returns a constraint that ensures var1 != var2 - 2."""
    return Constraint([var1, var2], lambda a, b: a != b - 2)

def not_equal_1(var1, var2):
    """Returns a constraint that ensures var1 != var2 - 1."""
    return Constraint([var1, var2], lambda a, b: a != b - 1)

def greater_than(var1, var2):
    """Returns a constraint that ensures var1 > var2."""
    return Constraint([var1, var2], lambda a, b: a > b)

def less_than(var1, var2):
    """Returns a constraint that ensures var1 < var2."""
    return Constraint([var1, var2], lambda a, b: a < b)

def less_than_1(var1, var2):
    """Returns a constraint that ensures var1 < var2 - 1."""
    return Constraint([var1, var2], lambda a, b: a < b - 1)

def no_more_than(var1, var2):
    """Returns a constraint that ensures var1 <= var2."""
    return Constraint([var1, var2], lambda a, b: a <= b)

def no_less_than(var1, var2):
    """Returns a constraint that ensures var1 >= var2."""
    return Constraint([var1, var2], lambda a, b: a >= b)

def difference_is(var1, var2, diff):
    """Returns a constraint that ensures |var1 - var2| = diff."""
    return Constraint([var1, var2], lambda a, b: abs(a - b) == diff)

def is_even_difference(var1, var2):
    """Returns a constraint that ensures |var1 - var2| is even."""
    return Constraint([var1, var2], lambda a, b: abs(a-b) % 2 == 0)

def is_odd_difference(var1, var2):
    """Returns a constraint that ensures |var1 - var2| is odd."""
    return Constraint([var1, var2], lambda a, b: abs(a - b) % 2 == 1)

# create the CSP problem and add the constraints
csp_problem = CSP(
    "Example_CSP",
    {A, B, C, D, E, F, G, H},
    [
        greater_than(A, G),          # A > G
        no_more_than(A, H),          # A <= H
        difference_is(F, B, 1),      # |F - B| = 1
        less_than(G, H),             # G < H
        difference_is(G, C, 1),      # |G - C| = 1
        is_even_difference(H, C),    # |H-C| is even
        not_equal(H, D),             # H != D 
        no_less_than(D, G),          # D >= G 
        not_equal(D, C),             # D != C
        not_equal(E, C),             # E != C
        less_than_1(E, D),           # E < D - 1
        not_equal_2(E, H),           # E != H - 2
        not_equal(G, F),             # G != F
        not_equal(H, F),             # H != F
        not_equal(C, F),             # C != F
        not_equal_1(D, F),           # D != F-1
        is_odd_difference(E, F)      # |E-F| is odd
    ]
)

class Search_from_CSP(Search_problem):
    """A search problem directly from the CSP.
    A node is a variable:value dictionary"""
    
    def __init__(self, csp, variable_order=[A, B, C, D, E, F, G, H]):
        self.csp = csp
        self.fail_count = 0
        if variable_order:
            assert set(variable_order) == set(csp.variables)
            assert len(variable_order) == len(csp.variables)
            self.variables = variable_order
        else:
            self.variables = list(csp.variables)

    def is_goal(self, node):
        """returns whether the current node is a goal for the search"""
        return len(node) == len(self.csp.variables)

    def start_node(self):
        """returns the start node for the search"""
        return {}

    def neighbors(self, node):
        """returns a list of the neighboring nodes of node"""
        var = self.variables[len(node)]  # the next variable to assign
        res = []
        for val in var.domain:
            new_env = node | {var: val}  # dictionary union
            if self.csp.consistent(new_env):  # Check if consistent
                res.append(Arc(node, new_env))  # Append as Arc
            else:
                self.fail_count += 1
        return res
        
    def get_fail_count(self):
        """return the number of failing branches"""
        return self.fail_count

import cspExamples
from searchGeneric import Searcher

def solver_from_searcher(csp):
    """Depth-first search solver"""
    path = Searcher(Search_from_CSP(csp)).search()
    search_problem = Search_from_CSP(csp)
    if path is not None:
        print("The number of failing branches:", search_problem.get_fail_count())
        return path.end()
    else:
        print("The number of failing branches:", search_problem.get_fail_count())
        return None

if __name__ == "__main__":
    solution = solver_from_searcher(csp_problem)
    print("Solution:", solution)
