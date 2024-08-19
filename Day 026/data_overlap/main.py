with open("file1.txt") as f1:
    file1 = f1.read().splitlines()

with open("file2.txt") as f2:
    file2 = f2.read().splitlines()

result = [int(item) for item in file1 if item in file2]

print(result)


