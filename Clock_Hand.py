# 14 March

le = input()
hr = int(input())
mi = int(input())

dic = {}

dic[0] = chr(ord(le) + 22)

x = 5
for i in range(ord(le), ord(le) + 24, 2):
    dic[x] = chr(i)
    x += 5
    
li1 = list(dic.keys())

if 13 <= hr <= 23:
    hr -= 12

if mi == 0:
    print("On", dic[hr * 5])
else:
    if hr == 0 or hr == 12:
        print("Between", dic[60], "and", le)
    else:
        print("Between", dic[hr * 5], "and", dic[(hr * 5) + 5])

if mi % 5 == 0:
    print("On", dic[mi])
else:
    for i in range(len(li1) - 1):
        if li1[i] < mi < li1[i + 1]:
            print("Between", dic[li1[i]], "and", dic[li1[i + 1]])
