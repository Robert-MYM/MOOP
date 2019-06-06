from math import sqrt,cos,pi
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution

class DTLZ1(FloatProblem):

    def __init__(self, number_of_variables: int=12):
        super(DTLZ1, self).__init__()
        self.number_of_variables = number_of_variables
        self.number_of_objectives = 3
        self.number_of_constraints = 0

        self.obj_directions = [self.MINIMIZE, self.MINIMIZE, self.MINIMIZE]
        self.obj_labels = ['x', 'y' ,'z']

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

    def evaluate(self, solution: FloatSolution) -> FloatSolution:
        g = self.eval_g(solution)

        solution.objectives[0] = 0.5*solution.variables[0]*solution.variables[1]*(1+g)
        solution.objectives[1] = 0.5*solution.variables[0]*(1-solution.variables[1])*(1+g)
        solution.objectives[2] = 0.5*(1-solution.variables[0])*(1+g)

        return solution

    def eval_g(self, solution: FloatSolution):
        g = sum([((x-0.5)*(x-0.5)-cos(20*pi*(x-0.5))) for x in solution.variables[2:]])
        return 100*(g+10.0)

    def get_name(self):
        return 'DTLZ1'