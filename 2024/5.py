import functools

file = open(0)

rules = []
for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

cache = {}

for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            key = (update[i], update[j])
            
            if key in cache and cache[key] == 1:
                return False
    return True

def cmp(x, y):
    return cache.get((x,y), 0)

sorted_total = 0
unsorted_total = 0
for line in file:
    update = list(map(int, line.split(",")))
    if is_ordered(update):
        sorted_total += update[len(update) // 2]
    else:
        update.sort(key =  functools.cmp_to_key(cmp))
        unsorted_total += update[len(update) // 2]
        


print(f"Sorted total is {sorted_total}" )
print(f"Unsorted total is {unsorted_total}")