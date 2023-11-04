import pygad
import numpy

function_inputs = [6, -3, 5.5, 2, -9, -5.7]
desired_output = 53


def fitness_func(solution, solution_idx):
    output = numpy.sum(solution*function_inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
    return fitness


num_generations = 100
num_parents_mating = 10
sol_per_pop = 20
num_genes = len(function_inputs)

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes)

ga_instance.run()

ga_instance.plot_result()