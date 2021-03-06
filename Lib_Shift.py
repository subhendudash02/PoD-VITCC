#6 March

n = int(input())

li = [0, 0]

def trip(i, n):
    if i % 2 == 0:
        return [2*i, i]
    else:
        return [i, 2*i]
        
t = 1
dec = True
f = ''

while dec:
    if sum(trip(t, n)) <= n:
        li[0] += trip(t, n)[0]
        li[1] += trip(t, n)[1]
        n -= sum(trip(t, n))
        t += 1
        
    else:
        #t -= 1
        x = 0
        y = 0
        if t % 2 == 0:
            p = 2 * t
        else:
            p = t
        for i in range(1, n + 1):
            if i <= p:
                x += 1
            else:
                y += 1
                
        #print(x, y)
        
        li[0] += x
        li[1] += y
        
        if x < y or y == 0:
            f = "Ramu"
        else:
            f = "Somu"
        dec = False
    
print(t)
print(str(li[0]) + "\t" + str(li[1]))
print(f)
#print(li)
