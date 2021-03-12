from collections import *
l = int(input())
u = int(input())

li = {}

for a in range(1, u + 1):
    for b in range(1, u + 1):
        for c in range(1, u + 1):
            if a >= l and b >= l and c >= l:
                exp = (c ** 2) - (a ** 2) + (b ** 2)
                s = tuple(sorted([a, b, c]))
                if exp == 0 and s not in li:
                    #print(s, "Exactly Pythagorean")
                    li[s] = "E"  
                elif (exp == 1 or exp == -1) and s not in li:
                    #print(s, "Very Close to Pythagorean")
                    li[s] = "VE"
                elif (exp == 2 or exp == -2) and s not in li:
                    #print(s, "Close to Pythagorean")
                    li[s] = "C"
                    
li = OrderedDict(sorted(li.items()))

for i in li:
    if li[i] == "E":
        print(*i, "Exactly Pythagorean")
    elif li[i] == "VE":
        print(*i, "Very Close to Pythagorean")
    else:
        print(*i, "Close to Pythagorean")
