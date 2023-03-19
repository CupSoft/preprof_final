c = 56
k = c // 8
m = 200
s = 0
for i in range(k):
    vi = 2 * 1 * 200 / (m + 8 * i)
    s += vi
days = k

for t in range(0, 31):
    for ox in range(61):
        if t + ox/2 == 40:
            for w in range(81):
                