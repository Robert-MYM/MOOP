from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import BinaryTournamentSelection, BitFlipMutation, SPXCrossover,PolynomialMutation,SBXCrossover
from jmetal.problem.multiobjective.unconstrained import OneZeroMax
from jmetal.util.comparator import RankingAndCrowdingDistanceComparator, DominanceComparator
from jmetal.util.observer import ProgressBarObserver, VisualizerObserver
from jmetal.util.solution_list import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
import ZDT1,DTLZ1,HRES
if __name__ == '__main__':
    #binary_string_length = 512
    #problem = OneZeroMax(binary_string_length)
    #problem = ZDT1.ZDT1()
    problem = HRES.HRES()
    max_evaluations = 50000
    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        #mutation=BitFlipMutation(probability=1.0 / binary_string_length),
        mutation=PolynomialMutation(probability=1.0/problem.number_of_variables,distribution_index=20),
        #crossover=SPXCrossover(probability=1.0),
        crossover=SBXCrossover(probability=1.0,distribution_index=20),
        selection=BinaryTournamentSelection(comparator=RankingAndCrowdingDistanceComparator()),
        termination_criterion=StoppingByEvaluations(max=max_evaluations),
        #dominance_comparator=DominanceComparator()
    )

    algorithm.observable.register(observer=ProgressBarObserver(max=max_evaluations))
    algorithm.observable.register(observer=VisualizerObserver())

    algorithm.run()
    front = algorithm.get_result()

    # Save results to file
    print_function_values_to_file(front, 'FUN.' + algorithm.get_name() + "-" + problem.get_name())
    print_variables_to_file(front, 'VAR.' + algorithm.get_name() + "-" + problem.get_name())

    print('Algorithm (continuous problem): ' + algorithm.get_name())
    print('Problem: ' + problem.get_name())
    print('Computing time: ' + str(algorithm.total_computing_time))