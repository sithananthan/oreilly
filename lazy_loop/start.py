#! /usr/bin/python3

names = ["harry", "larry", "carry"]

for i in names:
    print(f"Hello {i}")

for index, name in enumerate(names, start=1):
    print(f"Hello {name} at position {index}")