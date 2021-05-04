n = int(input())
li = list(map(int, input().split()))

x = sorted(li)
y = sorted(li, reverse = True)

s = 0
fin = []

for i in range(n // 2):
    s += abs(x[i] - y[i])
    fin.extend([x[i], y[i]])

print(*fin)
print(s)
