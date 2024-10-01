n = int(input())

extensions = {}

for _ in range(n):
    filename = input()
    ext = filename.split(".")[-1]
    if ext in extensions:
        extensions[ext] += 1
    else:
        extensions[ext] = 1

sorted_extensions = sorted(extensions.keys())

for ext in sorted_extensions:
    print(f"{ext} {extensions[ext]}")
