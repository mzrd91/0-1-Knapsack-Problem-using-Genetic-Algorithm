# 0-1-Knapsack-Problem-using-Genetic-Algorithm

## Project Description

In this project, a binary-coded (bit-string) Genetic Algorithm (GA) is implemented to solve the 0-1 knapsack problem of size 20. The project involves creating weights, values, and knapsack capacity within specific bounds, implementing different crossover methods, and using both static and dynamic penalty methods for constraint handling. The primary goal is to find the optimal set of items that maximize the total value without exceeding the knapsack's capacity.

### Problem Instances

Three problem instances are created to evaluate the algorithm:
1. **Instance 1:** No items fit in the knapsack.
2. **Instance 2:** All items fit in the knapsack.
3. **Instance 3:** A regular case where only some items fit.

### Crossover Methods
1. **One-point Crossover:** A single crossover point is selected, and the offspring inherits genes from both parents up to this point.
2. **Uniform Crossover:** Each gene is randomly selected from one of the parents with a probability of 0.5.
3. **Multi-parent Crossover:** The offspring is created by selecting segments from multiple parents.

### Penalty Methods
- **Static Penalty:** Applied when the total weight exceeds the knapsack's capacity or when no items are selected.
- **Dynamic Penalty:** Adjusts the total value based on the degree of constraint violation.

### Genetic Algorithm Parameters

| Parameter                       | Value  |
|---------------------------------|--------|
| **Population Size**             | 50     |
| **Chromosome Length**           | 20     |
| **Number of Generations**       | 50     |
| **Crossover Probability**       | 0.8    |
| **Mutation Probability**        | 0.01   |
| **Number of Parents**           | 2      |
| **Tournament Size**             | 5      |
| **Static Penalty Constant (c)** | 10     |
| **Dynamic Penalty Coefficient (α)** | 0.1 |

