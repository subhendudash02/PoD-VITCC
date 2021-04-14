n = int(input())
li = list(map(int, input().split()))
assert len(li) == n

k = []
[k.append(i) for i in li if i not in k]

print(len(k) ** 2)
print(*k)
