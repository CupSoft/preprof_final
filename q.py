from math import ceil


for t in range(0, 31):
    for ox in range(61):
        if t + ox/2 == 40:
            # print(t, ox)
            pass
for t in range(0, 31):
    for ox in range(61):
        if t + ox/2 == 20:
            # print(t, ox)
            pass

c = 56
k = c // 8
m = 200
s = 0
for i in range(k):
    vi = 2 * 1 * 200 / (m + 8 * i)
    s += vi
day_count_wihtout_growing = ceil((44 - ceil(s)) / 2)
day_count = day_count_wihtout_growing + k
fuel = day_count * 80
print(0)
# for i in range(day_count_wihtout_growing):
max_money = 1000000
for t in range(0, 31):
    for ox in range(61):
        if t + ox/2 == 20:
            e = t * (t + 1) // 2
            percent = ceil(e / 11)
            if percent <= 20:
                money = 8 * ox * 7 + percent * 10
                if money < max_money:
                    max_money = money
                    max_t = t
                    max_ox = ox                
                
print(money, max_t, max_ox)
