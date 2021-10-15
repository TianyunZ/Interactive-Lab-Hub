
f = open('taste.txt')
line = f.readline()
tast = ''
while line:
    taste = line
    line = f.readline()
f.close()
print(taste)

f = open('ingredient.txt')
line = f.readline()
ingredient = ''
while line:
    ingredient = line
    line = f.readline()
f.close()
print(ingredient)

recipe = []
if "tomato" in ingredient:
    recipe.append("tomato and beef soup")
if "beef" in ingredient:
    recipe.append("tomato and beef soup")
    recipe.append("mashed potato with steak")
if "potato" in ingredient:
    recipe.append("mashed potato and mushroom")
    recipe.append("mashed potato with steak")
if "mushroom" in ingredient:
    recipe.append("mashed potato and mushroom")
print(recipe)
recipe += recipe

f = open('recipes.txt', 'w')
for r in recipe:
	f.write(r)
	f.write('\n')
f.close()