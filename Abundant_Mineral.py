#28 Feb

dic = {}
for i in range(int(input())):
    x = input()
    for i in x:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

li = list(dic.values())

for i in dic:
    if dic[i] == max(li):
        print(i)
