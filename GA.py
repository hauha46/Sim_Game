import random
import pickle

lim = [[70,150], [1,3]]

def iniitialize():
    newCh = []
    for i in range(2):
        newCh.append(random.randint(lim[i][0], lim[i][1]))
    return newCh

def crossover(ch1, ch2):
    offspring = []
    for i in range(2):
        if random.random() <= 0.5:
            offspring.append(ch1[i])
        else:
            offspring.append(ch2[i])
    offspring = mutation(offspring)
    return offspring

def mutation(ch):
    mutated = []
    for i in range(2):
        if random.random() <= 0.01:
            mutated.append(random.randint(lim[i][0], lim[i][1]))
        else:
            mutated.append(ch[i])
    return mutated


def main():
    population = []
    try:
        with open('saved_chromosome', 'rb') as record:
            population = pickle.load(record)
            for i in population:
                print(i)
    except(FileNotFoundError):
        for i in range(10):
            temp = iniitialize()
            print(temp)
            population.append(temp)

    #TESTING AND SELECTION

    selection = input("4 selection of population:").split(", ")
    for i in range(4):
        selection[i] = int(selection[i])
    new_offspring = []

    new_offspring.append(crossover(population[selection[0]], population[selection[1]]))
    new_offspring.append(crossover(population[selection[0]], population[selection[2]]))
    new_offspring.append(crossover(population[selection[0]], population[selection[3]]))
    new_offspring.append(crossover(population[selection[1]], population[selection[2]]))
    new_offspring.append(crossover(population[selection[1]], population[selection[3]]))
    new_offspring.append(crossover(population[selection[2]], population[selection[3]]))

    for i in range(4):
        new_offspring.append(population[selection[i]])

    population = new_offspring

    with open('saved_chromosome', 'wb') as record:
        pickle.dump(population, record)

if __name__ == '__main__':
    main()