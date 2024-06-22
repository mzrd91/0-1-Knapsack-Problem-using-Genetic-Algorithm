import random
import numpy as np

def selection(population, knapsack, tournament_size):
    selected = []
    for i in range(len(population)):
        tournament = random.sample(range(len(population)), tournament_size)
        fitness_values = [fitness(np.array(list(map(int, population[j]))), knapsack) for j in tournament]
        selected.append(population[tournament[np.argmax(fitness_values)]])
    return selected
