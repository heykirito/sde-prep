from collections import defaultdict, Counter
# Dictionaries brush up

users = {"name": "Amit", "age": 20, "role":"Dev"}

print(users.get("name"))
print(users.keys())
print(users.values())
print(users.items())

for k, v in users.items():
    print(k,v)



counts = defaultdict(int)
for x in ["a","b","c"]:
    counts[x] += 1

print(counts)

# Counter fucntion is Capital C never use small
c = Counter(["a", "b", "a", "c", "b", "a"])
print(c)

# Dictionaries comprehension

squares = {x: x*x for x in range(5)}
print(squares)

levels = ["INFO", "ERROR", "INFO", "WARNING"]
counts = {lvl: levels.count(lvl) for lvl in set(levels)}
print(counts)

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(d)
