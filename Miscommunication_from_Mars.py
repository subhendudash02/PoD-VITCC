li = []
for i in range(int(input())):
    li.append(int(input()))

d = int(input())
re = int(input())

final = []

for i in range(len(li)):
    for j in range(len(li)):
        if li[i] != li[j] and abs(li[i] - li[j]) == d and li[i] ^ li[j] == re:
            if [li[i], li[j]] not in final and [li[j], li[i]] not in final:
                final.append([li[i], li[j]])

for i in final:
    i.sort()
    print(str(i[0]) + "\t" + str(i[1]))
