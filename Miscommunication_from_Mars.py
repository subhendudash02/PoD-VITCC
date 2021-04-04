li = []
for i in range(int(input())):
    li.append(int(input()))

d = int(input())
re = int(input())

for i in range(len(li)):
    for j in range(i, len(li)):
        if li[i] != li[j] and abs(li[i] - li[j]) == d and li[i] ^ li[j] == re:
            if li[i] < li[j]:
                print(str(li[i]) + "\t" + str(li[j]))
            else:
                print(str(li[j]) + "\t" + str(li[i]))            
