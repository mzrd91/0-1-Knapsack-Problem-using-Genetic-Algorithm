import random

def one_point_crossover(parents, chrom_len):
    crossover_point = random.randint(1, chrom_len - 1)
    offspring = parents[0][:crossover_point] + parents[1][crossover_point:]
    return offspring

def uniform_crossover(parents, chrom_len):
    offspring = []
    for i in range(chrom_len):
        if random.random() < 0.5:
            offspring.append(parents[0][i])
        else:
            offspring.append(parents[1][i])
    return ''.join(offspring)

def multi_parent_crossover(parents, chrom_len):
    num_parents = len(parents)
    num_points = random.randint(1, chrom_len - 1)
    points = random.sample(range(1, chrom_len), num_points)
    points.sort()
    child = ''
    for i in range(num_parents):
        if i == 0:
            segment_start = 0
        else:
            segment_start = points[i - 1]
        if i == num_parents - 1:
            segment_end = chrom_len
        else:
            segment_end = points[i]
        child += parents[i][segment_start:segment_end]
    return child
