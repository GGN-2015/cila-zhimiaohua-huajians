import os
dirnow = os.path.dirname(os.path.abspath(__file__))

arr = []

for file in os.listdir(dirnow):
    filepath = os.path.join(dirnow, file)
    if os.path.isfile(filepath) and filepath.endswith(".txt"):
        arr.append(file[:-4])

from code_replace import replace_generated_code

if __name__ == "__main__":
    new_arr_code = "const arr = " + repr(sorted(arr)) + ";"
    print(new_arr_code)
    
    index_file = os.path.join(os.path.dirname(dirnow), "index.html")
    assert os.path.isfile(index_file)

    with open(index_file, encoding="utf-8") as fp:
        original_code = fp.read()

    with open(index_file, "w", encoding="utf-8") as fp:
        fp.write(replace_generated_code(original_code, new_arr_code))
    
    print("replaced")