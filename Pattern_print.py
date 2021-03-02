#2 March

n = int(input())
l = ['. ', '* ']

def dot(n):
    return l[0]*n
    
def star_mid(n):
    if n == 0:
        return l[1]
    else:
        return l[1] + l[0] * (n - 1) + l[1]
    
c = 0
for i in range(n - 1, -1, -1):
    if len(star_mid(c)) != (2*n - 1):
        f = dot(i) + star_mid(c) + dot(i)
        f = f.rstrip()
        print(f)
    else:
        f = star_mid(c)
        f = f.rstrip()
        print(f)
    c += 2
    
