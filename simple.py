import random
import string
import math
goal_string = input('Vpisite ciljni niz: ')
survival_ration = int(input("Vpisite kolicino osebkov populacije, ki preživi: v odstotkih "))
population_size = int(input('Vpisite velikost populacije (minimalno ' + str((survival_ration/100)**-1) +'): '))
mutation_rate = int(input('Vpisite moznost mutacije v procentih: '))
population_size = 100
survival_ration = 50
half = int(population_size*survival_ration/100)
alpha = string.ascii_letters + ' '
def Mutation(dnk):
    dnk = list(dnk)
    for i in range(len(dnk)):
        if(random.randint(0, 100) <= mutation_rate):
            dnk[i] = random.choice(alpha)
    return ''.join(dnk)
def Crossover(dnk1, dnk2):
    dnk1 = list(dnk1); dnk2 = list(dnk2)
    for i in range(len(dnk1)):
        if(random.randint(0, 1)):
            dnk1[i] = dnk2[i]
    return(''.join(dnk1))
def fitness(dnk):
    score = 0
    for i in range(len(dnk)): score += dnk[i] == goal_string[i]
    return score
random_word = lambda n : ''.join([random.choice(alpha) for i in range(n)])
pool = [(x, fitness(x)) for x in [random_word(len(goal_string)) for x in range(population_size)]]
pool.sort(key = lambda x : x[1], reverse = True)
def GeneticTraning(pool, population_size, goal_string):
    steps = []
    while pool[0][0] != goal_string:
        steps.append(pool[0])
        new_pool = []
        for element in pool[:half]:
            for i in range((element[1]+1)):
                new_pool.append(Mutation(Crossover(element[0], random.choice(pool)[0])))
        pool = [(a, fitness(a)) for a in new_pool] + pool
        pool.sort(key = lambda x : x[1], reverse = True)
        pool = pool[:population_size]
    return steps + [pool[0]]

steps = GeneticTraning(pool, population_size, goal_string)
for i in steps:
    print(i[1])