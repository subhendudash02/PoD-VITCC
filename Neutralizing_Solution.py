n = int(input())
li = list(map(int, input().split()))

for i in range(min(li), max(li) + 1):
    k = list(li)
    for j in range(len(k)):
        k[j] -= i
    if sum(k) == 0:
        print("Yes")
        print(i)
        break

else:
    print("No")
