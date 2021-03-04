m = int(input())
n = int(input())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

l = arr[0]

for i in range(1, m):
    if set(l) != set(arr[i]):
        print("Not Shuffled Row Matrix")
        break
else:
    print("Shuffled Row Matrix")
