keys = ["name", "age", "city"]

values = ["Bob", 25, "London"]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)

result1= dict(zip(keys, values))

print(result1)