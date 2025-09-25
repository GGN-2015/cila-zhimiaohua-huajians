import os
dirnow = os.path.dirname(os.path.abspath(__file__))

arr = []

for file in os.listdir(dirnow):
    filepath = os.path.join(dirnow, file)
    if os.path.isfile(filepath) and filepath.endswith(".txt"):
        arr.append(file[:-4])

print(repr(arr))
