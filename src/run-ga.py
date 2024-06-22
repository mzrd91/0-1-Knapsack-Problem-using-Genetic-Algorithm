import random
import numpy as np
from selection import selection
from crossover import one_point_crossover, uniform_crossover, multi_parent_crossover
from mutation import mutation
from fitness import fitness

def run_ga(pop_size, chrom_len, num_generations, crossover_prob, mutation_prob, num_parents, 
           tournament_size, crossover_method, knapsack, c, alpha):

    best_solutions = []

    for i in range(30):
        population = [''.join([str(random.randint(0, 1)) for i in range(chrom_len)]) for j in range(pop_size)]

        for generation in range(num_generations):
            selected_population = selection(population, knapsack, tournament_size)
            offspring_population = []

            for i in range(int(pop_size/2)):
                parents = random.sample(selected_population, num_parents)
                if random.random() < crossover_prob:
                    if crossover_method == "uniform":
                        offspring1 = uniform_crossover(parents, chrom_len)
                        offspring2 = uniform_crossover(parents[::-1], chrom_len)
                    elif crossover_method == "one-point":
                        offspring1 = one_point_crossover(parents, chrom_len)
                        offspring2 = one_point_crossover(parents[::-1], chrom_len)
                    elif crossover_method == "multi-parent":
                        offspring1 = multi_parent_crossover(parents, chrom_len)
                        offspring2 = multi_parent_crossover(parents[::-1], chrom_len)
                    else:
                        raise ValueError("Invalid crossover method")
                    offspring_population += [offspring1, offspring2]
                else:
                    offspring_population += parents

            mutated_population = [mutation(chromosome, chrom_len, mutation_prob) for chromosome in offspring_population]
            fitness_values = [fitness(np.array(list(map(int, chromosome))), knapsack, c, alpha) for chromosome in mutated_population]
            population = [mutated_population[i] for i in np.argsort(fitness_values)[::-1][:pop_size]]

        best_solution = max(population, key=lambda chromosome: fitness(np.array(list(map(int, chromosome))), knapsack, c, alpha))
        best_solutions.append(best_solution)

    avg_best_solution = sum([fitness(np.array(list(map(int, chromosome))), knapsack, c, alpha) for chromosome in best_solutions]) / len(best_solutions)
    return avg_best_solution
