def fitness(chromosome, knapsack, c, alpha):
    chromosome_arr = np.array(list(map(int, chromosome)))
    total_weight = np.sum(chromosome_arr * knapsack["weights"])
    total_value = np.sum(chromosome_arr * knapsack["values"])

    if total_weight > knapsack["capacity"]:
        penalty = total_value - c * (total_weight - knapsack["capacity"])
        total_value -= penalty
    elif np.count_nonzero(chromosome_arr) == 0:
        total_value = (total_weight - knapsack["capacity"]) - c

    return total_value
