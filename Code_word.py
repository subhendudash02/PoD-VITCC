# 8 March

def finder(sen, letter):
    li = []
    for i in sen:
        if letter in i:
            li.append(i)
    return li
    
def issame(lis):
    a = lis[0]
    for i in range(1, len(lis)):
        if lis[i] != a:
            return False
    else:
        return True

def vowel_c(li):
    v = ['A', 'E', 'I', 'O', 'U']
    k = []
    for i in li:
        c = 0
        for j in i:
            if j in v:
                c += 1
        k.append(c)
    
    if issame(k):
        return True
    else:
        return False
        
l = input().split()
x = []
f = ""

for i in l:
    for j in i:
        li = finder(l, j)
        if len(li) == 2:
            if vowel_c(li) == False:
                break
        else:
            break
    else:
        f = i

print(f)
