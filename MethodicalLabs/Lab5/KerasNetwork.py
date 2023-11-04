import tensorflow
import pygad.kerasga
import numpy
import pygad

def fitness_func(solution, sol_idx):
    global data_inputs, data_outputs, keras_ga, model

    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model,
                                                                 weights_vector=solution)

    model.set_weights(weights=model_weights_matrix)

    predictions = model.predict(data_inputs)

    mae = tensorflow.keras.losses.MeanAbsoluteError()
    abs_error = mae(data_outputs, predictions).numpy() + 0.00000001
    solution_fitness = 1.0 / abs_error

    return solution_fitness

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))


input_layer = tensorflow.keras.layers.Input(3)
dense_layer = tensorflow.keras.layers.Dense(5, activation="relu")
output_layer = tensorflow.keras.layers.Dense(1, activation="linear")

model = tensorflow.keras.Sequential()
model.add(input_layer)
model.add(dense_layer)
model.add(output_layer)

weights_vector = pygad.kerasga.model_weights_as_vector(model=model)

keras_ga = pygad.kerasga.KerasGA(model=model,
                                 num_solutions=10)

data_inputs = numpy.array([[0.03, 0.1, 0.25],
                           [0.5, 0.8, 0.6],
                           [1.6, 1.1, 1.4],
                           [3.1, 2.5, 3.1]])

data_outputs = numpy.array([[0.2], [0.5], [1.5], [2.2]])

num_generations = 300
num_parents_mating = 5
initial_population = keras_ga.population_weights

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       initial_population=initial_population,
                       fitness_func=fitness_func,
                       on_generation=callback_generation)
ga_instance.run()

ga_instance.plot_result(title="PyGAD & Keras - Покоління до Відповідності", linewidth=4)

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Показник найкращого отриманого результату : {solution_fitness}".format(solution_fitness=solution_fitness))
print("Індекс найкращого отриманого результату : {solution_idx}".format(solution_idx=solution_idx))


best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model,
                                                              weights_vector=solution)
model.set_weights(best_solution_weights)
predictions = model.predict(data_inputs)
print("Передбаченя : \n", predictions)

mae = tensorflow.keras.losses.MeanAbsoluteError()
abs_error = mae(data_outputs, predictions).numpy()
print("Абсолютна похибка : ", abs_error)

