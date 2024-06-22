import random

def mutation(chromosome, chrom_len, mutation_prob):
    mutated_chromosome = ''
    for i in range(chrom_len):
        if random.random() < mutation_prob:
            mutated_chromosome += '1' if chromosome[i] == '0' else '0'
        else:
            mutated_chromosome += chromosome[i]
    return mutated_chromosome
