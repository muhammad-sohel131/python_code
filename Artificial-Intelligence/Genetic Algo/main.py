countries = ["CANADA", "FRANCE", "BRAZIL", "JAPANL", "RUSSIA", "SWEDEN", "GREECE", "MEXICO"]
vowels = "AEIOU"

def calculate_fitness(country):
  score = sum(1 for c in country if c in vowels)
  return score

fitness_scores = {country: calculate_fitness(country) for country in countries}

sortedCountry = sorted(fitness_scores.items(), key = lambda x : x[1], reverse=True)[:4]
topCountry = [country for country, score in sortedCountry]

print("Top 4 Parents: ", topCountry)

def target_vowel_index(country):
  countVowel = 0
  for i, c in enumerate(country):
    if c in vowels:
      countVowel += 1
      if countVowel == 2:
        return i
  return -1

offspring = []
for i in range(0,4,2):
  parent1 = topCountry[i]
  parent2 = topCountry[i+1]

  cross_point = target_vowel_index(parent1)

  child1 = parent1[:cross_point] + parent2[cross_point:]
  child2 = parent2[:cross_point] + parent1[cross_point:]

  offspring.extend([child1, child2])

print("Offspring after crossover: ", offspring)

muted_offspring = []
for child in offspring:
  mutated_child = child.replace('A', 'X').replace('E','X')
  muted_offspring.append(mutated_child)

print("Final Offspring after mutation: ", muted_offspring)
