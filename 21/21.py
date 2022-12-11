#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

allergensd = defaultdict(list)
ingredients_pending = set()
allergens_pending = set()
all_products = []

for line in stdin.readlines():
  ingredients_raw, allergens_raw = line.split(" (contains ")
  allergens_raw = allergens_raw.split(")")[0]
  allergens = allergens_raw.split(", ")
  ingredients = set(ingredients_raw.split(" "))
  
  ingredients_pending.update(ingredients)
  allergens_pending.update(allergens)
  all_products.append(ingredients)
  for allergen in allergens:
    allergensd[allergen].append(ingredients)
  print(ingredients)
  print(allergens)

print(allergensd)
print(allergens_pending)
print(ingredients_pending)
print(all_products)

answer_b = dict()

while allergens_pending:
  for allergen in allergens_pending.copy():
    common_ingredient = ingredients_pending.intersection(*allergensd[allergen])
    print("Common Ingredients for", allergen, common_ingredient)
    if len(common_ingredient) == 1:
      # the common_ingredient is the one that has the allergen
      common_ingredient = common_ingredient.pop()
      print(allergen, "is", common_ingredient)
      answer_b[allergen]=common_ingredient
      allergens_pending.remove(allergen)
      for product in all_products:
        product.discard(common_ingredient)
    print(allergensd)
    print(all_products)

print(all_products)

print(sum([len(x) for x in all_products]))      

print(",".join([answer_b[allergen] for allergen in sorted(list(answer_b.keys()))] ))
