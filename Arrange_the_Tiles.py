n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
assert n == len(x)
assert n == len(y)

c = 0

while x != y:
    for i in range(len(x)):
        k = y.index(x[i])
        if (i != k):
            x[i], x[k] = x[k], x[i]
            #print(x)
            c += 1
            
print(c)
