keys = ["math", "science", "english", "history"] 
default = 0
result = {}

for i in range(len(keys)):
    result[keys[i]] = default

print(result)
# fromkeys()
# Python har key ko same value assign kar deta hai.
# dict.fromkeys(["a", "b", "c"], 100)
# {'a':100, 'b':100, 'c':100}
result1 = dict.fromkeys(keys, default)

print(result1)