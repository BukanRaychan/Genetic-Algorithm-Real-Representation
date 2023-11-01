import math
import random
import os

def initializePopulation():

    #Real Chromosome Representaion [0,1] Interval

    population = []
    for _ in range(POPULATION_SIZE):
        population.append((random.uniform(0,1), random.uniform(0,1)))
    return population

def fitnessCalculation(decoded_population):
    fitness_of_population = []
    a = 0.01
    for individual in decoded_population:
        x1 = individual[0]
        x2 = individual[1]
        fitness_of_population.append(1/((-(math.sin(x1) * - math.cos(x2) + 4/5 * math.exp(1 - (x1**2 + x2 ** 2) ** 0.5))) + a))
    return fitness_of_population

def decodeChromosomeToIndividual(population):

    #Real Decoder from [0,1] Interval to [-10,-10] Interval

    decoded_population = []
    for chromosome in population:
        x1 = LOWER_LIMIT + (UPPER_LIMIT - LOWER_LIMIT) * chromosome[0]
        x2 = LOWER_LIMIT + (UPPER_LIMIT - LOWER_LIMIT) * chromosome[1]
        decoded_population.append((x1,x2))
    return decoded_population

def parentSelection(fitness_of_population, population):
    sorted_fitness = sorted(fitness_of_population)

    #Collect 2 largest fitness point i population

    return population[fitness_of_population.index(sorted_fitness[-1])], population[fitness_of_population.index(sorted_fitness[-2])]

def recombination(parent1, parent2):

    #Recombination using single arithmetic crossover

    alpha = random.uniform(0,1) #Random alpha value interval [0,1] in real number
    gen =  random.randint(0,1)
    
    #if the gen is 1 then change the second chromosome only else change the first one only
    if gen == 1:
        return (parent1[0], alpha * parent2[gen] + (1 - alpha) * parent1[gen]), (parent2[0], alpha * parent1[gen] + (1 - alpha) * parent2[gen])
    else:
        return (alpha * parent1[gen] + (1 - alpha) * parent2[gen], parent1[1]), (alpha * parent2[gen] + (1 - alpha) * parent1[gen], parent2[1])

def mutation(child1, child2):
    
    # Uniform Mutation

    list_of_child = [list(child1), list(child2)]

    for child in list_of_child:
        child[random.randint(0,1)] = random.uniform(0,1)

    return tuple(list_of_child[0]), tuple(list_of_child[1])

def exchangePopulation(population, fitness_of_population, child1, child2):
    new_population = population
    new_generation = [child1, child2]
    decoded_new_generation = decodeChromosomeToIndividual(new_generation)
    fitness_of_new_generation = fitnessCalculation(decoded_new_generation)

    sorted_population_fitness = sorted(fitness_of_population)

    for i in range (0, 2, 1):
        for j in range(-1, -POPULATION_SIZE - 1, -1):
            if sorted_population_fitness[j] < fitness_of_new_generation[i]:
                new_population[fitness_of_population.index(sorted_population_fitness[j])] = new_generation[i]
                break
            
    return new_population



def main():

    global POPULATION_SIZE, UPPER_LIMIT, LOWER_LIMIT, TARGET_MINIMUM_F
    POPULATION_SIZE = 20
    UPPER_LIMIT = 10
    LOWER_LIMIT = -10

    Limitation_of_change = 3000
    change_credit = 0
    generation = 0 
    best_fitness = float('-inf')
    best_individual = (0, 0)
    
    population = initializePopulation()
    while change_credit <= Limitation_of_change:
        # Decode Cromosom to individual
        decoded_population = decodeChromosomeToIndividual(population)

        # Fitness Calculation
        fitness_of_population = fitnessCalculation(decoded_population)

        # Parent Selection
        parent1, parent2 = parentSelection(fitness_of_population, population)

        # Recombination
        child1, child2 = recombination(parent1,parent2)
        
        # permutation
        mutated_child1, mutated_child2 = mutation(child1, child2)

        # Exchange Population
        population = exchangePopulation(population, fitness_of_population, mutated_child1, mutated_child2)

        if best_fitness < max(fitnessCalculation(population)):
            best_fitness = max(fitnessCalculation(population))
            best_individual = population[fitness_of_population.index(max(fitness_of_population))]
            change_credit = 0

        os.system('cls')
        print(f'Generation : {generation}\n')
        print(f'BEST INDIVIDUAL')
        print(f'x1 : {best_individual[0]}')
        print(f'x2 : {best_individual[1]}\n')
        print(f'BEST FITNESS: {best_fitness}\n')

        change_credit += 1
        generation += 1

main()

# # Decode Cromosom to individual
# decoded_population = decodeChromosomeToIndividual(population)
# print("============== DECODED POPULATION ============== ")
# print(decoded_population,"\n\n")

# # Fitness Calculation
# fitness_of_population = fitnessCalculation(decoded_population)
# print("============== FITNESS POPULATION ============== ")
# print(fitness_of_population,"\n\n")

# # Parent Selection
# parent1, parent2 = parentSelection(fitness_of_population, population)
# print(f'parent 1 : {parent1} \nparent 2 : {parent2}\n')

# # Recombination
# child1, child2 = recombination(parent1,parent2)
# print(f'child 1 : {child1} \nchild 2 : {child2}\n') 

# # permutation
# mutated_child1, mutated_child2 = mutation(child1, child2)
# print(f'mutated child 1 : {mutated_child1} \nmutated child 2 : {mutated_child2}\n') 

# # Exchange Population
# population = exchangePopulation(population, fitness_of_population, mutated_child1, mutated_child2)
# print("============== POPULATION ============== ")
# print(population,"\n\n")
