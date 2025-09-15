#! /usr/bin/python3

names = ["harry", "larry", "carry"]

for i in names:
    print(f"Hello {i}")

for index, name in enumerate(names, start=1):
    print(f"Hello {name} at position {index}")


for name in names:
    if name.startswith("l"):
        print(f"Found {name}")
        break
else:
    print("No name found starting with 'l'")