d = input()
n = int(input())
m = int(input())
t = float(input())

if d == 'l':
    diff = abs(n - m) - 1
    x = "{d:.2f}"
    print(x.format(d = diff * t))
else:
    diff = abs(n - m) + 1
    x = "{d:.2f}"
    print(x.format(d = diff * t))
