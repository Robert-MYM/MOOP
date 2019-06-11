from math import sqrt,cos,pi
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution

cost=[2835,5832,596,148]
CRF=[0.1175,0.1175,0.1175,0.2638]
Ann=[333,685.02,70.01,39.04]
MO=[67.7,116.64,38.08,2.96]  #Maintance and operation cost
AEP=100000.0

class HRES(FloatProblem):

    def __init__(self, number_of_variables: int=4):
        super(HRES, self).__init__()
        self.number_of_variables = number_of_variables
        self.number_of_objectives = 2
        self.number_of_constraints = 1

        self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
        self.obj_labels = ['LCE', 'P']

        self.lower_bound = self.number_of_variables * [1.0]
        self.upper_bound = self.number_of_variables * [AEP]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution) -> FloatSolution:

        solution.objectives[0] = ((CRF[0]*cost[0]+Ann[0]+(MO[0]*20))*solution.variables[0]+(CRF[1]*cost[1]+Ann[1]+(MO[1]*20))*solution.variables[1]+(CRF[2]*cost[2]+Ann[2]+(MO[2]*20))*solution.variables[2]+(CRF[3]*cost[3]+Ann[3]+(MO[3]*20))*solution.variables[3])/sum(solution.variables)
        solution.objectives[1] = solution.variables[3] * solution.variables[3] + solution.variables[2]
        self.__evaluate_constraints(solution)
        return solution

    def __evaluate_constraints(self, solution: FloatSolution) -> None:
        constraints = [0.0 for _ in range(self.number_of_constraints)]

        constraints[0] = (solution.variables[0]+solution.variables[1]+solution.variables[2]+solution.variables[3])-AEP
        #constraints[1] = (AEP*1.1)-(solution.variables[0] + solution.variables[1] + solution.variables[2]+solution.variables[3])

        overall_constraint_violation = 0.0
        number_of_violated_constraints = 0.0
        for constrain in constraints:
            if constrain < 0.0:
                overall_constraint_violation += constrain
                number_of_violated_constraints += 1

        solution.attributes['overall_constraint_violation'] = overall_constraint_violation
        solution.attributes['number_of_violated_constraints'] = number_of_violated_constraints


    def get_name(self):
        return 'HRES'