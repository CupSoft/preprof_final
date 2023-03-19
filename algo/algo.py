from algo.shemas import DayPD
from math import sin, pi


def process_mission(points):
    results = []
    results_point = []
    day = 1
    base_weight = 192
    use_oxi = 0
    use_power_percent = 0
    for point in points:
        now_sh = 8
        now_dist_to = point["distance"]
        need_sh = point["SH"]
        flag = True
        while flag:
            for r_power in range(80, 0, -1):
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                if now_dist_to - speed > 0:
                    now_dist_to -= speed
                    use_oxi += now_sh * 2
                    use_power_percent += r_power
                    day += 1
                    use_power_percent += 20
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=20 + r_power, use_oxi=now_sh * 2,
                              distribution_engine=r_power, distribution_autoclave=20))
                    if r_power != 80:
                        flag = False
                    break
            else:
                flag = False

        flag = True
        while flag:
            for oxi in range(20, 0, -1):
                k = sin(-pi / 2 + (pi * (30 + 0.5 * oxi) / 40))
                if now_sh + now_sh * k <= need_sh + 8:
                    use_oxi += now_sh * oxi
                    now_sh = now_sh + now_sh * k
                    day += 1
                    use_power_percent += 43
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=43, use_oxi=now_sh * oxi,
                              distribution_engine=0, distribution_autoclave=43))
                    if oxi != 20:
                        flag = False
                    break
                else:
                    flag = False
        print(day)

        flag = True
        while flag:
            for r_power in range(1, 81):
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                if now_dist_to - speed < 0:
                    now_dist_to -= speed
                    use_oxi += now_sh * 2
                    use_power_percent += r_power
                    day += 1
                    use_power_percent += 20
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=r_power + 20, use_oxi=now_sh * 2,
                              distribution_engine=r_power, distribution_autoclave=20))
                    flag = False
                    break
            else:
                r_power = 80
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                now_dist_to -= speed
                use_oxi += now_sh * 2
                use_power_percent += r_power
                day += 1
                use_power_percent += 20
        results_point.append(PointPD(day=day, current_power=use_power_percent, current_oxi=use_oxi))

    return (results, results_point)
