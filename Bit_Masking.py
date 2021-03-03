# 3 March

M = int(input())
N = int(input())

def is_bit(x):
    if len(x) != 32:
        return (32 - len(x))*'0' + x
    else:
        return x

M_b = bin(M)
N_b = bin(N)

M_b = M_b.rstrip()
M_b = M_b.lstrip("0b")

N_b = N_b.rstrip()
N_b = N_b.lstrip("0b")

M_b = is_bit(M_b)[::-1]
N_b = is_bit(N_b)[::-1]

for i in range(len(M_b)):
    for j in range(len(N_b)):
        if M_b[i] == N_b[j] and i == j:
            print(i + 1, end = " ")
            
