# 3 March

M = int(input())
N = int(input())

def is_bit(x):
    if len(x) != 32:
        return (32 - len(x))*'0' + x
    else:
        return x

M_b = is_bit(bin(M).lstrip("0b"))[::-1]
N_b = is_bit(bin(N).lstrip("0b"))[::-1]

for i in range(32):
    if M_b[i] == N_b[i]:
        print(i + 1, end = " ")
