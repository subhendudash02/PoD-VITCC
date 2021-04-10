#1st approach
a = int(input())
b = int(input())
c = int(input())

x = [a, b, c]
x.sort()
a, b, c = x

li = []

li.extend([a+b+c, a-b+c, a-b-c,a+b-c])
li.extend([a*b+c, a*b*c, a+b*c, a+b+c])
li.extend([a*b*c, a*b-c, a-b*c, a-b-c])

print(min(li))
print(li)

###############################################################

#2nd approach
a = int(input())
b = int(input())
c = int(input())

x = [a, b, c]
x.sort()
a, b, c = x

exp1 = a - b - c
exp2 = a - b * c
if exp1 < exp2:
    print(exp1)
else:
    print(exp2)
