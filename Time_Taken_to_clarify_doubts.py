#1 Mar
#Private test cases failed

def each_round(arr, t, time):
    for i in range(len(arr)):
        for j in range(t):
            arr[i] -= 1
            time += 1
            if arr[i] == 0:
                #arr.remove(arr[i])
                arr.sort()
                return time
    return time

li = []
n = int(input())
for i in range(n):
    li.append(int(input()))

li2 = list(li)

t = int(input())

p = each_round(li, t, 0)
final = []

for i in range(n):
    while 0 not in li:
        k = each_round(li, t, p)
        p = k
        if 0 in li:
            final.append(k)
            c = li.count(0)
            for j in range(c):
                li.remove(0)
            break

f = sorted(zip(sorted(li2), final))

for i in li2:
    for j in f:
        if j[0] == i:
            print(j[1])
